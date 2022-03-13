from django.contrib import admin
from .models import *
from . import models
from mptt.admin import MPTTModelAdmin

@admin.register(lection)
class LectionAdmin(admin.ModelAdmin):
    list_display = ["title", "description","data", "id"]

@admin.register(task)
class LectionAdmin(admin.ModelAdmin):
    list_display = ["title","data", "id"]

@admin.register(laborator)
class LectionAdmin(admin.ModelAdmin):
    list_display = ["title", "description","data", "id"]

@admin.register(examen)
class LectionAdmin(admin.ModelAdmin):
    list_display = ["title", "description","data", "id"]


admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Tag)