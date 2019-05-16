# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-12 15:51
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0003_auto_20190512_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeschedule1',
            name='payment_date',
            field=models.DateField(verbose_name=datetime.datetime(2019, 5, 12, 21, 51, 27, 787674)),
        ),
        migrations.AlterField(
            model_name='ourevents1',
            name='end_date',
            field=models.DateField(verbose_name=datetime.datetime(2019, 5, 12, 21, 51, 27, 791695)),
        ),
        migrations.AlterField(
            model_name='ourevents1',
            name='start_date',
            field=models.DateField(verbose_name=datetime.datetime(2019, 5, 12, 21, 51, 27, 791695)),
        ),
    ]