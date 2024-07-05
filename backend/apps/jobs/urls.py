from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/', views.job_list, name='job_list'),
    path('<int:pk>/', views.job_detail, name='job_detail'),
    path('job/new/', views.job_create, name='job_create'),
    path('apply/<int:job_id>/', views.job_apply, name='apply_job'),
     path('job_search/', views.job_search, name='job_search'), 
]
