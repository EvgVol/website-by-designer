# Generated by Django 4.2.1 on 2023-08-09 06:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_message_order_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(help_text='Укажите номер телефона для связи', max_length=11, validators=[django.core.validators.RegexValidator(message='Номер телефона в формате `89876543210`', regex='^8\\d{10}$')], verbose_name='Номер телефона'),
        ),
    ]
