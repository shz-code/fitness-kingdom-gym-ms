# Generated by Django 4.2.8 on 2023-12-10 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0007_coach_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True, verbose_name='Phone'),
        ),
    ]
