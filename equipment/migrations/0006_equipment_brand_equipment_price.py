# Generated by Django 4.2.8 on 2023-12-10 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0005_equipmentactivitytrack_booked_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='brand',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Brand'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='price',
            field=models.FloatField(blank=True, null=True, verbose_name='Price'),
        ),
    ]
