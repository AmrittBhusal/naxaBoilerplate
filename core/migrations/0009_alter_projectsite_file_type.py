# Generated by Django 4.1 on 2024-07-09 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_projectsite_file_type_projectsite_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectsite',
            name='file_type',
            field=models.CharField(blank=True, choices=[('shapefile', 'ShapeFile')], max_length=50, null=True),
        ),
    ]
