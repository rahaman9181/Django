# Generated by Django 2.2.1 on 2019-08-25 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('micit', '0007_it_posts_postby'),
    ]

    operations = [
        migrations.AlterField(
            model_name='it_posts',
            name='postby',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
