from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.models import User
from .models import Task, Category, Author
from .forms import TaskForm

# Create your views here.

def show_index_page(request):
    return render(request, 'index.html', { 'title': "Aplicació To-Do"})


def list_tasks(request):
    # Aqui utilizo 'Author' en compte de 'User' perque son molt semblants (es diferencien només que User no té dni)
    # I en la vista, només vull el "name", així que es indiferent
    author = Author.objects.all()
    tasks = Task.objects.all()
    categories = Category.objects.all()

    return render(request, 'list_tasks.html', {'authors': author, 'tasks': tasks, 'categories': categories})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            title = request.POST.get('title')
            author_id = request.POST.get('author_id')
            categories_ids = request.POST.getlist('categories_ids')

            author = Author.objects.get(id=author_id)
            categories = Category.objects.filter(id__in=categories_ids)

            task = Task.objects.create(
                title=title,
                author=author,
                completed=False,
            )
            task.categories.set(categories) # En les relacion Many-To-Many, s'ha d'afegir amb un 'set'

            task.save()
            return redirect('llistar_tasques')
        else:
            return redirect('index')

    else:
        return TaskForm()

def edit_task(request, id):
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

def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        task.delete()
    return redirect('llistar_tasques')

# def eliminar_libro(request, id):
#     libro = get_object_or_404(Libro, id=id)
#     if request.method == 'POST':
#         libro.delete()
#         return redirect('lista_libros')
#     return render(request, 'aplicacion1/eliminar_libro.html', {'libro': libro})