from django import forms


class ContactForm(forms.Form):
    """Форма заявки."""

    first_name = forms.CharField(max_length=50)
    phone_number = forms.IntegerField(min_value=89000000000,
                                      max_value=89999999999)
    email = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea,
                              max_length=2000)
