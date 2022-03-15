from msilib.schema import ListView
from django.shortcuts import get_object_or_404, render
from .models import *
from .models import Category

def index(request):
    tasks = task.objects.all()
    return render( request, "main/index.html", {"title": "Дом", "task": tasks, " kz ": "kzversion/index.html" } )

def staties(request):
    lections = lection.objects.all()
    return render(request,"main/lection.html", {"title": "Лекции", "lection": lections , "lectionkz": "kzversion/lection.html", "seelection": "article.html"})

def article(request):
    lections = lection.objects.all()
    return render(request,"main/article.html", {"title": "Статья", "lection": lections })

def practise(request):
    tasks = task.objects.all()
    return render( request, "main/practise.html", {"title": "Практические работы. Каталог", "task": tasks, "practisekz": "kzversion/practise.html"} )

def labworks(request):
    laborators = laborator.objects.all()
    return render( request, "main/labworks.html",  {"title": "Лабораторные работы", "laborators": laborators, "labworkskz": "kzversion/labwork.html"} )

def labsee(request):
    laborators = laborator.objects.all()
    return render( request, "main/labsee.html",  {"title": "Лабораторная работа", "laborators": laborators })

def exem(request):
    examens = examen.objects.all()
    return render( request, "main/exem.html", {"title": "Экзамены", "examen": examens,"examenkz": "kzversion/exem.html" })

def faq(request):
    return render( request, "main/faq.html",{"faqkz": "kzversion/faq.html" })


# def text(request):