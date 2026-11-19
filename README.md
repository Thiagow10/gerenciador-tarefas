# 📝 Gerenciador de Tarefas

Aplicação web simples para cadastrar, editar, concluir e excluir tarefas do dia a dia (CRUD).

## Sobre o projeto
Projeto de nível iniciante criado para praticar os fundamentos de desenvolvimento web com Python.
A finalidade é ajudar o usuário a organizar suas atividades, separando o que está **pendente**
do que já foi **concluído**, com prioridade (baixa, média ou alta) em cada tarefa.

## Tecnologias
- **Python 3** – linguagem principal
- **Django** – framework web (models, views, templates, forms, admin)
- **SQL / SQLite** – banco de dados; o projeto usa o ORM do Django e também uma consulta SQL pura
  (veja `tarefas/views.py` e o arquivo `consultas.sql`)

## Funcionalidades
- Criar, listar, editar e excluir tarefas
- Marcar como concluída / reabrir
- Prioridade (Baixa, Média, Alta)
- Painel com total, pendentes e concluídas (calculado com SQL puro)
- Painel administrativo do Django (`/admin`)

## Como executar
```bash
# 1. Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Crie as tabelas no banco de dados
python manage.py makemigrations tarefas
python manage.py migrate

# 4. (Opcional) Crie um superusuário para acessar o /admin
python manage.py createsuperuser

# 5. Rode o servidor
python manage.py runserver
```
Acesse: http://127.0.0.1:8000

## Estrutura
```
config/      -> configurações do projeto
tarefas/     -> app principal (models, views, forms, urls, templates)
consultas.sql -> exemplos de SQL usados no projeto
```

## Ideias para evoluir
- Login de usuários (cada um com suas tarefas)
- Filtro por prioridade e busca
- Data limite para as tarefas
- Testes automatizados
