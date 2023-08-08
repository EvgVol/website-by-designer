from django.conf import settings
from aiogram import Bot, Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware


bot = Bot(token=settings.TELEGRAM_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


async def send_telegram_notification(order):

    message = (
        f"Новый заказ презентации\n"
        f"Имя: {order.first_name}\n"
        f"Телефон: {order.phone_number}\n"
        f"Сообщение: {order.content}\n"
        f"Email: {order.email}\n"
    )

    await bot.send_message(chat_id=settings.TELEGRAM_CHAT_ID, text=message)
