from django.urls import path

from app_job import views

app_name = 'jobs'
urlpatterns = [
    path('', views.JobListView.as_view(), name='list'),
    path('job/<int:job_id>/', views.JobRetrieveView.as_view(), name='retrieve'),
]
