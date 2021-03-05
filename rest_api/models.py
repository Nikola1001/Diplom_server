from django.db import models
from django.contrib.auth.models import User



class Process(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    date = models.TextField()
    history = models.TextField()
    suspicious_processes = models.TextField()
    all_processes = models.TextField()

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title