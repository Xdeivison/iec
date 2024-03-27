# Generated by Django 3.1.2 on 2020-11-10 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vismet', '0009_elementcategory_display_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('display_name', models.CharField(max_length=100, verbose_name='nome de visualização')),
                ('desc', models.TextField(max_length=200, null=True, verbose_name='descrição adicional')),
                ('time_interval', models.CharField(max_length=100, verbose_name='intervalo de ano')),
                ('related_source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subsource', to='vismet.elementsource')),
            ],
        ),
    ]
