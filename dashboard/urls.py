from django.urls import path
from . import views

urlpatterns = [
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('', views.admin_dashboard, name='home'),  # This makes / point to the dashboard
]