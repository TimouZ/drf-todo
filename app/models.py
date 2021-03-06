from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    summary = models.CharField(max_length=64, unique=True, blank=False)
    description = models.TextField(max_length=128, blank=True, null=True)
    owner = models.ForeignKey(User, related_name='task_author', on_delete=models.CASCADE)
    assignee = models.ManyToManyField(User, related_name='task_assignee', blank=True)  # Optional field, can be empty
    photo = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
