from django.urls import path

from app_company import views


app_name = 'companies'
urlpatterns = [
    path('me/', views.RetrieveCompanyView.as_view(), name='retrieve_company'),
    path('me/update/', views.UpdateCompanyView.as_view(), name='update_company'),
]
