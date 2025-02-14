from django.urls import path
from .views import show_index_page, list_tasks, add_task, edit_task, delete_task

urlpatterns = [
    path('', show_index_page, name='index'),
    path('list/', list_tasks, name='llistar_tasques'),
    path('agregar/', add_task, name='afegir_task'),
    path('editar/<int:task_id>/', edit_task, name= 'editar_task'),
    path('eliminar/<int:id>/', delete_task, name='eliminar_task'),
]