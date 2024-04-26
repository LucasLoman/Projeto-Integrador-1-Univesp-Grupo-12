from typing import Optional
import sqlalchemy as sqla
import sqlalchemy.orm as sqlorm
from app import db

class Candidato(db.Model):
    id: sqlorm.Mapped[int] = sqlorm.mapped_column(primary_key=True)
    nome: sqlorm.Mapped[str] = sqlorm.mapped_column(sqla.String(64), index=True, unique=True)
    email: sqlorm.Mapped[str] = sqlorm.mapped_column(sqla.String(64), index=False, unique=False)
    telefone: sqlorm.Mapped[int] = sqlorm.mapped_column(sqla.Integer(), index=False, unique=False)
    endereco: sqlorm.Mapped[str] = sqlorm.mapped_column(sqla.String(120), index=False, unique=False)
    objetivo: sqlorm.Mapped[str] = sqlorm.mapped_column(sqla.String(256), index=False, unique=False)
    formacao: sqlorm.Mapped[str] = sqlorm.mapped_column(sqla.String(256), index=False, unique=False)
    experiencia: sqlorm.Mapped[str] = sqlorm.mapped_column(sqla.String(256), index=False, unique=False)

    