# Generated by Django 4.2.8 on 2023-12-10 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_alter_user_join_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='metadata',
            name='funds',
            field=models.FloatField(blank=True, null=True, verbose_name='Funds'),
        ),
    ]
