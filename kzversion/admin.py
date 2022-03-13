from django.contrib import admin
from main.models import laborator
from .models import *
from mptt.admin import MPTTModelAdmin

admin.site.register(Collection, MPTTModelAdmin)
admin.site.register(Teg)

@admin.register(lect)
class LectionAdmin(admin.ModelAdmin):
    list_display = ["name", "description","data", "id"]

@admin.register(exemples)
class LectionAdmin(admin.ModelAdmin):
    list_display = ["name","data", "id"]

@admin.register(labwork)
class LectionAdmin(admin.ModelAdmin):
    list_display = ["name", "description","data", "id"]

@admin.register(exam)
class LectionAdmin(admin.ModelAdmin):
    list_display = ["name", "description","data", "id"]
