# taskmanager/urls.py
"""Task Manager URL Configuration"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("tasks.urls")),
]
# This code includes the URL patterns for the task management application.
# It includes paths for the Django admin interface and the task management app's URLs.
