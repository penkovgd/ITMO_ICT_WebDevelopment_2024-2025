# Generated by Django 5.1.2 on 2024-10-30 17:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='creation_date',
        ),
        migrations.AddField(
            model_name='feedback',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
