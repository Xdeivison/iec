# Generated by Django 3.0.8 on 2020-08-11 17:47

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vismet', '0006_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='area_km2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='cod_ibge',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='data',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='esc_local',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='estrutura',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='fid',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='fonte',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='geom',
            field=django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='city',
            name='lei_criaca',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='macroestad',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='microestad',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='nome',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='origem',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='percen_are',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='perim_m',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='regional',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
