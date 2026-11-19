-- Consultas SQL equivalentes ao que o Django faz por baixo dos panos.
-- Para testar: python manage.py dbshell   (ou use o DB Browser for SQLite)

-- 1) Listar todas as tarefas (pendentes primeiro, mais recentes antes)
SELECT id, titulo, prioridade, concluida, criada_em
FROM tarefas_tarefa
ORDER BY concluida ASC, criada_em DESC;

-- 2) Listar apenas as tarefas pendentes de prioridade alta
SELECT titulo, criada_em
FROM tarefas_tarefa
WHERE concluida = 0 AND prioridade = 'A';

-- 3) Contar tarefas por prioridade
SELECT prioridade, COUNT(*) AS quantidade
FROM tarefas_tarefa
GROUP BY prioridade;

-- 4) Inserir uma tarefa manualmente
INSERT INTO tarefas_tarefa (titulo, descricao, prioridade, concluida, criada_em)
VALUES ('Estudar Django', 'Ver a documentação oficial', 'A', 0, datetime('now'));

-- 5) Marcar uma tarefa como concluída
UPDATE tarefas_tarefa SET concluida = 1 WHERE id = 1;

-- 6) Excluir uma tarefa
DELETE FROM tarefas_tarefa WHERE id = 1;
