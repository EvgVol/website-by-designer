from django.conf import settings

from telegram import Bot, ParseMode


def send_telegram_notification(order):
    bot = Bot(token=settings.TELEGRAM_TOKEN)

    if order.email:
        email_text = f"Email: {order.email}\n"
    else:
        email_text = ""

    message = (
        f"Новый заказ презентации\n"
        f"Имя: {order.first_name}\n"
        f"Телефон: {order.phone_number}\n"
        f"Сообщение: {order.content}\n" +
        email_text
    )

    bot.send_message(chat_id=settings.TELEGRAM_CHAT_ID,
                     text=message,
                     parse_mode=ParseMode.HTML)
