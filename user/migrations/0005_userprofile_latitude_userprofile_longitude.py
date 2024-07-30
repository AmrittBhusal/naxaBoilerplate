# Generated by Django 4.1 on 2024-07-08 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_userprofile_date_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
    ]