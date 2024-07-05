from django.urls import path
from . import views

urlpatterns = [
    path('applications/', views.application_list, name='application_list'),
    path('applications/<int:pk>/', views.application_detail, name='application_detail'),
    path('applications/<int:pk>/approve/', views.approve_application, name='approve_application'),
    path('applications/<int:pk>/reject/', views.reject_application, name='reject_application'),
]
