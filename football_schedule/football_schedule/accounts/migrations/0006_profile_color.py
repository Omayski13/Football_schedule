# Generated by Django 5.1.4 on 2025-01-17 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_rename_generation_profile_team_generation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='color',
            field=models.CharField(choices=[('blue', 'син'), ('yellow', 'жълт'), ('red', 'червен'), ('green', 'зелен')], default='blue', max_length=20),
        ),
    ]
