# Generated by Django 3.0.8 on 2020-08-06 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vismet', '0003_heatpixeltimeseries'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HeatPixelTimeSeries',
            new_name='HeatPixelData',
        ),
    ]
