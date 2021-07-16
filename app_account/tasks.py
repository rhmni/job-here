import redis
from celery import shared_task

from django.conf import settings
from django.core.mail import EmailMessage
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from app_account.models import User
from app_account.token import account_change_email_token, account_activation_token


@shared_task
def send_activate_user_email(domain, data):
    user, created = User.objects.get_or_create(
        name=data['name'],
        email=data['email'],
        password=data['password'],
    )
    user.is_company = data['is_company']
    user.is_active = False
    user.save()

    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = account_activation_token.make_token(user)

    email = EmailMessage(
        subject='activate account',
        body=f"https://{domain}{reverse('accounts:user_register_activate', args=[uid, token])}",
        to=[user.email],
    )
    email.send()


@shared_task
def send_change_password_email(user_id, domain, email):
    user = User.objects.get(pk=user_id)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = account_change_email_token.make_token(user)
    redis_con = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_CHANGE_EMAIL_DB)

    redis_con.set(str(user.pk), email)

    email = EmailMessage(
        subject='activate account',
        body=f"http://{domain}{reverse('accounts:change_password_verify', args=[uid, token])}",
        to=[email],
    )
    email.send()
