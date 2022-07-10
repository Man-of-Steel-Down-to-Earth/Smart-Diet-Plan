# Generated by Django 3.1 on 2020-11-15 18:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20201115_2043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='text',
            new_name='task',
        ),
        migrations.AlterField(
            model_name='assignment',
            name='date_and_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 15, 18, 25, 19, 91417, tzinfo=utc)),
        ),
    ]