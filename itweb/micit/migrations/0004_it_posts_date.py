# Generated by Django 2.2.1 on 2019-08-23 10:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micit', '0003_auto_20190823_0209'),
    ]

    operations = [
        migrations.AddField(
            model_name='it_posts',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
