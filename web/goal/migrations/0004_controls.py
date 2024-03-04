# Generated by Django 5.0.1 on 2024-02-16 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goal', '0003_banners'),
    ]

    operations = [
        migrations.CreateModel(
            name='controls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images/')),
                ('date', models.DateField()),
                ('para', models.CharField(max_length=300)),
            ],
        ),
    ]
