# Generated by Django 4.2.8 on 2023-12-08 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0002_remove_equipment_equipmenttype_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='url',
            field=models.TextField(blank=True, null=True, verbose_name='Url'),
        ),
    ]