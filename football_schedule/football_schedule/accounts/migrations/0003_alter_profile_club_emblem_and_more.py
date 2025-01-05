# Generated by Django 5.1.4 on 2025-01-03 16:50

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_club_emblem_profile_generation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='club_emblem',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='club_emblem'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='profile_picture'),
        ),
    ]