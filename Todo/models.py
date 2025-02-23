from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dni = models.CharField(max_length=9)
    photo = models.ImageField(default='fallback_avatar.webp', blank=True)

    def __str__(self):
        return self.user.username # <- S'accedeix a través de user

class Task(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title + ' ' + str(self.author)
