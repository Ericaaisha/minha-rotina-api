from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from banco import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=Truee)
    titulo = Column(String(100), nullable=False)
    descricao = Column(String(500), nullable=True)
    concluida = Column(Boolean, default=False)
    prioridade = Column(String(10), default="media")
    categoria = Column(String(20), default="geral")
    criada_em = Column(DateTime, server_default=func.now())
    atualizada_em = Column(DateTime, onupdate=func.now())
