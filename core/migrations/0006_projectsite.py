# Generated by Django 4.1 on 2024-07-09 05:31

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_deparment_user_userprofile_document_user_userprofile_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proj_site_cordinates', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('area', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('way_from_home', django.contrib.gis.db.models.fields.LineStringField(srid=4326)),
            ],
        ),
    ]
