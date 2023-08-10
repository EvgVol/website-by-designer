from django.core.validators import RegexValidator
from django.db import models


class Order(models.Model):

    first_name = models.CharField('Имя', max_length=150, blank=False)
    phone_number = models.CharField(
        'Номер телефона', validators=[
            RegexValidator(
                regex=r'^(\+7|8)[0-9]{10}$',
                message='Номер телефона должен быть в формате '
                        '8XXXXXXXXXX или +7XXXXXXXXXX.'
            )
        ],
        blank=False,
        help_text='Укажите номер телефона для связи', max_length=12
    )
    email = models.EmailField(
        'Электронный адрес (email)', max_length=150,
        help_text='Укажите Email-адрес для связи'
    )
    content = models.TextField(
        'Содержимое письма', blank=False,
    )
    time_create = models.DateTimeField('Дата заявки', auto_now_add=True)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-time_create']

    def __str__(self):
        return (
            f'Заявка oт {self.email}({self.first_name}: {self.phone_number})'
        )
