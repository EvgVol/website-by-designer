from django.shortcuts import render

from .forms import OrderForm
from .email import send_contact_email_message


def home(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            send_contact_email_message(order)
            return render(
                request, 'core/index.html', {'form': OrderForm(), 'success': True}
            )
    else:
        form = OrderForm()

    return render(request, 'core/index.html', {'form': form})


def policy(request):
    return render(request, 'core/policy.html')
