from django.contrib import admin
from .models import CustomUser, Categories, Task
# Register your models here.

class CustomUserFields(admin.ModelAdmin):
    fields= ['full_name', 'email']

class TaskFields(admin.ModelAdmin):
    fields= ['title','categories']
    list_display = ['title', 'get_categories']
    def get_categories(self,obj):
        return ", ".join([str(c) for c in obj.categories.all()])

admin.site.register(CustomUser)
admin.site.register(Categories)
admin.site.register(Task, TaskFields)