# Generated by Django 2.0.4 on 2018-06-07 19:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0006_auto_20180607_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='alignment',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 7, 19, 16, 30, 466796, tzinfo=utc)),
            preserve_default=False,
        ),
    ]