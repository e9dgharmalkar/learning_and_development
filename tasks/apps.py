"""Django application configuration for the tasks app.
This file defines the configuration for the task
s application, including the default auto field
 type and the name of the application.
"""

from django.apps import AppConfig


class TasksConfig(AppConfig):
    """Configuration class for the tasks application."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "tasks"
