from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Task, Category, Author
from .forms import TaskForm, AuthorForm, UserForm

# Create your views here.

def show_index_page(request):
    return render(request, 'index.html', { 'title': "Aplicació To-Do"})

def show_register_page(request):
    authorForm = AuthorForm() 
    userForm = UserForm() 
    return render(request, 'register.html', {'userForm': userForm, 'authorForm': authorForm})



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

def edit_task(request, task_id):

    if request.method == "GET":
        task = get_object_or_404(Task, id=task_id)
        categories = Category.objects.all()
        return render(request, 'edit_task.html', { "task": task, "categories": categories })

    else:
        task = get_object_or_404(Task, id=task_id)
        categories_ids = request.POST.getlist('categories_ids')
        categories = Category.objects.filter(id__in=categories_ids)
        title = request.POST.get('title')
        is_completed = bool(request.POST.getlist('completed'))

        task.categories.set(categories)

        task.title = title
        task.completed = is_completed
        task.categories.set(categories)  # Asignar las categorías seleccionadas

        task.save()

        return redirect('llistar_tasques')
    # task = 
    # libro = get_object_or_404(Libro, id=id)
    # if request.method == 'POST':
    # form = LibroForm(request.POST, instance=libro)
    # if form.is_valid():
    # form.save()
    # return redirect('lista_libros')

    # else:
    # form = LibroForm(instance=libro)

def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('llistar_tasques')
