from django.core.mail import EmailMessage

from celery import shared_task


@shared_task
def send_email(subject, message, email):
    email = EmailMessage(
        subject=subject,
        body=message,
        to=[email],
    )
    email.send()
