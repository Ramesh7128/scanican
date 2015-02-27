# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('scanapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barcode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('scan_format', models.CharField(max_length=64)),
                ('scan_code', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('asin', models.CharField(max_length=64)),
                ('marketplace', models.IntegerField()),
                ('title', models.CharField(max_length=512, null=True)),
                ('product_type', models.CharField(max_length=128, null=True)),
                ('current_sales_rank', models.IntegerField(null=True)),
                ('current_new_price', models.FloatField(null=True)),
                ('current_new_quantity', models.IntegerField(null=True)),
                ('current_used_price', models.FloatField(null=True)),
                ('current_used_quantity', models.IntegerField(null=True)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sales_rank', models.IntegerField(null=True)),
                ('new_price', models.FloatField(null=True)),
                ('new_quantity', models.IntegerField(null=True)),
                ('used_price', models.IntegerField(null=True)),
                ('used_quantity', models.IntegerField(null=True)),
                ('added_date', models.DateTimeField(default=datetime.datetime.now)),
                ('product', models.ForeignKey(to='scanapp.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ScannedProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('matched_filter', models.BooleanField(default=True)),
                ('scanned_date', models.DateTimeField(null=True)),
                ('barcode', models.ForeignKey(to='scanapp.Barcode')),
                ('product', models.ForeignKey(to='scanapp.ProductHistory', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ScanSession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('place_name', models.CharField(max_length=128, null=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('total_scanned', models.IntegerField(default=0)),
                ('total_matched', models.IntegerField(default=0)),
                ('total_spent', models.FloatField(default=0.0)),
                ('total_profit', models.FloatField(default=0.0)),
                ('session_start', models.DateTimeField(null=True)),
                ('session_end', models.DateTimeField(null=True)),
                ('device', models.ForeignKey(to='scanapp.Device')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='scannedproduct',
            name='scansession',
            field=models.ForeignKey(to='scanapp.ScanSession'),
            preserve_default=True,
        ),
        migrations.AlterModelOptions(
            name='device',
            options={'ordering': ['registered_on'], 'verbose_name_plural': 'Devices'},
        ),
        migrations.AlterField(
            model_name='device',
            name='manufacturer',
            field=models.CharField(max_length=128, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='device',
            name='os',
            field=models.CharField(max_length=128, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='devicesession',
            name='device_token',
            field=models.CharField(max_length=512, blank=True),
            preserve_default=True,
        ),
    ]
