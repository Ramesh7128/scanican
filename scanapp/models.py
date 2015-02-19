from django.db import models
from datetime import datetime
from django.contrib.auth.models import User, UserManager


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    encrypted_user_id = models.CharField(max_length=256, unique=True)
    activation_code = models.CharField(max_length=32, null=True)
    activated = models.BooleanField(default=False)
    added_date = models.DateTimeField(default=datetime.now)
    #subscription_plan = models.ForeignKey(UserSubscriptionPlan, null=True)

    def __unicode__(self):
        return self.user.first_name

class Device(models.Model):
    userprofile = models.ForeignKey(UserProfile, null=True)
    device_id = models.CharField(max_length=512)
    os = models.CharField(max_length=128, null=True)
    manufacturer = models.CharField(max_length=128, null=True)
    registered_on = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return self.device_id


class DeviceSession(models.Model):

    device = models.ForeignKey(Device)
    device_token = models.CharField(max_length=512)
    new_token = models.CharField(max_length=512, null=True)
    is_valid = models.BooleanField(default=True)
    issued_date = models.DateTimeField(default=datetime.now)
    expiry_date = models.DateTimeField(null=True)

    def __unicode__(self):
        return self.device

