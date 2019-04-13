# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-12 21:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sensoriumSite', '0005_testplugin'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymainmodel',
            name='description',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, verbose_name='description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mymainmodel',
            name='text',
            field=models.CharField(default=django.utils.timezone.now, max_length=200, verbose_name='text'),
            preserve_default=False,
        ),
    ]