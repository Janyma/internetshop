from django.urls import path
from . import views
from .views import Register

urlpatterns=[
    path("", views.home, name='blog-home'),
    path('about/', views.about, name='about-club'),
    path("register/", Register.as_view(), name="register"),
    #path("login/", Login.as_view(), name="login"),
    #path('login/', view="login"),
]