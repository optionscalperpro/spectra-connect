from .views import login_view

urlpatterns = [
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('', views.admin_dashboard, name='home'),
    path('login/', login_view, name='login'),  # ← Add this line
]