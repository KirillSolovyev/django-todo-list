from django.contrib import admin
from app.models import List, Task


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'due', 'user', 'list']
    ordering = ['name']
    search_fields = ['name', 'user__first_name', 'list__name']
    list_filter = ['created', 'due']
