# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 12:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=200)),
                ('location', models.CharField(blank=True, max_length=50)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic/')),
                ('car_model', models.CharField(blank=True, max_length=30)),
                ('car_number_plates', models.CharField(blank=True, max_length=30)),
                ('car_capacity', models.IntegerField(default=0)),
                ('car_image', models.ImageField(blank=True, null=True, upload_to='car_images/')),
                ('car_color', models.CharField(blank=True, max_length=30)),
                ('current_location', models.CharField(max_length=10)),
                ('destination', models.CharField(blank=True, max_length=30, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TripPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_location', models.CharField(max_length=30)),
                ('destination', models.CharField(max_length=30)),
                ('driver_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drivers.Driver_profile')),
            ],
        ),
    ]
