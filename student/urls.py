"""Mywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home, name="site"),
    path('home', views.index, name="home"),
    path('all',views.allstudent, name="all"),
    path('active',views.activestudent, name="active"),
    path('inactive',views.inactivestudent, name="inactive"),
    path('add/', views.addstudent, name='add'),
    path('search', views.search, name='search'),
    path('results', views.show, name='show'),
    path('update',views.update, name='update' ),
    path('department', views.assigndepartment , name="department"),
    path('create_order',views.createorder,name="create_order")


    
]