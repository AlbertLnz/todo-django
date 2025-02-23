from django.urls import path
from .views import list_tasks, add_task, edit_task, delete_task, register_author, login_author, signout, manage_categories
from .views_cbv import IndexPageView

from rest_framework import routers
from .api import CategoryViewSet, AuthorViewSet, TaskViewSet

urlpatterns = [
    # path('', show_index_page, name='index'),
    path('', IndexPageView.as_view(), name='index'),
    path('list/', list_tasks, name='llistar_tasques'),
    path('agregar/', add_task, name='afegir_task'),
    path('editar/<int:task_id>/', edit_task, name= 'editar_task'),
    path('eliminar/<int:id>/', delete_task, name='eliminar_task'),
    # path('index/<str:user>/', show_index_page, name='index'),
    path('index/<str:user>/', IndexPageView.as_view(), name='index'),
    path('register/', register_author, name='register_author'),
    path('login/', login_author, name="login_author"),
    path('signout/', signout, name='signout'),
    path('manage-categories/', manage_categories, name='manage_categories'),
]

router = routers.DefaultRouter()
router.register('api/categories', CategoryViewSet, 'category') # == (url, viewSet, name)
router.register('api/authors', AuthorViewSet, 'author') # == (url, viewSet, name)
router.register('api/tasks', TaskViewSet, 'task') # == (url, viewSet, name)

urlpatterns += router.urls
