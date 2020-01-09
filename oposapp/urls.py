from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from django.contrib import admin

from . import views

urlpatterns = [
    #path('login', views.UserFormView.as_view()),
    #path('logout/', views.LogoutView.as_view(), name='logout'),
    path('', views.LoginView.as_view()),
    path('index', views.IndexView.as_view(),name='index'),
    path('cart', views.CartsView.as_view()),
    #path('login', views.LoginView.as_view()),
    path('orders', views.OrdersView.as_view()),
    path('metrics', views.MetricsView.as_view()),
    path('stocks', views.StocksView.as_view()), 
    path('supplies', views.SuppliesView.as_view()),
    path('pettycash', views.PettycashView.as_view()),
    path('suppliers', views.SuppliersView.as_view()),
    path('customers', views.CustomersView.as_view()),
    path('login', views.login_request,name='login'),
    path('order', views.Order,name='Order'),
     path('pin', views.Pin,name='Pin'),
     path('pincash', views.PinCash,name='PinCash'),
    path('clear', views.Clear,name='Clear'),
    path('flag', views.Flag,name='Flag'),
    path('orderdetails', views.OrderDetails,name='orderdetails'),
    path('sales', views.Sales,name='Sales'),
    path('sales_summary', views.Sales_summary,name='Sales_summary'),
    path('reports', views.reports,name='reports'),
    path('sales_summary_spoilt', views.Sales_summary_spoilt,name='Sales_summary_spoilt'),
    path('pdf_generator', views.write_pdf_view,name='write_pdf_view'),
    path('meals_summary', views.Meals_summary,name='meals_summary'),
]