# Generated by Django 3.1.2 on 2020-11-17 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vismet', '0018_auto_20201111_1010'),
    ]

    operations = [
        migrations.CreateModel(
            name='PixelData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('evapo', models.FloatField(blank=True, default=None, null=True)),
                ('minTemp', models.FloatField(blank=True, default=None, null=True)),
                ('maxTemp', models.FloatField(blank=True, default=None, null=True)),
                ('ocis', models.FloatField(blank=True, default=None, null=True)),
                ('precip', models.FloatField(blank=True, default=None, null=True)),
                ('rnof', models.FloatField(blank=True, default=None, null=True)),
                ('tp2m', models.FloatField(blank=True, default=None, null=True)),
                ('data_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pixel_data', to='vismet.datamodel')),
                ('pixel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pixel_data', to='vismet.pixel')),
            ],
        ),
    ]