# Generated by Django 3.0.2 on 2020-03-13 11:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0005_auto_20200313_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mytweetmodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 13, 11, 16, 56, 479305, tzinfo=utc)),
        ),
    ]
