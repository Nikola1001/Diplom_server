from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import User
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.dispatch import receiver
from django.db.models.signals import post_save




class Category(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ['name']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_last_name = models.CharField(max_length=150, verbose_name='ФИО')
    # bio = models.TextField(max_length=500, blank=True)
    email = models.CharField(max_length=50, blank=True, verbose_name='Почта')
    location = models.CharField(max_length=40, blank=True, verbose_name='Группа')
    position = models.CharField(max_length=50, blank=True, verbose_name='Должность')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    # selected_tasks = models.ManyToManyField(Tasks, null=True, verbose_name='Выбранные задачи')
    # selected_tasks = models.ManyToManyField(Tasks, verbose_name='Выбранные задачи')

    refused_tasks = models.ManyToManyField('Tasks', blank=True,
                                            verbose_name='Задачи, от которых отказался')

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Tasks (models.Model):
    paginate_by = 10
    title = models.CharField(max_length=50, verbose_name='Название задачи')
    content = models.TextField(null = True, blank=True, verbose_name='Описание')

    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Создана')
    category = models.ForeignKey('Category', null=True, on_delete=models.PROTECT, verbose_name='Категория')
    status_completed = models.BooleanField(default=False)
    user_completed_task = models.ManyToManyField('Profile', null=True,
                                            verbose_name='Пользователь, завершивший задачу')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Задачи'
        verbose_name = 'Задача'
        ordering = ['-published']


class User_Task(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Пользователь')
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE, verbose_name='Выбранная задача')

    def __str__(self):
        return str(self.user) + ' ' + str(self.task)

