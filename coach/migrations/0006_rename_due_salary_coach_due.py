# Generated by Django 4.2.8 on 2023-12-10 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0005_coachactivitytrack'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coach',
            old_name='due_salary',
            new_name='due',
        ),
    ]
