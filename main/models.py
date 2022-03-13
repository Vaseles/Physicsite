from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.template.defaultfilters import slugify

#category
class Category(MPTTModel):
    title = models.CharField("title",max_length=200)
    slug = models.SlugField("slug", max_length=300)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.title

    class MPTTMeta:
       order_insertion_by = ["title"]


#tag
class Tag(models.Model):
    title = models.CharField("title",max_length=200)
    slug = models.SlugField("slug", max_length=300)

    def __str__(self):
        return self.title

# Create your models here.
class task(models.Model):
    title = models.CharField("title", max_length=200,default=' ')
    data = models.DateField(auto_now=True)
    teg = models.CharField("teg", max_length=100, default=' ')
    category = models.ForeignKey(Category, related_name="task", on_delete= models.SET_NULL, null = True)
    tags = models.ManyToManyField(Tag, related_name = "task")

    title1 = models.CharField( "Title1" , max_length=500, default=' ')
    task1 = models.TextField("Task1", default=' ')
    answe1 = models.CharField( "Answer1",max_length=300, default=' ')

    title2 = models.CharField( "Title2" ,max_length=500, blank = True, default=' ')
    task2 = models.TextField("Task2", blank = True, default=' ')
    answe2 = models.CharField( "Answer2",max_length=300, blank = True, default=' ' )

    title3 = models.CharField( "Title3" ,max_length=500,blank = True, default=' ')
    task1 = models.TextField("Task3", blank = True, default=' ')
    answe1 = models.CharField( "Answer3",max_length=300, blank = True, default=' ')

    title4 = models.CharField( "Title4" ,max_length=500, blank = True,default=' ')
    task4 = models.TextField("Task4", blank = True, default=' ')
    answe4 = models.CharField( "Answer4",max_length=300, blank = True, default=' ')

    title5 = models.CharField( "Title5" ,max_length=500, blank = True , default=' ')
    task5 = models.TextField("Task5", blank = True , default=' ')
    answe5 = models.CharField( "Answer5",max_length=300, blank = True, default=' ')

    title6 = models.CharField( "Title6" ,max_length=500, blank = True, default=' ')
    task6 = models.TextField("Task6", blank = True, default=' ')
    answe6 = models.CharField( "Answer6",max_length=300, blank = True, default=' ')



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

from django.urls import reverse #Used to generate URLs by reversing the URL patterns
class lection(models.Model):
    title = models.CharField("title", max_length=200)
    description = models.CharField ("description", max_length = 400)
    data = models.DateField(auto_now=True)
    text = models.TextField("Your article")
    category = models.ForeignKey(Category, related_name="lection", on_delete= models.SET_NULL, null = True)
    tags = models.ManyToManyField(Tag, related_name = "lection")
 

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def get_absolute_url(self):
        return reverse('lection: article', args=[str(self.id)])



class laborator(models.Model):
    title = models.CharField("title", max_length=200)
    description = models.CharField ("description", max_length = 300)
    materials = models.CharField("matrials", max_length=500, blank = True)
    data = models.DateField(auto_now=True)
    text = models.TextField("Your article")
    category = models.ForeignKey(Category, related_name="laborator", on_delete= models.SET_NULL, null = True)
    tags = models.ManyToManyField(Tag, related_name = "laborator")
 

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Лабораторная работа"
        verbose_name_plural = "Лабораторные работы"

    def get_absolute_url(self):
        return reverse('labwork-detail', args=[str(self.id)])

class examen(models.Model):
    title = models.CharField("title", max_length=200)
    description = models.CharField ("description", max_length = 300)
    data = models.DateField(auto_now=True)
    text = models.TextField("Some_text")
    tags = models.ManyToManyField(Tag, related_name = "examen")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Экзаменационная работа"
        verbose_name_plural = "Экзаменнационные работы"

    def get_absolute_url(self):
        return reverse('exam-detail', args=[str(self.id)])

