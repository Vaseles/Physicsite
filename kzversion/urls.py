from django.urls import path
from . import views

urlpatterns = [
     # главная страница
    path("kz", views.homekz, name = "homekz"),
    # страница с вопросами
    path("faqkz", views.faqkz, name =  "faqkz"),
    # страница с лекциями
    path("lectionkz", views.lection, name = "lectionkz"),
    # страница с экз материлом
    path("examenkz", views.examen, name = "examenkz" ),
    # страница с лабораторными работами
    path("labworkskz",views.laborator, name = "labworkskz"),
     # страница с заданиями
     path("practisekz", views.practise, name = "practisekz"),
     path("articlekz",views.article, name = "articlekz" ),
     path("labseekz", views.labsee, name = "labseekz"),
]