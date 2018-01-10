from django.db import models

class Todo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    duedate = models.DateTimeField(blank=True,null=True)
    memo = models.TextField()
    taskfinish = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)
