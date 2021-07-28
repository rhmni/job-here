from django.contrib import admin
from django.urls import path, include, re_path

from Config.yasg import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('app_account.urls', namespace='accounts')),
    path('companies/', include('app_company.urls', namespace='companies')),
    path('employees/', include('app_employee.urls', namespace='employees')),
    path('options/', include('app_option.urls', namespace='options')),
    path('jobs/', include('app_job.urls', namespace='jobs')),

    # for doc
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
