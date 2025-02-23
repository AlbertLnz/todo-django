from django.contrib import admin
from .models import Category, Author, Task

admin.site.register(Category)

admin.site.register(Author)

class TaskAdmin(admin.ModelAdmin):
    fields= ['title', 'author', 'categories']
    list_display = ['title', 'get_categories']

    def get_categories(self,obj):
        return ", ".join([str(c) for c in obj.categories.all()])

admin.site.register(Task, TaskAdmin)