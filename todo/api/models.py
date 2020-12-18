from django.db import models

class Task(models.Model):
    title = models.TextField()
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title