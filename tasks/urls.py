"""This module defines the URL patterns for the tasks app."""

from django.urls import path
from tasks.views import DashboardView


urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
]
