from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_tarefas, name="lista_tarefas"),
    path("nova/", views.criar_tarefa, name="criar_tarefa"),
    path("<int:pk>/editar/", views.editar_tarefa, name="editar_tarefa"),
    path("<int:pk>/concluir/", views.alternar_conclusao, name="alternar_conclusao"),
    path("<int:pk>/excluir/", views.excluir_tarefa, name="excluir_tarefa"),
]
