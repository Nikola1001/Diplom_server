

from django.shortcuts import render

from .models import Book, Author, BookInstance, Genre
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
from .models import Tasks, Category, User, Profile
from .forms import TasksForm, CategoryForm
from django.shortcuts import redirect
from django.http import HttpResponse
# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'


# def index(request):
#     """
#     Функция отображения для домашней страницы сайта.
#     """
#     # Генерация "количеств" некоторых главных объектов
#     num_books=Book.objects.all().count()
#     num_instances=BookInstance.objects.all().count()
#     # Доступные книги (статус = 'a')
#     num_instances_available=BookInstance.objects.filter(status__exact='a').count()
#     num_authors=Author.objects.count()  # Метод 'all()' применен по умолчанию.
#
#     # Отрисовка HTML-шаблона index.html с данными внутри
#     # переменной контекста context
#     return render(
#         request,
#         'index.html',
#         context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
#     )
def redirect_todolist(request):
    return redirect('index', permanent=True)


def index(request):
    tasks = Tasks.objects.all()
    num_tasks = Tasks.objects.all().count()
    categors = Category.objects.all()
    context = {'tasks': tasks, 'categors': categors}
    return render(request, 'index.html', context)


def by_category(request, category_id):
    tasks = Tasks.objects.filter(category = category_id, status_completed=False)
    categors = Category.objects.all()
    current_category = Category.objects.get(pk=category_id)
    context = {'tasks': tasks, 'categors': categors, 'current_category': current_category}
    return render(request, 'by_category.html', context)


def by_task(request, name):
    task = Tasks.objects.get(title=name)
    users = Profile.objects.filter(selected_tasks = task)
    # users = User.objects.all()
    name_task = task.title
    content = task.content
    return render(request, 'by_task.html', {'name': name_task, 'content': content, 'users': users})


def tasks_by_user (request, user_id):
    # user = Tasks.objects.get(username)
    # tasks = username.selected_tasks()
    # tasks = Tasks.objects.get(id=1)
    user = Profile.objects.get(user=user_id)
    tasks = user.selected_tasks.all()
    # tasks = username
    return render(request, 'task_by_user.html', {'tasks': tasks})


class TaskCreateView(CreateView):
    template_name = 'create_task.html'
    form_class = TasksForm
    success_url = '/todolist/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categors'] = Category.objects.all()
        return context


class CategoryCreateView(CreateView):
    template_name = 'create_category.html'
    form_class = CategoryForm
    success_url = '/todolist/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categors'] = Category.objects.all()
        return context


def add_task_user(request, name, user_id):
    user = Profile.objects.get(user=user_id)
    task = Tasks.objects.get(title=name)
    users = Profile.objects.filter(selected_tasks=task)
    usdo = user.selected_tasks

    # user.selected_tasks.intersection(user.selected_tasks,  task)

    user.selected_tasks.add(task)
    user.save()
    do = user.selected_tasks.all()
    # do.union(task)

    print(type(task))
    print(type(user))
    print(type(users))

    # user.selected_tasks.add(task)
    user.bio = "sdgffdgdfgeregreg"
    us = user
    ts = task
    ut = us.selected_tasks
    if user in users:
        answer = "Задача уже добавлена в список ваших задач"
    else:
        answer = 'Задача успешно добавлена'
    name_task = task.title
    content = task.content
    return render(request, 'by_task.html', {'name': name_task, 'content': content, 'users': users, 'answer':answer, 'usdo':usdo ,'us':us, 'ts':ts, 'ut':ut, 'u':do})

def about_task_for_user(request, user_id, name):
    task = Tasks.objects.get(title=name)
    users = Profile.objects.filter(selected_tasks=task)
    # users = User.objects.all()
    name_task = task.title
    content = task.content
    return render(request, 'about_task_for_user.html', {'name': name_task, 'content': content, 'users': users})


def mark_task_completed(request, user_id, name):     # Нужно удалить задачу у других юзеров
    user = Profile.objects.get(user=user_id)
    task = Tasks.objects.get(title=name)
    name_task = Tasks.objects.get(title=name).title
    content =Tasks.objects.get(title=name).content
    users = Profile.objects.filter(selected_tasks=task)
    task.status_completed = True


    return render(request, 'about_task_for_user.html', {'name': name_task, 'content': content, 'users': users, 'answer':answer})

