from django.contrib import admin
from doctor.models import Doctor, Schedule, Hospital, Test

admin.site.register(Doctor)
admin.site.register(Schedule)
admin.site.register(Hospital)
admin.site.register(Test)
