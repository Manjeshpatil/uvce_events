# Generated by Django 4.0.5 on 2023-11-29 09:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0020_alter_event_start_date_alter_event_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateField(default=datetime.date(2023, 11, 29), null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(default=datetime.time(9, 4, 29, 169066), null=True),
        ),
    ]