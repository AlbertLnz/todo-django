from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import Task, Category, Author
from .forms import TaskForm, AuthorForm, UserForm

# Create your views here.

def show_index_page(request):
    user = request.user

    return render(request, 'index.html', { 'title': "Aplicació To-Do", 'user': user})

@login_required
def list_tasks(request):
    user = request.user
    # Aqui utilizo 'Author' en compte de 'User' perque son molt semblants (es diferencien només que User no té dni)
    # I en la vista, només vull el "name", així que es indiferent
    author = Author.objects.all()
    tasks = Task.objects.all()
    categories = Category.objects.all()
    return render(request, 'list_tasks.html', {'authors': author, 'tasks': tasks, 'categories': categories, 'user': user})

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


# ########### AUTHOR #####################

def show_register_page(request):
    authorForm = AuthorForm()
    userForm = UserForm()
    return render(request, 'register.html', {'userForm': userForm, 'authorForm': authorForm})


def register_author(request):
    if request.method == 'POST':
        userForm = UserForm(request.POST)
        authorForm = AuthorForm(request.POST)

        if userForm.is_valid() and authorForm.is_valid():
            username = userForm.cleaned_data['username'] # Abans d'utilitzar 'cleaned_data', has de validar que el form sigui vàlid
            password = userForm.cleaned_data['password']
            dni = authorForm.cleaned_data['dni']

            tmp_user, created = User.objects.get_or_create(username=username)

            if created:
                tmp_user.set_password(password)
                tmp_user.save()

            author, created = Author.objects.get_or_create(user=tmp_user, defaults={'dni': dni})

            if created:
                author.dni = dni
                author.save()
            return redirect('login')

        elif not authorForm.is_valid():
            return render(request, 'register.html', {'userForm': UserForm(), 'authorForm': AuthorForm(), 'error_message': ' - DNI incorrect, ha de tenir 8 números i 1 lletra'})

        else:
            return render(request, 'register.html', {'userForm': UserForm(), 'authorForm': AuthorForm(), 'error_message': ' - Error en el usuari o password'})

    else:
        return render(request, 'register.html', {'userForm': UserForm(), 'authorForm': AuthorForm()})

def login_author(request):
    if request.method == "POST":
        userForm = AuthenticationForm(data=request.POST)
        if userForm.is_valid():
            username = userForm.cleaned_data.get("username")
            password = userForm.cleaned_data["password"]
            password2 = request.POST["password2"]
           
            if password == password2:
                user = authenticate(username=username,password=password)
                login(request, user)
                return redirect('llistar_tasques')
        return render(request, 'login.html', {'userForm': AuthenticationForm(), 'error_message': 'Usuari no validat'})
    else:
        return render(request, 'login.html', {'userForm': AuthenticationForm()})

def signout(request):
    logout(request)
    return redirect('index')