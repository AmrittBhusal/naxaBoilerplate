# Generated by Django 4.1 on 2024-07-08 05:58

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_userprofile_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='home_address',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4236),
        ),
    ]