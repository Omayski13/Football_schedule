# Generated by Django 5.1.4 on 2025-01-03 18:27

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0002_alter_week_friday_type_alter_week_monday_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisplayScheduleData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_emblem', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='club_emblem')),
                ('generation', models.CharField(blank=True, max_length=20, null=True)),
                ('coach', models.CharField(blank=True, max_length=50, null=True)),
                ('coach_photo', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='coach_photo')),
                ('month', models.CharField(blank=True, choices=[('January', 'Януари'), ('February', 'Февруари'), ('March', 'Март'), ('April', 'Април'), ('May', 'Май'), ('June', 'Юни'), ('July', 'Юли'), ('August', 'Август'), ('September', 'Септември'), ('October', 'Октомври'), ('November', 'Ноември'), ('December', 'Декември')], null=True)),
            ],
        ),
    ]
