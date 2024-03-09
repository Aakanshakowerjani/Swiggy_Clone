from django.contrib import admin
from django.urls import path,include
from swiggy import views

urlpatterns = [
    path('',views.home,name="home"),
    path('base',views.base,name="base"),
    path('about',views.base,name="about"),
    path('contact',views.base,name="contact"),
    path('services',views.base,name="services"),
    path('logout',views.user_logout,name="logout"),
]
