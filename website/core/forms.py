from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    """Форма заявки"""

    class Meta:
        model = Order
        fields = ('first_name', 'phone_number', 'email', 'content')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'first_name': 'Имя',
            'phone_number': 'Номер телефона',
            'email': 'Электронный адрес',
            'content': 'Содержимое письма'
        }
        help_texts = {
            'phone_number': 'Укажите номер телефона для связи',
            'email': 'Укажите email-адрес для связи',
            'content': 'Введите текст вашего сообщения'
        }
        error_messages = {
            'phone_number': {
                'required': 'Пожалуйста, укажите номер телефона',
            },
            'email': {
                'required': 'Пожалуйста, укажите электронный адрес',
            },
            'content': {
                'required': 'Пожалуйста, укажите текст вашего сообщения',
            }
        }
