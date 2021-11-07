from django.urls import path
from .apps import SellerConfig
from .views import DashboardView
from user.decorators import seller_required

app_name = SellerConfig.name

urlpatterns = [
    path("dashboard/", seller_required(DashboardView.as_view()), name="dashboard"),
]
