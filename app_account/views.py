from datetime import datetime

from django.urls import reverse
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from app_account.models import User
from app_account.serializers import UserRegisterSerializer
from app_account.token import account_activation_token
from app_company.models import Company
from app_employee.models import Employee
from permissions import IsAnonymoused

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage


class UserRegisterView(GenericAPIView):
    """
        get user data and send email for activate user account
    """

    serializer_class = UserRegisterSerializer

    permission_classes = (
        IsAnonymoused,
    )

    def post(self, request):
        srz_data = self.serializer_class(data=request.data)
        if srz_data.is_valid(raise_exception=True):
            data = srz_data.validated_data

            user, created = User.objects.get_or_create(
                name=data['name'],
                email=data['email'],
                password=data['password'],
            )
            user.is_employer = data['is_employer']
            user.is_active = False
            user.save()

            domain = get_current_site(request)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = account_activation_token.make_token(user)
            email = EmailMessage(
                subject='activate account',
                body=f"http://{domain}{reverse('accounts:user_register_activate', args=[uid, token])}",
                to=[user.email]
            )
            email.send()
            return Response(data={'message': 'Please confirm your email address'})


class ActivateUserView(GenericAPIView):
    """
        get link and activate user
    """

    permission_classes = (
        IsAnonymoused,
    )

    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.join_date = datetime.now()
            user.save()
            if user.is_employer:
                Company.objects.create(user=user)
            else:
                Employee.objects.create(user=user)
            return Response(data={'message': 'your account now is active'})
        else:
            return Response(data={'message': 'this link is expired'})
