from django.urls import path
from app_account import views


app_name = 'accounts'
urlpatterns = [
    path('signup/', views.UserRegisterView.as_view(), name='user_register'),
    path('signup/activate/<uidb64>/<token>/', views.ActivateUserView.as_view(), name='user_register_activate'),
]
