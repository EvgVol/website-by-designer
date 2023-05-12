from django.core.exceptions import ValidationError


def validate_not_empty(value):
    """Валидация поля формы."""
    if value == '':
        raise ValidationError(
            'Поле не может быть пустым!',
            params={'value': value},
        )
