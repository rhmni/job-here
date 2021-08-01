from django.urls import path

from app_apply import views

app_name = 'applys'
urlpatterns = [
    path('apply/<int:job_id>/', views.ApplyJobView.as_view(), name='apply_for_job'),
    path('employee/', views.ApplyListForEmployeeView.as_view(), name='list_applys_for_employee'),
    path('employee/<int:apply_id>/', views.ApplyRetrieveForEmployeeView.as_view(), name='retrieve_apply_for_employee'),
    path('company/<int:apply_id>/', views.ApplyRetrieveForCompanyView.as_view(), name='retrieve_apply_of_job_for_company'),
    path('company/list/<int:job_id>/', views.ApplyListForCompanyView.as_view(), name='list_applys_of_job_for_company'),
]
