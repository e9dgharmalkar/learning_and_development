from django.contrib import admin
from .models import Task, List, SubTask

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'list', 'completed', 'status')  # shows status in admin too

@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'assignee', 'status', 'task')
