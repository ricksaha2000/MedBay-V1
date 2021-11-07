from django.urls import path
from .apps import MedbayAdminConfig
from .views import DashboardView
from user.decorators import admin_required

app_name = MedbayAdminConfig.name

urlpatterns = [
    path("dashboard/", admin_required(DashboardView.as_view()), name="dashboard"),
]
