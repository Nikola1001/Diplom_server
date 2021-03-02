from django.forms import ModelForm
from .models import Tasks, Category, Profile

class TasksForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ('title', 'content', 'category')


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name',)


