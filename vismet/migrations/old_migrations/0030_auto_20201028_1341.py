# Generated by Django 3.1.2 on 2020-10-28 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vismet', '0029_auto_20201028_1339'),
    ]

    operations = [
        migrations.RenameField(
            model_name='elementvariable',
            old_name='sigla',
            new_name='init',
        ),
    ]
