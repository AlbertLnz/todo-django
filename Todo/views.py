from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

# Create your views here.

def first_fnct(request):
    # return HttpResponse({'message': 'Hello World!'})
    return render(request, 'index.html')

def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'Todo/list_tasks.html', {'tasks':
    tasks})

def add_task(request):
    # if request.method == 'POST':
    # form = LibroForm(request.POST)
    # if form.is_valid():
    # form.save()
    # return redirect('lista_libros')

    # else:
    # form = LibroForm()
    # return render(request, 'libros/form_libro.html', {'form': form})

    pass

def editar_libro(request, id):
    # libro = get_object_or_404(Libro, id=id)
    # if request.method == 'POST':
    # form = LibroForm(request.POST, instance=libro)
    # if form.is_valid():
    # form.save()
    # return redirect('lista_libros')

    # else:
    # form = LibroForm(instance=libro)
    # return render(request, 'libros/form_libro.html', {'form': form})
    pass