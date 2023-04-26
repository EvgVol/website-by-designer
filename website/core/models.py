from django.db import models

class Order(models.Model):
    """Модель заказа."""

    first_name = models.CharField(max_length=50)
    phone_number = models.IntegerField(min_value=89000000000,
                                      max_value=89999999999)
    email = models.EmailField(max_length=150)
    message = models.TextField()
