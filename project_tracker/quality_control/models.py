from django.db import models
from django.utils import timezone
from tasks.models import Project, Task

class BugReport(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)
    STATUS_CHOICES = [
        ('Новая', 'Новая'),
        ('В работе', 'В работе'),
        ('Завершена', 'Завершена'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    priority = models.IntegerField(default=1)  # Добавлено поле priority
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

class FeatureRequest(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)
    STATUS_CHOICES = [
        ('Рассмотрение', 'Рассмотрение'),
        ('Принято', 'Принято'),
        ('Отклонено', 'Отклонено'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    priority = models.IntegerField(default=1)  # Добавлено поле priority
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)