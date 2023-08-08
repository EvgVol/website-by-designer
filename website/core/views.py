from django.shortcuts import render
from django.template.response import TemplateResponse
from channels.db import database_sync_to_async
from django.views.decorators.csrf import csrf_protect

import asyncio

from .forms import OrderForm
from .email import send_contact_email_message
from .telegram import send_telegram_notification


@database_sync_to_async
def save_form_async(form):
    return form.save()


@csrf_protect
async def home(request):
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
