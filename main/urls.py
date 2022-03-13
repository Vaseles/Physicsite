from django.urls import path

from main.models import lection
from . import views

urlpatterns = [
    # главная страница
    path("", views.index, name = 'home'),
    # страница с заданиями
    path("practise", views.practise, name = "practise"),
    # страница с лекциями
    path("staties", views.staties, name = "lection"),
    # страница с лабораторными работами
    path("labworks",views.labworks, name = "labworks"),
     # страница с экз материлом
    path("exem",views.exem, name = "exem"),
     # страница с вопросами
    path("faq",views.faq, name = "faq"),
    path("<id>/", views.lection_url, name = "lect"),
]
