# Generated by Django 4.2 on 2023-06-08 15:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo_List_App', '0013_task_completed_alter_task_duedate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='taskDesc',
        ),
        migrations.AlterField(
            model_name='task',
            name='dueDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 9, 15, 45, 14, 796873, tzinfo=datetime.timezone.utc)),
        ),
    ]
