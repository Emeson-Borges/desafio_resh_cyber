from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register_view, name='register_view'),
    path('dashboard/', views.dashboard_view, name='dashboard_view'),
    path('change_email/', views.change_email_view, name='change_email'),
    path('change_password/', views.change_password_view, name='change_password'),
    path('delete_account/', views.delete_account_view, name='delete_account'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
