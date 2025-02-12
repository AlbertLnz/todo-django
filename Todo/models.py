from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name
    
    
class CustomUser(User):
    full_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.username

class Task(models.Model):
    title = models.CharField(max_length=300)
    completed = models.BooleanField(default=False)
    categories = models.ManyToManyField(Categories)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    