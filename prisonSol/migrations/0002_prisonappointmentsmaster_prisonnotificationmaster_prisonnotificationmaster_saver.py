# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prisonSol', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrisonAppointmentsMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('advocateId', models.CharField(null=True, blank=True, max_length=100)),
                ('appointment_date_time', models.DateTimeField(null=True, auto_now_add=True)),
                ('status', models.CharField(choices=[('Confirmed', 1), ('Rejected', 2), ('Pending', 3)], max_length=50)),
                ('isActiveYesNo', models.BooleanField(default=True)),
                ('prisonId', models.ForeignKey(null=True, blank=True, to='prisonSol.Registration')),
            ],
        ),
        migrations.CreateModel(
            name='PrisonNotificationMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('notification_type_id', models.CharField(null=True, blank=True, max_length=100)),
                ('notification_type', models.CharField(null=True, blank=True, max_length=100)),
                ('notification_name', models.CharField(null=True, blank=True, max_length=100)),
                ('created_at', models.DateTimeField(null=True, auto_now_add=True)),
                ('last_modified_date_time', models.DateTimeField(null=True, auto_now_add=True)),
                ('isActiveYesNo', models.BooleanField(default=True)),
                ('prisonId', models.ForeignKey(null=True, blank=True, to='prisonSol.Registration')),
            ],
        ),
        migrations.CreateModel(
            name='PrisonNotificationMaster_saver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('notification_type_id', models.CharField(null=True, blank=True, max_length=100)),
                ('notification_type', models.CharField(null=True, blank=True, max_length=100)),
                ('notification_name', models.CharField(null=True, blank=True, max_length=100)),
                ('created_at', models.DateTimeField(null=True, auto_now_add=True)),
                ('last_modified_date_time', models.DateTimeField(null=True, auto_now_add=True)),
                ('isActiveYesNo', models.BooleanField(default=True)),
                ('notification_time', models.TimeField(null=True, auto_now_add=True)),
                ('prisonId', models.ForeignKey(null=True, blank=True, to='prisonSol.Registration')),
            ],
        ),
    ]
