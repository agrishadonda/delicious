# Generated by Django 5.0.1 on 2024-02-16 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goal', '0004_controls'),
    ]

    operations = [
        migrations.AddField(
            model_name='controls',
            name='titals',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
