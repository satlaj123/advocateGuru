# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advocateInfo', '0003_remove_advocateprofile_profilephoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, null=True, max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('subject', models.CharField(blank=True, null=True, max_length=100)),
                ('message', models.CharField(max_length=300)),
            ],
        ),
    ]
