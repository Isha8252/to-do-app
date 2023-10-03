# Generated by Django 4.2 on 2023-06-11 20:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo_List_App', '0023_alter_task_createddate'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='dueTime',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
        migrations.AlterField(
            model_name='task',
            name='createdDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 11, 20, 3, 17, 211122, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='dueDate',
            field=models.DateField(),
        ),
    ]
