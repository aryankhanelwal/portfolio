# Generated by Django 4.0.5 on 2022-07-28 06:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfo', '0011_alter_post_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 28, 6, 13, 4, 599023, tzinfo=utc)),
        ),
    ]
