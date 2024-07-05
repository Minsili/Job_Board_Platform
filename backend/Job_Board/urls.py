from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.accounts.urls')),
    path('', include('apps.jobs.urls')),
    path('companies/', include('apps.companies.urls')),
    path('applications/', include('apps.applications.urls')),
]
