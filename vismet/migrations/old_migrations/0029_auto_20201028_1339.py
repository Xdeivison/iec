# Generated by Django 3.1.2 on 2020-10-28 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vismet', '0028_auto_20201026_1441'),
        ('vismet', '0028_pixel')
    ]

    operations = [
        migrations.CreateModel(
            name='ElementVariable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('sigla', models.CharField(max_length=10)),
                ('unit', models.CharField(max_length=10)),
                ('chartType', models.CharField(max_length=10)),
                ('chartColor', models.CharField(max_length=15)),
            ],
        ),
        migrations.RemoveField(
            model_name='elementsource',
            name='variables',
        ),
        migrations.AddField(
            model_name='elementsource',
            name='variables',
            field=models.ManyToManyField(to='vismet.ElementVariable'),
        ),
    ]
