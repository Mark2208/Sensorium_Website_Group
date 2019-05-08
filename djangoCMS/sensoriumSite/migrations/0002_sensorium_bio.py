# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-25 13:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('sensoriumSite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensorium_Bio',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='sensoriumsite_sensorium_bio', serialize=False, to='cms.CMSPlugin')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('img_name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]