from django.db import models

# Create your models here.


class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    task_title = models.CharField(max_length=100)
    task_details = models.TextField()

    def __str__(self):
        return (f"{self.task_title}")
