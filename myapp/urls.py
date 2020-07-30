from django.urls import path, include
from . import views

urlpatterns = [
    #main screen = index_list
    path('', views.index_list, name='index_list'),

    #dinner menu 
    path('dinner/', views.dinner, name='dinner'),

    #variable routing
    path('hello/<str:name>/', views.hello, name='hello'),

    #throw request
    path('throw/', views.throw, name='throw'),

    path('catch/', views.catch, name='catch'),


]