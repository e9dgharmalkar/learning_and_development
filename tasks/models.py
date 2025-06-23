from django.db import models
from collections import Counter              
STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('In Review', 'In Review'),
        ('Completed', 'Completed'),
        ('On Hold', 'On Hold'),]
class List(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
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
        if not statuses:
            return 'Pending'
        Counter = Counter(statuses)
        if len(Counter) == 1:
            return statuses[0]
        return "In Progress" 

        
    class SubTask(models.Model):
       
    

     name = models.CharField(max_length=255)
    assignee = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='subtasks')

    def __str__(self):
        return self.name   




