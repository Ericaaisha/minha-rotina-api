from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from banco import engine, get_db, Base
import estrutura as models
import contrato as schemas

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="🌻 Minha Rotina API",
    description="Minhas tarefas do dia a dia — academia, faculdade, vida!",
    version="1.0.0",
)


@app.get("/")
def root():
    return {"mensagem": "Minha Rotina API rodando!"}


@app.post("/tasks", response_model=schemas.TaskResponse, status_code=201)
def criar_tarefa(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    nova_tarefa = models.Task(**task.dict())
    db.add(nova_tarefa)
    db.commit()
    db.refresh(nova_tarefa)
    return nova_tarefa


@app.get("/tasks", response_model=List[schemas.TaskResponse])
def listar_tarefas(
    concluida: Optional[bool] = Query(None),
    prioridade: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(models.Task)
    if concluida is not None:
        query = query.filter(models.Task.concluida == concluida)
    if prioridade is not None:
        query = query.filter(models.Task.prioridade == prioridade)
    return query.order_by(models.Task.criada_em.desc()).all()


@app.get("/tasks/{task_id}", response_model=schemas.TaskResponse)
def buscar_tarefa(task_id: int, db: Session = Depends(get_db)):
    tarefa = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada.")
    return tarefa


@app.patch("/tasks/{task_id}/concluir", response_model=schemas.TaskResponse)
def concluir_tarefa(task_id: int, db: Session = Depends(get_db)):
    tarefa = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada.")
    tarefa.concluida = True
    db.commit()
    db.refresh(tarefa)
    return tarefa


@app.delete("/tasks/{task_id}", status_code=204)
def deletar_tarefa(task_id: int, db: Session = Depends(get_db)):
    tarefa = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada.")
    db.delete(tarefa)
    db.commit()
    return None


@app.get("/stats", response_model=schemas.TaskStats)
def estatisticas(db: Session = Depends(get_db)):
    total = db.query(models.Task).count()
    concluidas = db.query(models.Task).filter(models.Task.concluida == True).count()
    alta = db.query(models.Task).filter(models.Task.prioridade == "alta").count()
    return schemas.TaskStats(
        total=total,
        concluidas=concluidas,
        pendentes=total - concluidas,
        alta_prioridade=alta,
    )