# Generated by Django 2.0.7 on 2018-08-29 13:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_auto_20180829_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 29, 13, 26, 53, 656720, tzinfo=utc)),
        ),
    ]
