from django.urls import path
from .views import company_list, company_detail

urlpatterns = [
    path('', company_list, name='company_list'),
    path('<int:pk>/', company_detail, name='company_detail'),
]
