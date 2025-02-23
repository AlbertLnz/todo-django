from .models import Category, Author, Task
from .serializers import CategorySerializer, AuthorSerializer, TaskSerializer
from rest_framework import viewsets, permissions, request
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategorySerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AuthorSerializer

# TASKS BY ARGS
# api/tasks -> returns all tasks
# api/tasks/<id> -> returns a single task
class TaskViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
