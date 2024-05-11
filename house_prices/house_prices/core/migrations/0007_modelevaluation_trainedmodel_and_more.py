# Generated by Django 5.0.3 on 2024-04-21 08:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_housepricefactor_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelEvaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=100)),
                ('metric_name', models.CharField(max_length=50)),
                ('train_score', models.FloatField()),
                ('test_score', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'model_evaluation',
            },
        ),
        migrations.CreateModel(
            name='TrainedModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('model_type', models.CharField(max_length=50)),
                ('serialized_model', models.BinaryField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'trained_model',
            },
        ),
        migrations.AlterField(
            model_name='housepricefactor',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 21, 8, 4, 17, 135346, tzinfo=datetime.timezone.utc)),
        ),
    ]