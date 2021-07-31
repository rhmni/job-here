from django.urls import path

from app_job import views

app_name = 'jobs'
urlpatterns = [
    path('', views.JobListView.as_view(), name='list'),
    path('create/', views.JobCreateView.as_view(), name='create'),
    path('update/<int:job_id>/', views.JobUpdateView.as_view(), name='update'),
    path('delete/<int:job_id>/', views.JobDeleteView.as_view(), name='delete'),
    path('<int:job_id>/', views.JobRetrieveView.as_view(), name='retrieve'),
]
