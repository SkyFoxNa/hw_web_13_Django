from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from . import views
from .forms import LoginForm

app_name = "users"

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name = 'register'),
    path('login/',
         LoginView.as_view(template_name = 'users/login.html', form_class = LoginForm,
                           redirect_authenticated_user = True), name = 'login'),
    path('logout/', LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'),
    path('profile/', views.profile, name = 'profile'),
    path('reset_password/', views.ResetPassword.as_view(template_name = 'users/reset_password.html'),
         name = 'reset_password'),
    path('reset_password_site/', views.ChangePasswordView.as_view(template_name = 'users/reset_password_site.html'),
         name = 'reset_password_site'),
]
