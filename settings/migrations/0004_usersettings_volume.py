# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-29 07:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_auto_20180118_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersettings',
            name='volume',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]