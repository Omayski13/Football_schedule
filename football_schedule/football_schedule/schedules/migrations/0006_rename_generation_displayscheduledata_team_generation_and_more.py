# Generated by Django 5.1.4 on 2025-01-08 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0005_alter_displayscheduledata_month'),
    ]

    operations = [
        migrations.RenameField(
            model_name='displayscheduledata',
            old_name='generation',
            new_name='team_generation',
        ),
        migrations.AddField(
            model_name='displayscheduledata',
            name='team_generation_choice',
            field=models.CharField(choices=[('Отбор', 'Отбор'), ('Набор', 'Набор'), ('Без да посочваш', 'Без да посочваш')], default=2008, max_length=20),
            preserve_default=False,
        ),
    ]
