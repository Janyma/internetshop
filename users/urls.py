from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from main import views
from django.views.generic.base import TemplateView
from users.views import register
from users.views import profile

urlpatterns = [
 
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('profile/', profile, name='profile')

]