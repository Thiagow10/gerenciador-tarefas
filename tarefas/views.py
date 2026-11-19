from django.db import connection
from django.shortcuts import render, redirect, get_object_or_404

from .forms import TarefaForm
from .models import Tarefa


def lista_tarefas(request):
    tarefas = Tarefa.objects.all()

    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT COUNT(*),
                   COALESCE(SUM(CASE WHEN concluida THEN 1 ELSE 0 END), 0)
            FROM tarefas_tarefa
            """
        )
        total, concluidas = cursor.fetchone()

    contexto = {
        "tarefas": tarefas,
        "total": total,
        "concluidas": concluidas,
        "pendentes": total - concluidas,
    }
    return render(request, "tarefas/lista.html", contexto)


def criar_tarefa(request):
    form = TarefaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("lista_tarefas")
    return render(request, "tarefas/form.html", {"form": form, "titulo": "Nova tarefa"})


def editar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    form = TarefaForm(request.POST or None, instance=tarefa)
    if form.is_valid():
        form.save()
        return redirect("lista_tarefas")
    return render(request, "tarefas/form.html", {"form": form, "titulo": "Editar tarefa"})


def alternar_conclusao(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == "POST":
        tarefa.concluida = not tarefa.concluida
        tarefa.save()
    return redirect("lista_tarefas")


def excluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == "POST":
        tarefa.delete()
        return redirect("lista_tarefas")
    return render(request, "tarefas/confirmar_exclusao.html", {"tarefa": tarefa})
