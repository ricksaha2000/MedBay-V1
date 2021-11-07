from django.urls import path
from .apps import PatientConfig
from .views import DashboardView, compare_test, search_tests
from user.decorators import patient_required

app_name = PatientConfig.name

urlpatterns = [
    path("dashboard/", (DashboardView.as_view()), name="dashboard"),
    path("test/", compare_test, name="test"),
    path("searchtest/", search_tests, name="search_tests")

]
