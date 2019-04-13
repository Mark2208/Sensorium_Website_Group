# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-12 19:35
from __future__ import unicode_literals

import cms.models.fields
from django.db import migrations, models
import django.db.models.deletion
import sensoriumSite.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placeholder', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, slotname=sensoriumSite.models.slot_siteDescription, to='cms.Placeholder')),
            ],
        ),
    ]