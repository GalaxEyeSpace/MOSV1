# Generated by Django 5.1.5 on 2025-02-21 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedulemanager', '0006_alter_schedule_execution_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduleset',
            name='schedule_set_id',
        ),
    ]
