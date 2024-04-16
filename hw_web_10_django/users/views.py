import random
import string
from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string

from .forms import RegisterForm, ProfileForm, CustomPasswordResetForm, ResetPasswordFormSite


# Create your views here.


@login_required
def profile(request) :
    return render(request, 'users/profile.html')


@login_required
def profile(request) :
    if request.method == 'POST' :
        profile_form = ProfileForm(request.POST, request.FILES, instance = request.user.profile)
        if profile_form.is_valid() :
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to = 'users:profile')

    profile_form = ProfileForm(instance = request.user.profile)
    return render(request, 'users/profile.html', {'profile_form' : profile_form})


class RegisterView(View) :
    template_name = 'users/register.html'
    form_class = RegisterForm

    def dispatch(self, request, *args, **kwargs) :
        if request.user.is_authenticated :
            return redirect(to = "users:register")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request) :
        return render(request, self.template_name, {"form" : self.form_class})

    def post(self, request) :
        form = self.form_class(request.POST)
        if form.is_valid() :
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request, f"Вітаємо {username}! Ваш акаунт успішно зареєстровано!")
            return redirect(to = "users:login")
        return render(request, self.template_name, {"form" : form})


class ResetPassword(View) :
    template_name = 'users/reset_password.html'
    form_class = CustomPasswordResetForm

    def get(self, request) :
        return render(request, self.template_name, {"form" : self.form_class})

    def post(self, request) :
        email = self.form_class(request.POST).data.get('email')
        user = User.objects.filter(email = email).exists()
        if not user :
            messages.success(self.request, 'The user with the specified email does not exist.')
            return redirect(to = "users:reset_password")
        user = User.objects.filter(email = email).first()
        new_password = ''.join(random.choices(string.ascii_letters + string.digits, k = 10))
        user.set_password(new_password)
        user.save()
        subject = 'New password'
        message = render_to_string('users/password_reset_email.html', {
            'username' : user.username,
            'password' : new_password,
        })

        user.email_user(subject, message, html_message = message)
        messages.success(self.request, 'The password reset email was sent successfully.')
        return render(request, self.template_name, {"form" : email})


class ChangePasswordView(View) :
    template_name = 'reset_password_site.html'
    form_class = ResetPasswordFormSite

    def get(self, request) :
        return render(request, self.template_name, {"form" : self.form_class})

    def post(self, request) :
        form = self.form_class(request.POST)
        if form.is_valid() :
            password = self.form_class(request.POST).data.get('password')
            password1 = self.form_class(request.POST).data.get('password1')
            password2 = self.form_class(request.POST).data.get('password2')
            email = request.user.email
            user = User.objects.filter(email = email).first()
            if user.check_password(password) :
                if password1 == password2 :
                    try :
                        password_validation.validate_password(password1)
                        user = User.objects.filter(email = email).first()
                        user.set_password(password1)
                        user.save()
                        messages.success(request, 'Your password was successfully updated!')
                    except forms.ValidationError as error :
                        messages.success(request, 'The new password is not validated')

                else :
                    messages.success(request, 'Passwords1 and Passwords2 do not match.')
            else:
                messages.success(request, 'Passwords do not match.')
            return render(request, self.template_name, {'form' : form})
        else :
            messages.error(request, 'Please correct the error below.')
            return render(request, self.template_name, {'form' : form})
