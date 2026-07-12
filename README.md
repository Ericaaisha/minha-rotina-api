# 🌻 Minha Rotina API

API REST para gerenciamento de tarefas do dia a dia — academia, faculdade, saúde e vida!

Desenvolvida do zero com Python, FastAPI e banco de dados SQLite.

## 🚀 Tecnologias

- Python 3.14
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

## ⚙️ Como rodar

```bash
# 1. Clonei o repositório
git clone https://github.com/Ericaaisha/minha-rotina-api.git
cd minha-rotina-api

# 2. Criei o ambiente virtual
python -m venv venv
venv\Scripts\activate

# 3. Instalei as dependências
pip install -r requisitos.txt

# 4. Rode a API
py -m uvicorn main:app --reload
```

Acesse **http://localhost:8000/docs** para ver a documentação interativa.

## 📌 Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/` | Status da API |
| POST | `/tasks` | Criar tarefa |
| GET | `/tasks` | Listar tarefas |
| GET | `/tasks/{id}` | Buscar por ID |
| PATCH | `/tasks/{id}/concluir` | Concluir tarefa |
| DELETE | `/tasks/{id}` | Deletar tarefa |
| GET | `/stats` | Estatísticas |
