# Generated by Django 3.2.6 on 2021-08-16 10:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_auto_20210816_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 16, 10, 45, 54, 73821)),
        ),
        migrations.AddConstraint(
            model_name='todoitem',
            constraint=models.UniqueConstraint(fields=('title', 'todo_list'), name='name of constraint'),
        ),
    ]