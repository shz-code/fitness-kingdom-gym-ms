# Generated by Django 4.2.8 on 2023-12-10 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_remove_user_due_payment_user_due'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='emp_id',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Employee Id'),
        ),
    ]