# Generated by Django 2.0.4 on 2018-06-07 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0005_alignment_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='alignment',
            name='points1',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alignment',
            name='points2',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
