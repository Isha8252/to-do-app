# Generated by Django 4.2 on 2023-06-08 06:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo_List_App', '0008_alter_task_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='dueDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 9, 6, 8, 25, 668720, tzinfo=datetime.timezone.utc)),
        ),
    ]
