# Generated by Django 5.0.7 on 2024-07-13 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id_number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
    ]
