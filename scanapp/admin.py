from django.contrib import admin
from scanapp.models import Device, DeviceSession, UserProfile, ScanSession
# Register your models here.

admin.site.register(Device)
admin.site.register(DeviceSession)
admin.site.register(UserProfile)
admin.site.register(ScanSession)
