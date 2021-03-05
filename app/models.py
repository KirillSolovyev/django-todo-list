from django.db import models
from django.conf import settings


class List(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=256)
    created = models.DateField(auto_now=True)
    due = models.DateField()
    completed = models.BooleanField(default=False)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
