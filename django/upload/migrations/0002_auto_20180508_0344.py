# Generated by Django 2.0.4 on 2018-05-08 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imageset',
            old_name='location',
            new_name='ident',
        ),
    ]
