from django import forms
from .models import Task

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
