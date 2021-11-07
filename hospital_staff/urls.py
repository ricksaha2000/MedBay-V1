from django.urls import path
from .apps import HospitalStaffConfig
from .views import DashboardView
from user.decorators import staff_required

app_name = HospitalStaffConfig.name

urlpatterns = [
    path("dashboard/", staff_required(DashboardView.as_view()), name="dashboard"),
]
