# Generated by Django 4.2 on 2023-06-11 17:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo_List_App', '0020_alter_task_createddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='createdDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 11, 17, 8, 12, 876463, tzinfo=datetime.timezone.utc)),
        ),
    ]
