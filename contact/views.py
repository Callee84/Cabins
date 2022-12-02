from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.views import View

from .forms import ContactForm


def contact_sent(request):
    return render(request, 'contact_sent.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            question = form.cleaned_data['question']
            recipient = [settings.EMAIL_HOST_USER]

            html = render_to_string('contactform.html',
                                    {
                                        'name': name,
                                        'email': email,
                                        'subject': subject,
                                        'question': question
                                    })

            send_mail(subject, question,
                      email, ['carl.g.holm@gmail.com'],
                      html_message=html)
            print('Email was sent')

            return redirect('sent')

    else:
        form = ContactForm()
    return render(request, 'contact.html', {
        'form': form})
