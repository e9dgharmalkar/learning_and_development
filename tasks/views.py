"""Django views for managing tasks in a task management application."""

from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Task, List




def dashboard(request):
    lists = List.objects.order_by("-created_at")[:3]
    return render(request, "tasks/task_list.html", {"lists": lists})


class ListCreateView(CreateView):
    model = List
    fields = ["name"]
    template_name = "tasks/list_form.html"
    success_url = reverse_lazy("dashboard")


class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"


# class TaskCreateView(CreateView):
#     """View for creating a new task."""

#     model = Task
#     fields = ["title", "description", "completed", "deadline"]
#     template_name = "task_form.html"
#     success_url = reverse_lazy("task_list")


# class TaskUpdateView(UpdateView):
#     """View for updating an existing task."""

#     model = Task
#     fields = ["title", "description", "completed", "deadline"]
#     template_name = "task_form.html"
#     success_url = reverse_lazy("task_list")


# class TaskDeleteView(DeleteView):
#     """View for deleting a task."""

#     model = Task
#     template_name = "task_confirm_delete.html"
#     success_url = reverse_lazy("task_list")
