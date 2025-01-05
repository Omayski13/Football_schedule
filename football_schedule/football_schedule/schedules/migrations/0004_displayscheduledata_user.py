# Generated by Django 5.1.4 on 2025-01-03 18:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0003_displayscheduledata'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='displayscheduledata',
            name='user',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='display_schedule', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]