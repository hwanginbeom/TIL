from django.contrib import admin
from django.urls import path
from greetingApp import views

urlpatterns = [
    path('index/', views.greeting),
    path('hi/', views.hi)
]