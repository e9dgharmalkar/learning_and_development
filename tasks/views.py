"""Django views for managing tasks in a task management application."""

from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Task, List




class DashboardView(TemplateView):
    template_name = 'tasks/task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lists'] = List.objects.order_by('-created_at')[:3]

        list_id = self.request.GET.get("list_id")
        task_id = self.request.GET.get("task_id")
        page = self.request.GET.get("page")

        if task_id:
            selected_task = Task.objects.get(id=task_id)
            subtasks = selected_task.subtask_set.all().order_by("deadline")

            paginator = Paginator(subtasks, 15)
            page_obj = paginator.get_page(page)

            context["selected_task"] = selected_task
            context["subtasks"] = page_obj

        elif list_id:
            selected_list = List.objects.get(id=list_id)
            

            paginator = Paginator(selected_list, 7)
            page_obj = paginator.get_page(page)

            context["selected_list"] = selected_list
            context["tasks"] = page_obj

        return context





class ListCreateView(CreateView):
    model = List
    fields = ["name"]
    template_name = "tasks/list_form.html"
    success_url = reverse_lazy("dashboard")


class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lists'] = List.objects.order_by('-created_at')[:3]
        return context

# class ListDetailView(DetailView):
#     model = List
#     template_name = "tasks/list_detail.html"
#     context_object_name = "list"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         tasks = Task.objects.filter(list=self.object).order_by("deadline")
#         print(tasks)
#         paginator = Paginator(tasks, 7)  # Show 7 tasks per page
#         page_number = self.request.GET.get('page')
#         page_obj = paginator.get_page(page_number)
#         context["tasks"] = page_obj
#         return context

    


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
