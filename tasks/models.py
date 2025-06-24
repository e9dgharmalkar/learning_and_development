"""This module defines the models for the task management application."""

from collections import Counter
from django.db import models


STATUS_CHOICES = [
    ("Pending", "Pending"),
    ("In Progress", "In Progress"),
    ("In Review", "In Review"),
    ("Completed", "Completed"),
    ("On Hold", "On Hold"),
]


class List(models.Model):
    """Model representing a list of tasks."""

    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Task(models.Model):
    """Model representing a task."""

    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    deadline = models.DateTimeField(null=True, blank=True)
    description = models.TextField(blank=True)
    list = models.ForeignKey(
        "List", on_delete=models.CASCADE, related_name="tasks", null=True, blank=True
    )

    def __str__(self):
        return f"{self.title}"

    # Create your models here.

    @property
    def status(self):
        """Calculate the status of the task based on its subtasks."""
        statuses = [subtask.status for subtask in self.subtasks.all()]
        if not statuses:
            return "Pending"
        counter = Counter(statuses)
        if len(counter) == 1:
            return statuses[0]
        return "In Progress"


class SubTask(models.Model):
    """Model representing a subtask of a task."""

    name = models.CharField(max_length=255)
    assignee = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    task = models.ForeignKey("Task", on_delete=models.CASCADE, related_name="subtasks")

    def __str__(self):
        return f"{self.name}"
