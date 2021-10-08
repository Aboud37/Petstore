# Generated by Django 3.2.2 on 2021-10-08 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0012_alter_response_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='response',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.response'),
        ),
    ]