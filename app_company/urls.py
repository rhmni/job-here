from django.urls import path

from app_company import views


app_name = 'companies'
urlpatterns = [
    path('me/', views.RetrieveCompanyView.as_view(), name='retrieve'),
    path('me/update/', views.UpdateCompanyView.as_view(), name='update'),
    path('me/technologies/add/', views.TechnologyAddView.as_view(), name='add_technology'),
    path('me/technologies/delete/', views.TechnologyDeleteView.as_view(), name='delete_technology'),
]
