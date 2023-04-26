from django import forms

from .models import Order


class OrderForm(forms.Form):
    """Форма заявки."""

    class Meta:
        model = Order
        fields = '__all__'
