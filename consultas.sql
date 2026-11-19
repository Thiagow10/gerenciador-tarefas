
SELECT id, titulo, prioridade, concluida, criada_em
FROM tarefas_tarefa
ORDER BY concluida ASC, criada_em DESC;


SELECT titulo, criada_em
FROM tarefas_tarefa
WHERE concluida = 0 AND prioridade = 'A';


SELECT prioridade, COUNT(*) AS quantidade
FROM tarefas_tarefa
GROUP BY prioridade;


INSERT INTO tarefas_tarefa (titulo, descricao, prioridade, concluida, criada_em)
VALUES ('Estudar Django', 'Ver a documentação oficial', 'A', 0, datetime('now'));


UPDATE tarefas_tarefa SET concluida = 1 WHERE id = 1;


DELETE FROM tarefas_tarefa WHERE id = 1;
