# Generated by Django 3.2.2 on 2021-08-04 21:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20210804_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 4, 23, 13, 37, 583044), null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_login',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 4, 23, 13, 37, 583044), null=True),
        ),
    ]
