import ast
from msilib.schema import ListView

from django.db.models import Q
from django.shortcuts import render


from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
from .models import Tasks, Category, User, Profile, User_Task
from .forms import TasksForm, CategoryForm
from django.shortcuts import redirect
from django.http import HttpResponse

from rest_api.models import Process, User_proc
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
    num_tasks = Tasks.objects.all().count()
    num_completed = Tasks.objects.filter(status_completed=True).count()
    num_process = User_Task.objects.all().count()
    context = {'tasks': tasks, 'categors': categors, 'num_tasks': num_tasks, 'num_completed': num_completed, 'num_process': num_process}
    return render(request, 'index.html', context)


def by_category(request, category_id):
    tasks = Tasks.objects.filter(category = category_id, status_completed=False)
    categors = Category.objects.all()
    current_category = Category.objects.get(pk=category_id)
    context = {'tasks': tasks, 'categors': categors, 'current_category': current_category}
    return render(request, 'by_category.html', context)


def by_task(request, name):
    # task = Tasks.objects.get(title=name)
    # users = Profile.objects.filter(selected_tasks = task)
    # # users = User.objects.all()
    # name_task = task.title
    # content = task.content
    # return render(request, 'by_task.html', {'name': name_task, 'content': content, 'users': users})
####################
    task = Tasks.objects.get(title=name)

    users_all = User_Task.objects.filter(task=task)

    users =[]
    for u in users_all:
        users.append(u.user)

    name_task = task.title
    content = task.content
    date = task.published
    return render(request, 'by_task.html', {'name': name_task, 'content': content, 'users': users, 'date': date})


def tasks_by_user (request, user_id):
    # user = Tasks.objects.get(username)
    # tasks = username.selected_tasks()
    # tasks = Tasks.objects.get(id=1)
    user = Profile.objects.get(user=user_id)
    # tasks = user.selected_tasks.all()
#######################################################
    tasks = []
    tasks_all = User_Task.objects.filter(user=user)
    for task in tasks_all:
        tasks.append(task.task)

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
    # user = Profile.objects.get(user=user_id)
    # task = Tasks.objects.get(title=name)
    # users = Profile.objects.filter(selected_tasks=task)
    # usdo = user.selected_tasks
    #
    # # user.selected_tasks.intersection(user.selected_tasks,  task)
    #
    # user.selected_tasks.add(task)
    # user.save()
    # do = user.selected_tasks.all()
    # # do.union(task)
    #
    # print(type(task))
    # print(type(user))
    # print(type(users))
    #
    # # user.selected_tasks.add(task)
    # user.bio = "sdgffdgdfgeregreg"
    # us = user
    # ts = task
    # ut = us.selected_tasks
    # if user in users:
    #     answer = "Задача уже добавлена в список ваших задач"
    # else:
    #     answer = 'Задача успешно добавлена'
    # name_task = task.title
    # content = task.content
    # return render(request, 'by_task.html', {'name': name_task, 'content': content, 'users': users, 'answer':answer, 'usdo':usdo ,'us':us, 'ts':ts, 'ut':ut, 'u':do})
###############################################################
    user = Profile.objects.get(user=user_id)
    task = Tasks.objects.get(title=name)
    users = User_Task.objects.filter(task=task).all()
    find = User_Task.objects.filter(user=user, task=task)
    answer=''
    if not find:
        us = User_Task(task=task, user=user)
        us.save()
        answer = 'Задача успешно добавлена'
    else:
        answer = "Задача уже была добавлена в список ваших задач"
    us = name_task= content = usdo= ts =ut =do= 'dolzhen bit text'
    return render(request, 'by_task.html',
                  {'name': name_task, 'content': content, 'users': users, 'answer': answer, 'usdo': usdo, 'us': us,
                   'ts': ts, 'ut': ut, 'u': do})




def about_task_for_user(request, user_id, name):
    task = Tasks.objects.get(title=name)
######################################
    # users = Profile.objects.filter(selected_tasks=task)
    users_all = User_Task.objects.filter(task=task).all()
    users = []
    for us in users_all:
        users.append(us.user)
    # users = User.objects.all()
    name_task = task.title
    content = task.content
    return render(request, 'about_task_for_user.html', {'name': name_task, 'content': content, 'users': users})


def mark_task_completed(request, user_id, name):     # Нужно удалить задачу у других юзеров
    user = Profile.objects.get(user=user_id)
    task = Tasks.objects.get(title=name)
    # task.user_completed_task = user
    name_task = task.title
    content = task.content
    ##############################
    # user.completed_task.add(task)      #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    task.user_completed_task.add(user)
##########################
    # users = Profile.objects.filter(selected_tasks=task)
    # users_all = User_Task.objects.filter(task=task).all()
    User_Task.objects.filter(task=task).all().delete()
    users =[]
    # for us in users_all:
    #     us.remove()
        # users.append(us.user)
    task.status_completed = True
    task.save()
    answer_complete='Задача отмечена как выполненная'

    return render(request, 'about_task_for_user.html', {'name': name_task, 'content': content, 'users': users, 'answer_complete':answer_complete})


def refuse_task(request, user_id, name):
    user = Profile.objects.get(user=user_id)
    task = Tasks.objects.get(title=name)
    user.refused_tasks.add(task)
    name_task = task.title
    content = task.content
    ##########################
    # users = Profile.objects.filter(selected_tasks=task)
    users_all = User_Task.objects.filter(task=task).all()
    users = []
    for us in users_all:
        users.append(us.user)
    # task.status_completed = True
    # task.save()
    User_Task.objects.filter(user=user, task=task).delete()
    answer_refuse = 'Вы отказались от задачи'

    return render(request, 'about_task_for_user.html',
                  {'name': name_task, 'content': content, 'users': users, 'answer_refuse': answer_refuse})


def completed_tasks(request):
    tasks = Tasks.objects.filter(status_completed=True)
    return render(request, 'completed_task.html', {'tasks': tasks})


def about_completed_task(request, name):
    task = Tasks.objects.get(title=name)
    users_all = User_Task.objects.filter(task=task).all()
    users = []
    for us in users_all:
        users.append(us.user)
    # users = User.objects.all()
    name_task = task.title
    content = task.content
    return render(request, 'about_completed_task.html', {'name': name_task, 'content': content, 'users': users})


def user_processes(request, user_id):
    processes = Process.objects.filter(author=user_id)
    for p in processes:
        ans = p.suspicious_processes
        history = p.history
    # print("ssss")
    ans = ast.literal_eval(ans)
    history = ast.literal_eval(history)

    # ast.literal_eval("{'muffin' : 'lolz', 'foo' : 'kitty'}")
    history_time = []
    history_link = []
    for t, l in history:

        history_time.append(t)
        history_link.append(l)
    # print(history_time)

    return render(request, 'user_processes.html', {'processes': ans, 'history_time': history_time})


def all_users(request):
    users = Profile.objects.all()
    return render(request, 'users.html', {'users':users})


def about_user(request, user_id):
    return render(request, 'about_user.html', {})


def about_user_tasks(request, user_id):
    user = Profile.objects.get(user=user_id)
    tasks = []
    tasks_all = User_Task.objects.filter(user=user)
    for task in tasks_all:
        tasks.append(task.task)
    tasks_completed = Tasks.objects.filter(user_completed_task=user)
    refused_tasks = user.refused_tasks.all()
    return render(request, 'about_user_tasks.html', {'tasks_completed': tasks_completed, 'refused_tasks': refused_tasks, 'tasks': tasks})


def about_user_processes(request, user_id):
    user = Process.objects.filter(author=user_id)
    for p in user:
        suspicious_processes = p.suspicious_processes
        all_processes = p.all_processes
    suspicious_processes = ast.literal_eval(suspicious_processes)
    all_processes = ast.literal_eval(all_processes)
    return render(request, 'about_user_processes.html', {'suspicious_processes':suspicious_processes, 'all_processes': all_processes})


def about_user_history(request, user_id):
    user = Process.objects.filter(author=user_id)
    for p in user:
        history = p.history
    history = ast.literal_eval(history)
    return render(request, 'about_user_history.html', { 'history': history})