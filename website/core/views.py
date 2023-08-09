from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt
from channels.db import database_sync_to_async

import asyncio

from .forms import OrderForm
from .email import send_contact_email_message
from .telegram import send_telegram_notification


@database_sync_to_async
def save_form_async(form):
    return form.save()


async def async_csrf_exempt(view_func):
    def wrapped_view(*args, **kwargs):
        return asyncio.ensure_future(view_func(*args, **kwargs))
    wrapped_view = csrf_exempt(wrapped_view)
    return wrapped_view


@async_csrf_exempt
async def main(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = await save_form_async(form)
            tasks = [
                send_contact_email_message(order),
                send_telegram_notification(order),
            ]
            await asyncio.gather(*tasks)

            return render(
                request, 'core/index.html', {'form': OrderForm(),
                                             'success': True}
            )
    else:
        form = OrderForm()

    return TemplateResponse(request, 'core/index.html', {'form': form})


def policy(request):
    return render(request, 'core/policy.html')
