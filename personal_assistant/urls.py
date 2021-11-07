from django.urls import path
from .apps import PersonalAssistantConfig
from .views import DashboardView
from user.decorators import pa_required

app_name = PersonalAssistantConfig.name

urlpatterns = [
    path("dashboard/", pa_required(DashboardView.as_view()), name="dashboard"),
]
