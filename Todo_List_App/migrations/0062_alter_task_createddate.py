# Generated by Django 4.2 on 2023-09-09 05:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo_List_App', '0061_alter_task_createddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='createdDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 9, 5, 11, 3, 802023, tzinfo=datetime.timezone.utc)),
        ),
    ]
