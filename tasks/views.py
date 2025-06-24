"""Django views for managing tasks in a task management application."""

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task


class TaskListView(ListView):
    """View for listing all tasks."""

    model = Task
    template_name = "task_list.html"
    context_object_name = "tasks"


class TaskCreateView(CreateView):
    """View for creating a new task."""

    model = Task
    fields = ["title", "description", "completed", "deadline"]
    template_name = "task_form.html"
    success_url = reverse_lazy("task_list")


class TaskUpdateView(UpdateView):
    """View for updating an existing task."""

    model = Task
    fields = ["title", "description", "completed", "deadline"]
    template_name = "task_form.html"
    success_url = reverse_lazy("task_list")


class TaskDeleteView(DeleteView):
    """View for deleting a task."""

    model = Task
    template_name = "task_confirm_delete.html"
    success_url = reverse_lazy("task_list")
