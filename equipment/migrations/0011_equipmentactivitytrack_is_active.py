# Generated by Django 4.2.8 on 2023-12-11 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0010_remove_equipmentactivitytrack_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipmentactivitytrack',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is Active'),
        ),
    ]
