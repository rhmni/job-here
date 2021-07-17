from datetime import datetime

from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
import redis

from app_account.models import User
from app_account.serializers import UserRegisterSerializer, UserChangeEmailSerializer
from app_account.tasks import send_activate_user_email, send_change_password_email
from app_account.token import account_activation_token, account_change_email_token
from app_company.models import Company
from app_employee.models import Employee
from permissions import IsAnonymoused




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
            send_activate_user_email.delay(get_current_site(request).domain, srz_data.validated_data)

            return Response(data={'message': 'email send, please confirm your email address'})


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
            if user.is_company:
                Company.objects.create(user=user)
            else:
                Employee.objects.create(user=user)
            return Response(data={'message': 'your account now is active'})
        else:
            return Response(data={'message': 'this link is expired'})


class ChangeEmailView(GenericAPIView):
    """
        get user data and send email for change email of user
    """

    serializer_class = UserChangeEmailSerializer

    permission_classes = (
        IsAuthenticated,
    )

    def post(self, request):
        srz_data = self.serializer_class(data=request.data)
        if srz_data.is_valid(raise_exception=True):
            data = srz_data.validated_data
            if request.user.check_password(data['password']):
                domain = get_current_site(request).domain
                user_id = request.user.pk
                send_change_password_email.apply_async(args=[user_id, domain, data['new_email']])
                return Response({'message': 'email send please verify it'})
            return Response({'message': 'password is not correct.'})


class VerifyChangeEmailView(GenericAPIView):
    """
        get link and change email of user
    """

    permission_classes = (
        AllowAny,
    )

    def get(self, request, uidb64, token):

        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_change_email_token.check_token(user, token):
            redis_con = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_CHANGE_EMAIL_DB)
            if redis_con.exists(user.pk):
                email = redis_con.get(user.pk).decode('utf-8')
                if not User.objects.filter(email=email).exists():
                    user.email = email
                    user.save()
                    redis_con.expire(user.pk, 1)
                    return Response(data={'message': 'your email changed'})
                else:
                    return Response(data={'message': 'user with this email already exists'})
        return Response(data={'message': 'this link is expired'})
