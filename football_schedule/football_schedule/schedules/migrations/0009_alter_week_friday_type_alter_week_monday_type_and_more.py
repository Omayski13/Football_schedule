# Generated by Django 5.1.4 on 2025-03-20 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0008_displayscheduledata_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='week',
            name='friday_type',
            field=models.CharField(blank=True, choices=[('Тренировка', 'Тренировка'), ('Мач', 'Мач')], null=True),
        ),
        migrations.AlterField(
            model_name='week',
            name='monday_type',
            field=models.CharField(blank=True, choices=[('Тренировка', 'Тренировка'), ('Мач', 'Мач')], null=True),
        ),
        migrations.AlterField(
            model_name='week',
            name='saturday_type',
            field=models.CharField(blank=True, choices=[('Тренировка', 'Тренировка'), ('Мач', 'Мач')], null=True),
        ),
        migrations.AlterField(
            model_name='week',
            name='sunday_type',
            field=models.CharField(blank=True, choices=[('Тренировка', 'Тренировка'), ('Мач', 'Мач')], null=True),
        ),
        migrations.AlterField(
            model_name='week',
            name='thursday_type',
            field=models.CharField(blank=True, choices=[('Тренировка', 'Тренировка'), ('Мач', 'Мач')], null=True),
        ),
        migrations.AlterField(
            model_name='week',
            name='tuesday_type',
            field=models.CharField(blank=True, choices=[('Тренировка', 'Тренировка'), ('Мач', 'Мач')], null=True),
        ),
        migrations.AlterField(
            model_name='week',
            name='wednesday_type',
            field=models.CharField(blank=True, choices=[('Тренировка', 'Тренировка'), ('Мач', 'Мач')], null=True),
        ),
    ]
