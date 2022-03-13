from django.shortcuts import render
from .models import *
from .models import Collection


def homekz(request):
    return render( request, "kzversion/index.html", {"title": "Yйkz", "/": "main/index.html" })

def faqkz(request):
    return render( request, "kzversion/faq.html", {"faq": "main/faq.html"})

def lection(request):
    lections = lect.objects.all()
    return render(request,"kzversion/lection.html", {"title": "Дәрістер","staties": "main/lection.html", "lection": lections })

def examen(request):
    examena = exam.objects.all()
    return render( request, "kzversion/exem.html", {"title": "Емтихандар", "examens": examena, "exem": "main/exem.html"})

def laborator(request):
    laborators = labwork.objects.all()
    return render( request, "kzversion/labworks.html",  {"title": "Зертханалық жұмыс", "laborator": laborators, "labworks": "main/labworks.html" } )

def practise(request):
    tasks = exemples.objects.all()
    return render( request, "kzversion/practise.html", {"title": "Практикалық жұмыстар","rupractise": "main/practise.html", "task": tasks, "practise": "main/practise.html"} )