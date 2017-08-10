# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('prisonSol', '0002_prisonappointmentsmaster_prisonnotificationmaster_prisonnotificationmaster_saver'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvocateAppointmentsMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('appointment_date_time', models.DateTimeField(null=True, blank=True)),
                ('status', models.CharField(choices=[('Confirmed', 1), ('Rejected', 2), ('Hold', 3), ('Pending', 4)], max_length=20)),
                ('isActiveYesNO', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='AdvocateNotificationMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('notification_name', models.CharField(null=True, blank=True, max_length=200)),
                ('created_at', models.DateTimeField(null=True, blank=True)),
                ('last_modified_date_time', models.DateTimeField(null=True, blank=True)),
                ('isActiveYesNO', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='AdvocateNotificationMaster_saver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('notification_name', models.CharField(null=True, blank=True, max_length=200)),
                ('created_at', models.DateTimeField(null=True, blank=True)),
                ('last_modified_date_time', models.DateTimeField(null=True, blank=True)),
                ('isActiveYesNO', models.BooleanField(default=True)),
                ('notification_time', models.TimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AdvocateProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('dob', models.DateField(null=True, blank=True)),
                ('profilePhoto', models.URLField(null=True, blank=True)),
                ('address', models.CharField(null=True, blank=True, max_length=100)),
                ('license_no', models.CharField(null=True, blank=True, max_length=100)),
                ('pincode', models.BigIntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AdvocateUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('mobile_number', models.CharField(null=True, blank=True, max_length=100)),
                ('email', models.CharField(null=True, blank=True, max_length=100)),
                ('aadhar_no', models.CharField(null=True, blank=True, max_length=100)),
                ('activationToken', models.CharField(null=True, blank=True, max_length=50)),
                ('activationAttempts', models.IntegerField(null=True, blank=True, default=0)),
                ('isProfileComplete', models.BooleanField(default=False)),
                ('active_yesNo', models.BooleanField(default=False)),
                ('last_modified_by', models.BigIntegerField(null=True, blank=True)),
                ('last_modified_date_time', models.DateTimeField(null=True, auto_now_add=True)),
                ('pTime', models.DateTimeField(null=True, blank=True)),
                ('advocatePrison', models.ForeignKey(null=True, blank=True, to='prisonSol.Registration')),
                ('user', models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('day', models.CharField(null=True, blank=True, max_length=100)),
                ('date', models.DateField(null=True, blank=True)),
                ('from_time', models.TimeField(null=True, blank=True)),
                ('to_time', models.TimeField(null=True, blank=True)),
                ('venue', models.CharField(null=True, blank=True, max_length=100)),
                ('total_availability', models.IntegerField(null=True, blank=True)),
                ('doctorId', models.ForeignKey(null=True, blank=True, to='advocateInfo.AdvocateUser')),
            ],
        ),
        migrations.AddField(
            model_name='advocateprofile',
            name='advocateId',
            field=models.OneToOneField(null=True, blank=True, to='advocateInfo.AdvocateUser'),
        ),
        migrations.AddField(
            model_name='advocateprofile',
            name='cityId',
            field=models.ForeignKey(null=True, blank=True, to='prisonSol.CityMaster'),
        ),
        migrations.AddField(
            model_name='advocateprofile',
            name='countryId',
            field=models.ForeignKey(null=True, blank=True, to='prisonSol.CountryMaster'),
        ),
        migrations.AddField(
            model_name='advocateprofile',
            name='gender',
            field=models.ForeignKey(null=True, blank=True, to='prisonSol.GenderMaster'),
        ),
        migrations.AddField(
            model_name='advocateprofile',
            name='stateId',
            field=models.ForeignKey(null=True, blank=True, to='prisonSol.StateMaster'),
        ),
        migrations.AddField(
            model_name='advocatenotificationmaster_saver',
            name='advocateId',
            field=models.ForeignKey(null=True, blank=True, to='advocateInfo.AdvocateUser'),
        ),
        migrations.AddField(
            model_name='advocatenotificationmaster',
            name='advocateId',
            field=models.ForeignKey(null=True, blank=True, to='advocateInfo.AdvocateUser'),
        ),
        migrations.AddField(
            model_name='advocateappointmentsmaster',
            name='advocateId',
            field=models.ForeignKey(null=True, blank=True, to='advocateInfo.AdvocateUser'),
        ),
        migrations.AddField(
            model_name='advocateappointmentsmaster',
            name='prisonId',
            field=models.ForeignKey(null=True, blank=True, to='prisonSol.Registration'),
        ),
        migrations.AddField(
            model_name='advocateappointmentsmaster',
            name='venue_decided',
            field=models.ForeignKey(null=True, blank=True, to='advocateInfo.ScheduleMaster'),
        ),
    ]
