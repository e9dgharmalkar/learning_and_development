"""This module contains the form for the Task model."""

from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    """Form for creating and updating tasks."""

    class Meta:
        """Meta class for TaskForm."""

        model = Task
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        """Initialize the form with custom settings."""
        super().__init__(*args, **kwargs)
