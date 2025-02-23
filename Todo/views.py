from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import Task, Category, Author
from .forms import TaskForm, AuthorForm, UserForm, CategoryForm

# def show_index_page(request):
#     '''
#     Renderitza la pàgina principal
#     '''
#     user = request.user

#     return render(request, 'index.html', { 'title': "Aplicació To-Do", 'user': user})

@login_required
def list_tasks(request):
    '''
    Renderitza la pàgina de llistar tasues
    '''
    user = request.user
    author = Author.objects.get(user=user)
    tasks = Task.objects.filter(author=author)
    categories = Category.objects.all()
    return render(request, 'list_tasks.html', {'user': user, 'tasks': tasks, 'categories': categories, 'user': user})

def add_task(request):
    '''
    Afegir tasca
    '''
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            title = request.POST.get('title')
            author_id = request.POST.get('user_id')
            categories_ids = request.POST.getlist('categories_ids')

            author = Author.objects.get(id=author_id)
            categories = Category.objects.filter(id__in=categories_ids)

            task = Task.objects.create(
                title=title,
                author=author,
                completed=False,
            )
            task.categories.set(categories)

            task.save()
            return redirect('llistar_tasques')
        else:
            return redirect('llistar_tasques')

    else:
        return TaskForm()

def edit_task(request, task_id):
    '''
    Editar tasca
    '''
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
        task.categories.set(categories)

        task.save()

        return redirect('llistar_tasques')

def delete_task(_, id):
    '''
    Eliminar tasca
    '''
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('llistar_tasques')

# ########### CATEGORIA #####################

def manage_categories(request):
    '''
    CRUD de categories
    '''
    categories = Category.objects.all()
    form = CategoryForm()

    # Cuando se crea una nueva categoría
    if request.method == 'POST' and 'afegir' in request.POST:
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_categories')

    # Cuando se edita una categoría
    if request.method == 'POST' and 'edit' in request.POST:
        category_id = request.POST.get('category_id')
        category = get_object_or_404(Category, id=category_id)
        form = CategoryForm(instance=category)
        return render(request, 'manage_categories.html', {'form': form, 'categories': categories, 'editing': True, 'category': category})

    # # Cuando se actualiza una categoría (guardando cambios)
    if request.method == 'POST' and 'update' in request.POST:
        category_id = request.POST.get('category_id')
        category = get_object_or_404(Category, id=category_id)
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('manage_categories')

    # Cuando se elimina una categoría
    if request.method == 'POST' and 'delete' in request.POST:
        category_id = request.POST.get('category_id')
        category = get_object_or_404(Category, id=category_id)
        category.delete()
        return redirect('manage_categories')

    return render(request, 'manage_categories.html', {'form': form, 'categories': categories})


# ########### AUTHOR #####################

def show_register_page(request):
    '''
    Vista de registrar un usuari
    '''
    authorForm = AuthorForm()
    userForm = UserForm()
    return render(request, 'register.html', {'userForm': userForm, 'authorForm': authorForm})


def register_author(request):
    '''
    Acció de registrar un usuari
    '''
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
            return redirect('login_author')

        elif not authorForm.is_valid():
            return render(request, 'register.html', {'userForm': UserForm(), 'authorForm': AuthorForm(), 'error_message': ' - DNI incorrect, ha de tenir 8 números i 1 lletra'})

        else:
            return render(request, 'register.html', {'userForm': UserForm(), 'authorForm': AuthorForm(), 'error_message': ' - Error en el usuari o password'})

    else:
        return render(request, 'register.html', {'userForm': UserForm(), 'authorForm': AuthorForm()})

def login_author(request):
    '''
    Vista y acció d'inici de sessió del usuari
    '''
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
    '''
    Acció de tancar sessió d'usuari
    '''
    logout(request)
    return redirect('index')