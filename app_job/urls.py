from django.urls import path

from app_job import views

app_name = 'jobs'
urlpatterns = [
    path('', views.JobListView.as_view(), name='list'),
    path('company/', views.JobListForCompanyView.as_view(), name='company_list'),
    path('company/<int:job_id>/', views.JobRetrieveForCompanyView.as_view(), name='company_retrieve'),
    path('company/create/', views.JobCreateForCompanyView.as_view(), name='create'),
    path('company/update/<int:job_id>/', views.JobUpdateForCompanyView.as_view(), name='update'),
    path('company/delete/<int:job_id>/', views.JobDeleteForCompanyView.as_view(), name='delete'),
    path('<int:job_id>/', views.JobRetrieveView.as_view(), name='retrieve'),
]
