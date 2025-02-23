from django import forms
from .models import Task, Author, Category
from django.contrib.auth.models import User
import re

# ~~~~~~~~~~~~ TASK ~~~~~~~~~~~~~~~~~~

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']

        widgets = {
            'title': forms.TextInput(attrs={'name': 'title'}),
            # 'author', foreignKey don't need to be on form
            # 'categories': foreignKey don't need to be on form
        }

# ~~~~~~~~~~~~ CATEGORIES ~~~~~~~~~~~~~~~~~~

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


# ~~~~~~~~~~~~ REGISTER USER ~~~~~~~~~~~~~~~~~~

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['username', 'password']

        widgets = {
            'username': forms.TextInput(attrs={'name': 'username'}),
            'password': forms.PasswordInput(attrs={'name': 'password'})
        }

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['dni', 'photo']

        widgets = {
            'dni': forms.TextInput(attrs={'name': 'dni'}),
        }

    def clean_dni(self):
        dni = self.cleaned_data.get('dni')
        pattern = r"^(\d{8})([A-Z])$"
        if not re.fullmatch(pattern, dni):
            raise forms.ValidationError("El DNI no vàlid")
        return dni
