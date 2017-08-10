# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prisonSol', '0002_prisonappointmentsmaster_prisonnotificationmaster_prisonnotificationmaster_saver'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='image',
            field=models.ImageField(blank=True, upload_to='proifle_image'),
        ),
    ]
