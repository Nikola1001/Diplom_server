from django.db import models


class User_proc(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()

  def __str__(self):
      return self.name


class Process(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()
    history = models.TextField()
    suspicious_processes = models.TextField()
    all_processes = models.TextField()

    author = models.ForeignKey('User_proc', related_name='process', on_delete=models.CASCADE)

    def __str__(self):
        return self.title