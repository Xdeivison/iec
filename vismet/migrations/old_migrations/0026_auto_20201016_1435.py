# Generated by Django 3.1.2 on 2020-10-16 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vismet', '0025_auto_20201007_1400'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WeatherStation',
            new_name='Station',
        ),
        migrations.AlterField(
            model_name='inmetstationdata',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inmet_data', to='vismet.station'),
        ),
        migrations.AlterField(
            model_name='xavierstationdata',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='xavier_data', to='vismet.station'),
        ),
        migrations.DeleteModel(
            name='XavierStation',
        ),
    ]