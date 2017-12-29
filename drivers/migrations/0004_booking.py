# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 15:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rider', '0001_initial'),
        ('drivers', '0003_driver_profile_free_space'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rider_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rider.Rider_profile')),
                ('trip_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drivers.TripPlan')),
            ],
        ),
    ]
