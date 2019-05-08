# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-29 01:41
from __future__ import unicode_literals

import cms.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('sensoriumSite', '0018_project_descriptionplaceholdermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='news_descriptionPlaceholderModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plc_description', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, slotname='Description', to='cms.Placeholder')),
            ],
        ),
    ]