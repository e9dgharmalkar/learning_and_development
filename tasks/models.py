from django.db import models
class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    deadline = models.DateTimeField(null=True, blank=True)
    description = models.TextField(blank=True)
    list = models.ForeignKey('List', on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
    def __str__(self):
        return self.title
    # Create your models here.

    @property
    def status(self):
        statuses = [subtask.status for subtask in self.subtasks.all()]

        if all(status == 'Pending' for status in statuses):
            return 'Pending'
        elif any(status in ['In Progress', 'In Review', 'Completed'] for status in statuses):
            return 'In Progress'
        elif all(status == 'Completed' for status in statuses):
            return 'Completed'
        elif all(status == 'On Hold' for status in statuses):
            return 'On Hold'
        else:
            return 'Mixed'

class List(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
class SubTask(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('In Review', 'In Review'),
        ('Completed', 'Completed'),
        ('On Hold', 'On Hold'),
    ]

    name = models.CharField(max_length=255)
    assignee = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')

    def __str__(self):
        return self.name

