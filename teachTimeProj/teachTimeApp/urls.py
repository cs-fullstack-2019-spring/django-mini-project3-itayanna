from django.contrib import admin
from django.urls import path, include
from . import views


# defining  endpoints for routes

urlpatterns = [
    path('', views.index, name='index'),
    path('timeform/', views.newTimecard, name='timeform'),

]


