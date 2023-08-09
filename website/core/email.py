from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


def send_contact_email_message(order):
    """Фунция отправки сообщения на электронную почту."""
    email = order.email if order.email else None
    message = render_to_string('core/includes/order_email_send.html', {
        'first_name': order.first_name,
        'phone_number': order.phone_number,
        'content': order.content,
        'email': email,
    })
    email = EmailMessage(
        'Новый заказ презентации',
        message,
        settings.EMAIL_SERVER,
        [settings.EMAIL_ADMIN]
    )
    email.send(fail_silently=False)