# Generated by Django 4.2.8 on 2023-12-07 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trxId', models.CharField(blank=True, max_length=20, null=True, verbose_name='Transaction Id')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='Phone')),
                ('dob', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('salary', models.FloatField(blank=True, null=True, verbose_name='Salary')),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=50, null=True, verbose_name='Gender')),
                ('join_date', models.DateField(blank=True, null=True, verbose_name='Joining Date')),
                ('status', models.BooleanField(default=True, verbose_name='Active Status')),
            ],
        ),
    ]