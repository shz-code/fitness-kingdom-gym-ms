# Generated by Django 4.2.8 on 2023-12-12 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='attendance',
            field=models.BooleanField(default=False, verbose_name='Attendance'),
        ),
    ]