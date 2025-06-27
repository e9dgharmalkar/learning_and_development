"""This module defines the URL patterns for the tasks app."""

from django.urls import path
from .views import TaskListView, DashboardView, ListCreateView, DetailView


urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path('list/<int:pk>/', DashboardView.as_view(), name='list_detail'),
    path("add_list/", ListCreateView.as_view(), name="add_list"),
    path("tasks/", TaskListView.as_view(), name="task_list"),
    path("dashboard/task/<int:pk>/", DetailView.as_view(), name="task_detail"),
    path("task/<int:task_id>/", DashboardView.as_view(), name="list_detail"),
    # path('list/<int:list_id>/', views.list_detail, name='list_detail'),
    # path('add-list/', views.add_list, name='add_list'),
    # path("create/", TaskCreateView.as_view(), name="task_create"),
    # path("<int:pk>/update/", TaskUpdateView.as_view(), name="task_update"),
    # path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),
]
