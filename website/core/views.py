from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView

from .forms import OrderForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def index(request):
    return render(request, 'core/index.html')


class BookView(CreateView):
    form_class = OrderForm
    template_name = 'core/includes/concact_us.html'
    success_url = '/thankyou/'

# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = "Пробное сообщение"
#             body = {
#                 'first_name': form.cleaned_data['first_name'],
#                 'phone_number': form.cleaned_data['phone_number'],
#                 'email': form.cleaned_data['email_address'],
#                 'message': form.cleaned_data['message'],
#             }
#             message = "\n".join(body.values())
#             try:
#                 send_mail(subject, message, 
#                           'admin@example.com',
#                           ['volochek93@yandex.ru'])
#             except BadHeaderError:
#                 return HttpResponse('Найден некорректный заголовок')
#             return redirect("core:index")

#     form = ContactForm()
#     return render(request, "core/includes/concact_us.html", {'form': form})