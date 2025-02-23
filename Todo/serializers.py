from rest_framework import serializers
from .models import Category, Author, Task

class CategorySerializer(serializers.ModelSerializer):
    class Meta():
        model = Category
        fields = ['name', 'description'] # == '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta():
        model = Author
        fields = ['user', 'dni', 'photo'] # == '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta():
        model = Task
        fields = ['title', 'author', 'completed', 'categories'] # == '__all__'
