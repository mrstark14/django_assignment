# Generated by Django 3.2.6 on 2021-08-12 08:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_todoitem_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 12, 8, 11, 57, 114143)),
        ),
    ]
