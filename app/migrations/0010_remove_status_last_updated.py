# Generated by Django 3.1.3 on 2022-07-12 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20220712_1155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='last_updated',
        ),
    ]
