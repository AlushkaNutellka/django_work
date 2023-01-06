from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=40)
    body = models.TextField(blank=True)
    deadline = models.DateField()
    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=True)

    def __str__(self):
        return self.title
