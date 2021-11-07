from django.urls import path
from .apps import PharmacyConfig
from .views import DashboardView
from user.decorators import pharmacy_required

app_name = PharmacyConfig.name

urlpatterns = [
    path("dashboard/", pharmacy_required(DashboardView.as_view()), name="dashboard"),
]
