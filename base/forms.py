from dataclasses import fields
from django.forms import ModelForm
from base.models import *

class ArticleForm(ModelForm):
  class Meta:
    model = Article
    fields = ['title', 'tag', 'text']

class LabworkForm(ModelForm):
  class Meta:
    model = Labwork
    fields = ['title', 'Mission', 'materials', 'text', 'tag']

class PractiseForm(ModelForm):
  class Meta:
    model = Practise
    fields = ['name1','answer1','name2','answer2','name3','answer3','name4','answer4','name5','answer5','name6','answer6','name7','answer7','name8','answer8','name9','answer9','name10','answer10','title', 'tag']

class ExamenForm(ModelForm):
  class Meta:
    model = Examen
    fields = ['title','text']