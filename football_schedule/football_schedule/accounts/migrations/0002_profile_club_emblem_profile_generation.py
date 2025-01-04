# Generated by Django 5.1.4 on 2025-01-03 16:49

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='club_emblem',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='profile',
            name='generation',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
