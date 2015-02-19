# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('device_id', models.CharField(max_length=512)),
                ('os', models.CharField(max_length=128, null=True)),
                ('manufacturer', models.CharField(max_length=128, null=True)),
                ('registered_on', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DeviceSession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('device_token', models.CharField(max_length=512)),
                ('new_token', models.CharField(max_length=512, null=True)),
                ('is_valid', models.BooleanField(default=True)),
                ('issued_date', models.DateTimeField(default=datetime.datetime.now)),
                ('expiry_date', models.DateTimeField(null=True)),
                ('device', models.ForeignKey(to='scanapp.Device')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('encrypted_user_id', models.CharField(unique=True, max_length=256)),
                ('activation_code', models.CharField(max_length=32, null=True)),
                ('activated', models.BooleanField(default=False)),
                ('added_date', models.DateTimeField(default=datetime.datetime.now)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='device',
            name='userprofile',
            field=models.ForeignKey(to='scanapp.UserProfile', null=True),
            preserve_default=True,
        ),
    ]
