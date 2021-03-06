from django.urls import path
from app_account import views

from rest_framework_simplejwt import views as jwt_views

app_name = 'accounts'
urlpatterns = [
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('profile/update/', views.UserProfileUpdateView.as_view(), name='update_profile'),

    path('auth/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('signup/', views.UserRegisterView.as_view(), name='user_register'),
    path('signup/activate/<uidb64>/<token>/', views.ActivateUserView.as_view(), name='user_register_activate'),

    path('change-email/', views.ChangeEmailView.as_view(), name='change_password'),
    path('change-email/verify/<uidb64>/<token>/', views.VerifyChangeEmailView.as_view(), name='change_password_verify'),
]
