# Generated by Django 5.0.3 on 2024-04-20 07:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_housepricefactor_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housepricefactor',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 20, 7, 4, 48, 345259, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='housepricefactor',
            name='garagefinish',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]