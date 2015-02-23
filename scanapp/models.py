from django.db import models
from datetime import datetime
from django.contrib.auth.models import User, UserManager
import uuid


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    encrypted_user_id = models.CharField(max_length=256, unique=True)
    activation_code = models.CharField(max_length=32, null=True)
    activated = models.BooleanField(default=False)
    added_date = models.DateTimeField(default=datetime.now)
    #subscription_plan = models.ForeignKey(UserSubscriptionPlan, null=True)

    def __unicode__(self):
        return self.user.username

class Device(models.Model):

    userprofile = models.ForeignKey(UserProfile, null=True)
    device_id = models.CharField(max_length=512)
    os = models.CharField(max_length=128, null=True, blank=True)
    manufacturer = models.CharField(max_length=128, null=True, blank=True)
    registered_on = models.DateTimeField(default=datetime.now)

    class Meta:
        ordering = ['registered_on']
        verbose_name_plural = 'Devices'

    def __unicode__(self):
        return self.device_id



class DeviceSession(models.Model):

    device = models.ForeignKey(Device)
    device_token = models.CharField(max_length=512, blank=True)
    new_token = models.CharField(max_length=512, null=True)
    is_valid = models.BooleanField(default=True)
    issued_date = models.DateTimeField(default=datetime.now)
    expiry_date = models.DateTimeField(null=True)

    def __unicode__(self):
        return self.device_token


class ScanSession(models.Model):

    device = models.ForeignKey(Device)
    place_name = models.CharField(max_length=128, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    total_scanned = models.IntegerField(default=0)
    total_matched = models.IntegerField(default=0)
    total_spent = models.FloatField(default=0.0)
    total_profit = models.FloatField(default=0.0)
    session_start = models.DateTimeField(null=True)
    session_end = models.DateTimeField(null=True)


class ScannedProduct(models.model):

    scansession = models.ForeignKey(ScanSession)
    barcode = models.ForeignKey(Barcode)
    product = models.ForeignKey(ProductHistory, null=True)
    matched_filter = models.BooleanField(default=True)
    scanned_date = models.DateTimeField(null=True)


class Barcode(models.Model):

    scan_format = models.CharField(max_length=64)



