# Generated by Django 4.2.8 on 2023-12-10 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0007_alter_equipmentactivitytrack_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='serial',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Serial'),
        ),
    ]