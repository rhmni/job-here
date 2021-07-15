from django.urls import path

from app_employee import views


app_name = 'employees'
urlpatterns = [
    path('me/', views.RetrieveEmployeeView.as_view(), name='retrieve_employee'),
    path('me/update/', views.UpdateEmployeeView.as_view(), name='update_employee'),
]
