# Generated by Django 5.1.4 on 2025-05-16 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0006_displayprogramdata_use_emblems'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='use_team_1_profile_emblem',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='match',
            name='use_team_2_profile_emblem',
            field=models.BooleanField(default=False),
        ),
    ]
