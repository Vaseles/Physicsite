from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse

# категории
class Collection(MPTTModel):
    name = models.CharField("name", max_length=200,default="")
    slug = models.SlugField("slug", max_length=300)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='child')

    def __str__(self):
        return self.name
    
    class MPTTMeta:
        order_insertion_by = ["name"]

# теги для лекций, заданий и т.д.
class Teg(models.Model):
    name = models.CharField("name",max_length=200)
    slug = models.SlugField("slug", max_length=300)

    def __str__(self):
        return self.name

# лекции
class lect(models.Model):
    name = models.CharField("name", max_length=200,default="")
    description = models.CharField ("description", max_length = 400)
    data = models.DateField(auto_now=True)
    text = models.TextField("Your article")
    category = models.ForeignKey(Collection, related_name="lect", on_delete= models.SET_NULL, null = True)
    tags = models.ManyToManyField(Teg, related_name = "lect")
 

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Дәріс"
        verbose_name_plural = "Дәрістер"

    def get_absolute_url(self):
        return reverse('lect', args=[str(self.id)])

# задачи
class exemples(models.Model):
    name = models.CharField("name", max_length=200,default=' ')
    data = models.DateField(auto_now=True)
    teg = models.CharField("teg", max_length=100, default=' ')
    category = models.ForeignKey(Collection, related_name="task", on_delete= models.SET_NULL, null = True)
    tags = models.ManyToManyField(Teg, related_name = "exemples")

    title1 = models.CharField( "Title1" , max_length=500, default=' ')
    task1 = models.TextField("Task1", default=' ')
    answe1 = models.CharField( "Answer1",max_length=300, default=' ')

    title2 = models.CharField( "Title2" ,max_length=500, blank = True, default=' ')
    task2 = models.TextField("Task2", blank = True, default=' ')
    answe2 = models.CharField( "Answer2",max_length=300, blank = True, default=' ' )

    title3 = models.CharField( "Title3" ,max_length=500,blank = True, default=' ')
    task1 = models.TextField("Task3", blank = True, default=' ')
    answe1 = models.CharField( "Answer3",max_length=300, blank = True, default=' ')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тапсырма"
        verbose_name_plural = "Тапсырмалар"

# лабораторные работы 
class labwork(models.Model):
    name = models.CharField("name", max_length=200, )
    description = models.CharField ("description", max_length = 300)
    materials = models.CharField("matrials", max_length=500, blank = True)
    data = models.DateField(auto_now=True)
    text = models.TextField("Your article")
    category = models.ForeignKey(Collection, related_name="labwork", on_delete= models.SET_NULL, null = True)
    tags = models.ManyToManyField(Teg, related_name = "laborator")
 

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Зертханалық жұмыс"
        verbose_name_plural = "Зертханалық жұмыстар"

    def get_absolute_url(self):
        return reverse('labwork', args=[str(self.id)])

# типо для экзаменационного материала
class exam(models.Model):
    name = models.CharField("name", max_length=200, default="")
    description = models.CharField("description", max_length = 300)
    data = models.DateField(auto_now=True)
    text = models.TextField("Some_text")
    tags = models.ManyToManyField(Teg, related_name = "examen")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Емтихан қағазы"
        verbose_name_plural = "Емтихан қағазылар"

    def get_absolute_url(self):
        return reverse('exam', args=[str(self.id)])