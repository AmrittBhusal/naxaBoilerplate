# Generated by Django 4.1 on 2024-07-10 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_projectsite_file_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectsite',
            name='files',
            field=models.FileField(null=True, upload_to='shapefile/'),
        ),
    ]
