from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class Schedule(models.Model):
    doc = models.ForeignKey(Doctor, on_delete=models.CASCADE)


class Hospital(models.Model):
    hosp_name = models.CharField(
        max_length=100, null=True, blank=True, default='')
    hosp_code = models.CharField(primary_key=True, max_length=20)
    hosp_address = models.CharField(
        max_length=200, null=True, blank=True, default='')

    def __str__(self):
        return self.hosp_name


class Test(models.Model):
    hosp = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    test_name = models.CharField(
        max_length=100, null=True, blank=True, default='')
    test_price = models.CharField(max_length=6)

    def __str__(self):
        return self.test_name
