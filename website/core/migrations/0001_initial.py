# Generated by Django 4.2.1 on 2023-05-12 06:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='Имя')),
                ('phone_number', models.CharField(help_text='Укажите номер телефона для связи', max_length=11, validators=[django.core.validators.RegexValidator(message='Номер телефона должен начинаться с 8 и иметь 11 символов.', regex='^8\\d{10}$')], verbose_name='Номер телефона')),
                ('email', models.EmailField(help_text='Укажите Email-адрес для связи', max_length=150, verbose_name='Электронный адрес (email)')),
                ('message', models.TextField(verbose_name='Содержимое письма')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата заявки')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
                'ordering': ['-time_create'],
            },
        ),
    ]