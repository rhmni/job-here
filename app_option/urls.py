from django.urls import path

from app_option import views

app_name = 'options'
urlpatterns = [
    path('technologies/', views.TechnologyListView.as_view(), name='list_technologies'),
]
