# Generated by Django 5.0.3 on 2024-04-21 08:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_housepricefactor_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housepricefactor',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 21, 8, 1, 25, 117128, tzinfo=datetime.timezone.utc)),
        ),
    ]
