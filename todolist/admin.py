from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Tasks, Category, Profile, User_Task

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)
admin.site.register(Tasks)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(User_Task)
# def display_genre(self):
#     """
#     Creates a string for the Genre. This is required to display genre in Admin.
#     """
#     return ', '.join([genre.name for genre in self.genre.all()[:3]])
#
#
# display_genre.short_description = 'Genre'
#
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
#     fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
#
# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'display_genre')
#
# # Register the Admin classes for BookInstance using the decorator
#
# @admin.register(BookInstance)
# class BookInstanceAdmin(admin.ModelAdmin):
#     list_filter = ('status', 'due_back')
#

