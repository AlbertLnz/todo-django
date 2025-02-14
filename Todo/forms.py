from django import forms
from .models import Task, Author
from django.contrib.auth.models import User
import re

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']

        # FIX! No sé perquè 'author' i 'categories' no fa bé la validació...

        widgets = {
            'title': forms.TextInput(attrs={'name': 'title'}),
            # 'author': forms.Select(attrs={'name': 'author'}),
            # 'categories': forms.SelectMultiple(attrs={'name': 'categories'})
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['username', 'password']

    widgets = {
        'username': forms.TextInput(attrs={'name': 'user_id'}),
        'password': forms.PasswordInput(attrs={'name': 'password'})
  
    }
class AuthorForm(forms.ModelForm):
    class Meta:
       
        model = Author
        fields = ['dni']

        # FIX! No sé perquè 'author' i 'categories' no fa bé la validació...

        widgets = {
            'dni': forms.TextInput(attrs={'name': 'dni'}),
        }
        
    # def dni_validation(dni):
    #     pattern = r"^(\d{8})([A-Z])$"
    #     return re.fullmatch(pattern, dni)
    
    # def clean_dni(self):
    #     dni = self.cleaned_data.get('dni')
        
    #     if not self.dni_validation(dni):
    #         raise forms.ValidationError("DNI incorrecto")
        
    #     return dni
    # def clean_user(self):
    #     user = self.cleaned_data.get('user_id')
    #     return user
    # def clean_password(self):
    #     user = self.cleaned_data.get('password')
    #     return user
