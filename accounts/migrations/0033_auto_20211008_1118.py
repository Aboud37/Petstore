# Generated by Django 3.2.2 on 2021-10-08 09:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0032_auto_20211008_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 8, 11, 18, 28, 199425), null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_login',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 8, 11, 18, 28, 199425), null=True),
        ),
    ]
