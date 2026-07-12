from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TaskCreate(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    prioridade: str = "media"
    categoria: str = "geral"


class TaskUpdate(BaseModel):
    titulo: Optional[str] = None
    descricao: Optional[str] = None
    concluida: Optional[bool] = None
    prioridade: Optional[str] = None
    categoria: Optional[str] = None


class TaskResponse(BaseModel):
    id: int
    titulo: str
    descricao: Optional[str] = None
    concluida: bool
    prioridade: str
    categoria: str
    criada_em: datetime
    atualizada_em: Optional[datetime] = None

    class Config:
        from_attributes = True


class TaskStats(BaseModel):
    total: int
    concluidas: int
    pendentes: int
    alta_prioridade: int