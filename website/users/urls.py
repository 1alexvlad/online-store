from django.urls import path
from users.views import register
from django.contrib.auth.views import LoginView, LogoutView


app_name = "users"

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", LoginView.as_view(template_name='users/login.html'), name="login"),
    path("logout/", LoginView.as_view(template_name='users/logout.html'), name="logout"),
]