from django.contrib import admin
from .models import Category, Author, Task

# Register your models here.

# /* model Category */
admin.site.register(Category)

# /* model Author */
admin.site.register(Author)

# /* model Task (modificant qué es veure en el panel de admin) */
class TaskAdmin(admin.ModelAdmin):
    fields= ['title', 'author', 'categories']
    list_display = ['title', 'get_categories']

    # 👇🏼 Aixó es una funció customitzable per veure les categories en el panell d'admin
    def get_categories(self,obj):
        return ", ".join([str(c) for c in obj.categories.all()])

admin.site.register(Task, TaskAdmin)