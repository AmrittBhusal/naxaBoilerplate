# Generated by Django 4.1 on 2024-07-09 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_projectsite'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectsite',
            name='files',
            field=models.FileField(null=True, upload_to='projectfile/'),
        ),
    ]
