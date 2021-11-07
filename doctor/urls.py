from django.urls import path
from .apps import DoctorConfig
from .views import DashboardView
from user.decorators import doctor_required

app_name = DoctorConfig.name

urlpatterns = [
    path("dashboard/", doctor_required(DashboardView.as_view()), name="dashboard"),
]
