from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='users'

urlpatterns = [
    path('register/',auth_views.LoginView.as_view(template_name='users/login.html'),name='register'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout')
    
]
