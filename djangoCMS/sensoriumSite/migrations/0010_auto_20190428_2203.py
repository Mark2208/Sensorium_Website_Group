# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-28 21:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sensoriumSite', '0009_auto_20190428_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensorium_news',
            name='Facebook_link',
        ),
        migrations.RemoveField(
            model_name='sensorium_news',
            name='Linkedin_link',
        ),
        migrations.RemoveField(
            model_name='sensorium_news',
            name='Twitter_link',
        ),
    ]