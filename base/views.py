from django.shortcuts import redirect, render
from .models import *
from django.db.models import Q
from .forms import *

def index(request):
  articles = Article.objects.all()
  context = {'articles': articles}
  return render(request, 'base/index.html', context)

def lections(request):
  # articles = Article.objects.all()
  q = request.GET.get('q') if request.GET.get('q') != None else ''
  # articles = Article.objects.filter(tag__name__icontains = q)
  articles = Article.objects.filter(
      Q(tag__name__icontains=q) |
      Q(title__icontains=q)
  )

  tags = Tag.objects.all()

  context = {'articles': articles, 'tags': tags}
  return render(request, 'base/lections.html', context)

def lection(request,pk):
  article = Article.objects.get(id=pk)
  context = {'article': article}
  return render(request, 'base/lection.html', context)

def labworks(request):
  labworks = Labwork.objects.all()

  context = {'labworks': labworks}
  return render(request, 'base/labs.html', context)

def labwork(request,pk):
  labwork = Labwork.objects.get(id=pk)

  context = {'labwork': labwork}
  return render(request, 'base/labwork.html', context)


def createLection(request):
  form = ArticleForm()
  if request.method == 'POST':
    form = ArticleForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('base:index')

  context = {'form':form}
  return render(request, 'base/create-lection.html', context)

def createLabwork(request):
  form = LabworkForm()
  if request.method == 'POST':
    form = LabworkForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('base:index')

  context = {'form':form}
  return render(request, 'base/create-lection.html', context)