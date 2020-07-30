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

    #catch response
    path('catch/', views.catch, name='catch'),

    #call outer html page
    path('naver/', views.naver, name='naver'),


    # CRUD 
    path('create/', views.create, name='create'),

    path('new/', views.new, name='new'),

    path('<int:post_id>/', views.detail, name='detail'),

    path('post_list/', views.post_list, name='post_list'),


]