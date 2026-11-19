from django.db import models


class Tarefa(models.Model):
    PRIORIDADES = [
        ("B", "Baixa"),
        ("M", "Média"),
        ("A", "Alta"),
    ]

    titulo = models.CharField("Título", max_length=100)
    descricao = models.TextField("Descrição", blank=True)
    prioridade = models.CharField(max_length=1, choices=PRIORIDADES, default="M")
    concluida = models.BooleanField("Concluída", default=False)
    criada_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["concluida", "-criada_em"]

    def __str__(self):
        return self.titulo
