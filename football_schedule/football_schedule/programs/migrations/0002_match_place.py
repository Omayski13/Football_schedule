# Generated by Django 5.1.4 on 2025-03-20 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='place',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
