# Generated by Django 4.2.8 on 2023-12-10 03:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0005_member_nid_member_ref'),
        ('coach', '0004_coach_nid'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transaction', '0003_transaction_transactiontype_alter_transaction_reason'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trxId', models.CharField(blank=True, max_length=20, null=True, verbose_name='Transaction Id')),
                ('reason', models.CharField(blank=True, choices=[('salary_coach', 'Coach Salary'), ('salary_employee', 'Employee Salary')], max_length=50, null=True, verbose_name='Reason')),
                ('amount', models.FloatField(blank=True, null=True, verbose_name='Amount')),
                ('date', models.DateTimeField(blank=True, null=True, verbose_name='Date')),
                ('is_employee', models.BooleanField(default=True, verbose_name='Is Employee')),
                ('coach', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coach.coach')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Debit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trxId', models.CharField(blank=True, max_length=20, null=True, verbose_name='Transaction Id')),
                ('reason', models.CharField(blank=True, choices=[('package', 'Package'), ('private_session', 'Private Session')], max_length=50, null=True, verbose_name='Reason')),
                ('amount', models.FloatField(blank=True, null=True, verbose_name='Amount')),
                ('date', models.DateTimeField(blank=True, null=True, verbose_name='Date')),
                ('payed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.member')),
                ('received_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]