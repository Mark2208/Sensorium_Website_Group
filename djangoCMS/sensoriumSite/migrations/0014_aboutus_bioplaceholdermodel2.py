# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-28 21:23
from __future__ import unicode_literals

import cms.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('sensoriumSite', '0013_auto_20190428_2221'),
    ]

    operations = [
        migrations.CreateModel(
            name='aboutUs_BioPlaceholderModel2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plc_bio', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, slotname='Bio Line', to='cms.Placeholder')),
            ],
        ),
    ]
