# Generated by Django 4.1 on 2024-07-24 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_remove_projectsite_files_upload_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='projectsite',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project', to='core.projectsite'),
        ),
        migrations.DeleteModel(
            name='Upload_file',
        ),
    ]
