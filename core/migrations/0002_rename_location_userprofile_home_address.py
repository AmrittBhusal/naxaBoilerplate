# Generated by Django 4.1 on 2024-07-08 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='location',
            new_name='home_address',
        ),
    ]
