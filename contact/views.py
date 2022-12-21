from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
from .models import Contact
from smtplib import SMTPAuthenticationError


# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email_send = request.POST.get('email', '')
            content = request.POST.get('content', '')

            email = EmailMessage(
                subject='Name: New contact message',
                body=f'From {name} <{email_send}>\n\nWrote:\n\n{content}',
                from_email=email_send,
                to=['xxxxxx@xxxx.com'],
                reply_to=[email_send]
            )

        try:
            email.send()
            contact = Contact(name=name, email=email_send, content=content)
            contact.save()
            return redirect(reverse('contact') + '?ok')

        except SMTPAuthenticationError:
            return redirect(reverse('contact') + '?fail')

    return render(request, 'contact/contact.html', {'form': contact_form})
