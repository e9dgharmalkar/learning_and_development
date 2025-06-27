"""Django views for managing tasks in a task management application."""

from django.views.generic import TemplateView
from tasks.models import List, Task, SubTask


class DashboardView(TemplateView):
    """
    This view provides
        1. lists
        2. tasks in a list if selected else tasks in first available list
        3. subtasks in a task if selected
    """

    template_name = "tasks/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lists = List.objects.all().order_by("-created_at")
        selected_list, tasks = self.get_tasks(lists)
        selected_task, subtasks = self.get_selected_task_details(tasks)

        context.update(
            {
                "lists": lists,
                "selected_list": selected_list,
                "tasks": tasks,
                "selected_task": selected_task,
                "subtasks": subtasks,
            }
        )

        print(context)

        return context

    def get_tasks(self, lists):
        if not lists:
            return (List.objects.none(), Task.objects.none())

        list_id = self.request.GET.get("list_id", lists.first().id)
        return (List.objects.get(id=list_id), Task.objects.filter(list__id=list_id))

    def get_selected_task_details(self, tasks):
        if not tasks:
            return (Task.objects.none(), SubTask.objects.none())

        task_id = self.request.GET.get("task_id", tasks.first().id)
        print(f"Selected task ID: {task_id}")  # Debugging line to check task_id

        print(SubTask.objects.filter(task__id=task_id))

        return (Task.objects.get(id=task_id), SubTask.objects.filter(task__id=task_id))
