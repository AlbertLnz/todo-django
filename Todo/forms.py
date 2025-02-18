from django import forms
from .models import Task, Author
from django.contrib.auth.models import User
import re

# ~~~~~~~~~~~~ TASK ~~~~~~~~~~~~~~~~~~

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


# ~~~~~~~~~~~~ REGISTER USER ~~~~~~~~~~~~~~~~~~

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

        widgets = {
            'dni': forms.TextInput(attrs={'name': 'dni'}),
        }

    # S'executa automàticament al utilizar la función 'is_valid'
    def clean_dni(self):
        dni = self.cleaned_data.get('dni')
        pattern = r"^(\d{8})([A-Z])$"
        if not re.fullmatch(pattern, dni):
            raise forms.ValidationError("El DNI no vàlid")
        return dni
