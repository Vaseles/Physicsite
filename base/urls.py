from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
  path('', views.index, name='index'),
  path('lections/', views.lections, name='lections'),
  path('lection/<str:pk>/', views.lection, name='lection'),

  path('create-lection/', views.createLection, name='create-lection'),

  path('labworks/', views.labworks, name = "labworks"),
  path('labworks/<str:pk>/', views.labwork, name='labwork'),

  path('create-labwork/', views.createLabwork, name='create-labwork'),

]