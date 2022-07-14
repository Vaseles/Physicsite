from pyexpat import model
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Tag(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
      return self.name

#! lection
class Article(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  title = models.CharField(max_length=250)
  tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
  text = RichTextField()

  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  class Meta:
      ordering = ['-updated', '-created']
  
  def __str__(self):
      return self.title
    
#! lab works
class Labwork(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  title = models.CharField(max_length=400)
  Mission = models.CharField(max_length=1000, blank=True)
  materials = models.TextField(blank=True)
  text = RichTextField()
  tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)

  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  class Meta:
      ordering = ['-updated', '-created']
  
  def __str__(self):
      return self.title

#!practise
class Practise(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  title = models.CharField(max_length=250)
  tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)

  name1 = RichTextField()
  answer1 = models.CharField(max_length=100)
  name2 = RichTextField(blank=True)
  answer2 = models.CharField(max_length=100, blank=True)
  name3 = RichTextField(blank=True)
  answer3 = models.CharField(max_length=100, blank=True)
  name4 = RichTextField(blank=True)
  answer4 = models.CharField(max_length=100, blank=True)
  name5 = RichTextField(blank=True)
  answer5 = models.CharField(max_length=100, blank=True)
  name6 = RichTextField(blank=True)
  answer6 = models.CharField(max_length=100, blank=True)
  name7 = RichTextField(blank=True)
  answer7 = models.CharField(max_length=100, blank=True)
  name8 = RichTextField(blank=True)
  answer8 = models.CharField(max_length=100, blank=True)
  name9 = RichTextField(blank=True)
  answer9 = models.CharField(max_length=100, blank=True)
  name10 = RichTextField(blank=True)
  answer10 = models.CharField(max_length=100, blank=True)

  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  class Meta:
      ordering = ['-updated', '-created']

  def __str__(self):
      return self.title
    
class Examen(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  title = models.CharField(max_length=200)
  text = RichTextField()

  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  class Meta:
      ordering = ['-updated', '-created']

  def __str__(self):
      return self.title
