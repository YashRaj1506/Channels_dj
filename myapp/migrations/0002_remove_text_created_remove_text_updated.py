# Generated by Django 5.0.6 on 2024-07-01 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='text',
            name='created',
        ),
        migrations.RemoveField(
            model_name='text',
            name='updated',
        ),
    ]
