# Generated by Django 5.1.5 on 2025-02-19 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtimecommanding', '0004_remove_downlinkmessage_command_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uplinkmessage',
            name='command_id',
        ),
        migrations.AlterField(
            model_name='downlinkmessage',
            name='payload',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='downlinkmessage',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
