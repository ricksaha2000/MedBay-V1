from django.urls import path
from .views import (
    LoginView,
    SignUpView,
)
from .apps import UserConfig

app_name = UserConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("signup/", SignUpView.as_view(), name="login"),
]
