from django.conf import settings
from django.template.loader import render_to_string
import aiosmtplib
from email.message import EmailMessage


async def send_contact_email_message(order):
    """Функция отправки сообщения на электронную почту."""
    client_email = order.email if order.email else None
    message = render_to_string('core/includes/order_email_send.html', {
        'first_name': order.first_name,
        'phone_number': order.phone_number,
        'content': order.content,
        'email': client_email,
    })

    email = EmailMessage()
    email.set_content(message, "html")
    email["Subject"] = "Новый заказ презентации"
    email["From"] = settings.EMAIL_SERVER
    email["To"] = [settings.EMAIL_ADMIN]

    async with aiosmtplib.SMTP(settings.EMAIL_HOST,
                               settings.EMAIL_PORT) as server:
        await server.login(settings.EMAIL_HOST_USER,
                           settings.EMAIL_HOST_PASSWORD)
        await server.send_message(email)