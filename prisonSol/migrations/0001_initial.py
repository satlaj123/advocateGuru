# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodGroupMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('lastModifiedDateTime', models.CharField(null=True, blank=True, max_length=30)),
                ('activeYesNo', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CityMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('activeYesNo', models.BooleanField(default=False)),
                ('lastModifiedDateTime', models.CharField(null=True, blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CountryMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('activeYesNo', models.BooleanField(default=False)),
                ('lastModifiedDateTime', models.CharField(null=True, blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='GenderMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('lastDateTimeModified', models.DateTimeField()),
                ('lastModifiedBy', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('first_name', models.CharField(null=True, blank=True, max_length=100)),
                ('last_name', models.CharField(null=True, blank=True, max_length=100)),
                ('middle_name', models.CharField(null=True, blank=True, max_length=100)),
                ('mobile_number', models.BigIntegerField()),
                ('email', models.CharField(max_length=50)),
                ('aadhar_no', models.BigIntegerField()),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('activationToken', models.CharField(null=True, blank=True, max_length=20)),
                ('pincode', models.BigIntegerField(null=True, blank=True)),
                ('address', models.CharField(null=True, blank=True, max_length=100)),
                ('isProfileComplete', models.BooleanField(default=False)),
                ('activeYesNo', models.BooleanField(default=False)),
                ('lastModifiedDateTime', models.DateTimeField(null=True, auto_now_add=True)),
                ('blood_group', models.ForeignKey(null=True, blank=True, to='prisonSol.BloodGroupMaster')),
                ('city', models.ForeignKey(null=True, blank=True, to='prisonSol.CityMaster')),
                ('country', models.ForeignKey(null=True, blank=True, to='prisonSol.CountryMaster')),
                ('gender', models.ForeignKey(null=True, blank=True, to='prisonSol.GenderMaster')),
            ],
        ),
        migrations.CreateModel(
            name='StateMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('activeYesNo', models.BooleanField(default=False)),
                ('lastModifiedDateTime', models.CharField(null=True, blank=True, max_length=50)),
                ('country', models.ForeignKey(to='prisonSol.CountryMaster')),
            ],
        ),
        migrations.AddField(
            model_name='registration',
            name='state',
            field=models.ForeignKey(null=True, blank=True, to='prisonSol.StateMaster'),
        ),
        migrations.AddField(
            model_name='registration',
            name='user',
            field=models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='citymaster',
            name='state',
            field=models.ForeignKey(to='prisonSol.StateMaster'),
        ),
    ]
