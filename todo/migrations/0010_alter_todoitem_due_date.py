# Generated by Django 3.2.6 on 2021-08-16 10:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0009_auto_20210816_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 16, 10, 56, 11, 713768)),
        ),
    ]
