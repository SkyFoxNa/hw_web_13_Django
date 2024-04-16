from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.forms import CharField, TextInput, EmailInput, EmailField, PasswordInput, ModelForm, ImageField, FileInput

from .models import Profile


class RegisterForm(UserCreationForm):
    username = CharField(max_length=16, min_length=5, required=True, widget=TextInput(attrs={"class": "form-control"}))
    email = EmailField(max_length=25, required=True, widget=EmailInput(attrs={"class": "form-control"}))
    password1 = CharField(required=True, widget=PasswordInput(attrs={"class": "form-control"}))
    password2 = CharField(required=True, widget=PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = CharField(max_length=16, min_length=3, required=True, widget=TextInput(attrs={"class": "form-control"}))
    password = CharField(required=True, widget=PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'password')


class ProfileForm(ModelForm):
    avatar = ImageField(widget=FileInput())

    class Meta:
        model = Profile
        fields = ['avatar']


class CustomPasswordResetForm(ModelForm):
    email = EmailField(max_length=25, required=True, widget=EmailInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ('email',)


class ResetPasswordFormSite(ModelForm):
    password = CharField(required = True, widget = PasswordInput(attrs = {"class" : "form-control"}),
                         label = "Введіть ваш старий пароль:")
    password1 = CharField(required = True, widget = PasswordInput(attrs = {"class" : "form-control"}),
                          label = "Введіть новий пароль:")
    password2 = CharField(required = True, widget = PasswordInput(attrs = {"class" : "form-control"}),
                          label = "Підтвердіть новий пароль:")

    class Meta:
        model = User
        fields = ('password', 'password1', 'password2',)
