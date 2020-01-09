from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from django.contrib import admin

from . import views

urlpatterns = [
  
    path('', views.LoginView.as_view()),
    path('index', views.IndexView.as_view(),name='index'),
    path('customers', views.CustomersView.as_view(),name='customers'),
    path('stations', views.StationsView.as_view(),name='stations'),

]