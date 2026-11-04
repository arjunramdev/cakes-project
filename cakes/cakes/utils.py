from django.template.loader import render_to_string

from django.core.mail import EmailMultiAlternatives

from django.conf import settings

def send_mail(recipient,subject,template,context):
    mail=EmailMultiAlternatives(from_email=settings.EMAIL_HOST_USER,subject=subject,to=[recipient])
    context=render_to_string(template,context)

    mail.attach_alternative(context,mimetype='text/html')
    mail.send()