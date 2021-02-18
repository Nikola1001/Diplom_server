from django.views.generic import RedirectView
from django.urls import path, include
from .views import *

urlpatterns = [
    path('',redirect_todolist),
    path('todolist/', index, name='index'),
    path('add/', TaskCreateView.as_view(), name='add'),
    path('add_category/', CategoryCreateView.as_view(), name='add_category'),
    path('<int:category_id>/', by_category, name='by_category'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('about_task/<str:name>/', by_task, name='by_task'),
    path('tasks_user/<int:user_id>/', tasks_by_user, name='task_by_user'),
    path('add_task_user/<str:name>/<int:user_id>/', add_task_user, name='add_task_user'),
    path('about_task_for_user/<str:name>/<int:user_id>/', about_task_for_user, name='about_task_for_user'),
    path('mark_task_completed/<str:name>/<int:user_id>/', mark_task_completed, name='mark_task_completed'),
    path('mark_task_refuse/<str:name>/<int:user_id>/', refuse_task, name='mark_task_refuse'),
    path('completed_task', completed_tasks, name='completed_tasks'),
    path('about_completed_task/<str:name>/', about_completed_task, name='about_completed_task'),
    path('user_processes/<int:user_id>/', user_processes, name='user_processes'),
    path('users/', all_users, name='users'),
    path('about_user/<int:user_id>/', about_user, name='about_user'),
    path('about_user/history/<int:user_id>/', about_user_history, name='about_user_history'),
    path('about_user/processes/<int:user_id>/', about_user_processes, name='about_user_processes'),
    path('about_user/tasks/<int:user_id>/', about_user_tasks, name='about_user_tasks'),

]
