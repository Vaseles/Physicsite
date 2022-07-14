from django.contrib import admin
from .models import *

admin.site.register(Tag)
admin.site.register(Examen)

@admin.register(Article)
class LectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'tag', 'updated']

@admin.register(Labwork)
class LectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'tag', 'updated']

@admin.register(Practise)
class LectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'tag', 'updated']