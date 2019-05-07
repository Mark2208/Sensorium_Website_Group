# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-28 18:38
from __future__ import unicode_literals

import cms.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('sensoriumSite', '0005_sensorium_bio_plc_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='plc_AlistairLawson_description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plc', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, slotname='Alistair Lawson', to='cms.Placeholder')),
            ],
        ),
        migrations.CreateModel(
            name='plc_AugustoEsteves_description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plc', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, slotname='Augusto Esteves', to='cms.Placeholder')),
            ],
        ),
        migrations.CreateModel(
            name='plc_CallumEgan_description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plc', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, slotname='Callum Egan', to='cms.Placeholder')),
            ],
        ),
        migrations.CreateModel(
            name='plc_ClaireAlexander_description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plc', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, slotname='Claire Alexander', to='cms.Placeholder')),
            ],
        ),
        migrations.CreateModel(
            name='plc_DrRichardHetherington_description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plc', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, slotname='Dr Richard Hetherington', to='cms.Placeholder')),
            ],
        ),
        migrations.CreateModel(
            name='plc_DrThomasMethven_description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plc', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, slotname='Dr Thomas Methven', to='cms.Placeholder')),
            ],
        ),
        migrations.CreateModel(
            name='plc_IngiHelgason_description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plc', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, slotname='Ingi Helgason', to='cms.Placeholder')),
            ],
        ),
        migrations.CreateModel(
            name='plc_JohnMorisson_description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plc', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, slotname='John Morisson', to='cms.Placeholder')),
            ],
        ),
        migrations.CreateModel(
            name='plc_LauraMuir_description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plc', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, slotname='Laura Muir', to='cms.Placeholder')),
            ],
        ),
        migrations.CreateModel(
            name='plc_OliMival_description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plc', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, slotname='Oli Mival', to='cms.Placeholder')),
            ],
        ),
        migrations.CreateModel(
            name='plc_ProfXiaodongLiu_description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plc', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, slotname='Prof Xiaodong Liu', to='cms.Placeholder')),
            ],
        ),
        migrations.CreateModel(
            name='plc_QiLiu_description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plc', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, slotname='Qi Liu', to='cms.Placeholder')),
            ],
        ),
    ]
