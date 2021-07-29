from django.urls import path

from app_job import views

app_name = 'jobs'
urlpatterns = [
    path('', views.JobListView.as_view(), name='list'),
    path('job/<int:job_id>/', views.JobRetrieveView.as_view(), name='retrieve'),
    path('job/create/', views.JobCreateView.as_view(), name='create'),
    path('job/update/<int:job_id>/', views.JobUpdateView.as_view(), name='update'),
]
