from django.urls import path
from .views import list_tasks
urlpatterns = [
    path('', list_tasks, name='list_tasks'),
    # path('agregar/', views.agregar_libro, name='agregar_libro'),
    # path('editar/<int:id>/', views.editar_libro,
    # name='editar_libro'),
    # path('eliminar/<int:id>/', views.eliminar_libro,
    # name='eliminar_libro'),
]