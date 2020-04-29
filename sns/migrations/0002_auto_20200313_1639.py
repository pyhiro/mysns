# Generated by Django 3.0.2 on 2020-03-13 07:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sns', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewTweetModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.CharField(max_length=140)),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 3, 13, 7, 39, 32, 684549, tzinfo=utc))),
                ('good', models.IntegerField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='TweetModel',
        ),
    ]