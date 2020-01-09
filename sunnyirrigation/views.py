from django.shortcuts import render
from django.shortcuts import render,redirect
from django.views import generic
from django.http import HttpResponse
from sunnyirrigation.models import *

class LoginView(generic.ListView):
    template_name='sunnyirrigation/login.html'
    queryset = System_info.objects.all()

class IndexView(generic.ListView):
    template_name='sunnyirrigation/index.html'
    queryset = System_info.objects.all()  

class CustomersView(generic.ListView):
    template_name='sunnyirrigation/customers.html'
    queryset = System_info.objects.all() 

class StationsView(generic.ListView):
    template_name='sunnyirrigation/stations.html'
    queryset = System_info.objects.all() 