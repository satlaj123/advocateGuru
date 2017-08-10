# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prisonSol', '0002_prisonappointmentsmaster_prisonnotificationmaster_prisonnotificationmaster_saver'),
        ('advocateInfo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advocateprofile',
            old_name='cityId',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='advocateprofile',
            old_name='countryId',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='advocateprofile',
            old_name='stateId',
            new_name='state',
        ),
        migrations.RemoveField(
            model_name='advocateuser',
            name='pTime',
        ),
        migrations.AddField(
            model_name='advocateuser',
            name='blood_group',
            field=models.ForeignKey(to='prisonSol.BloodGroupMaster', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='advocateuser',
            name='middle_name',
            field=models.CharField(blank=True, null=True, max_length=200),
        ),
    ]
