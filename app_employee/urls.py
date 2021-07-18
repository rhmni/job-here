from django.urls import path

from app_employee import views


app_name = 'employees'
urlpatterns = [
    path('me/', views.RetrieveEmployeeView.as_view(), name='retrieve'),
    path('me/update/', views.UpdateEmployeeView.as_view(), name='update'),
    path('me/technologies/add/', views.TechnologyAddView.as_view(), name='add_technology'),
    path('me/technologies/delete/', views.TechnologyDeleteView.as_view(), name='delete_technology'),
]
