from django.urls import path

from app_apply import views

app_name = 'applys'
urlpatterns = [
    path('apply/<int:job_id>/', views.ApplyForJobView.as_view(), name='apply_for_job'),
]
