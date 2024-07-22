"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/

"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from cars.views import CarsListView,NewCarCreateView, CarsDetailView, CarUpdateView, CarDeleteView
from cars.forms import CarModelForm
from accounts.views import new_register, login_view, logout_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', CarsListView.as_view(), name='cars_list'),
    path('new_car/', NewCarCreateView.as_view(), name='new_car'),
    path('accounts/', new_register, name='accounts'),
    path('login/', login_view , name='login'),
    path('logout/', logout_view, name='logout'),
    path('car/<int:pk>/', CarsDetailView.as_view(), name ='car_detail'),
    path('car/<int:pk>/update/', CarUpdateView.as_view(),name ='car_update'),
    path('car/<int:pk>/delete/', CarDeleteView.as_view(),name ='car_delete'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


