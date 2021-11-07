"""medbay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import index, myajaxtestviewtext
from patient.views import heart_beat

urlpatterns = [
    path("", index),
    path('my-ajax-test-text/', myajaxtestviewtext, name='myajaxtestviewtext'),
    path("doctor/", include('doctor.urls')),
    path("patient/", include('patient.urls')),
    path("admin/", include('medbay_admin.urls')),
    path("hospital_staff/", include('hospital_staff.urls')),
    path("personal_assistant/", include('personal_assistant.urls')),
    path("pharmacy/", include('pharmacy.urls')),
    path("seller/", include('seller.urls')),
    path("", include('user.urls')),
    path('superuser/', admin.site.urls),
    path('heart_beat/', heart_beat),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
