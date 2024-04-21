import sqlalchemy as sqlal
import sqlalchemy.orm as sqlorm
from app import db

class Candidato(db.Model):
    id: sqlorm.Mapped[int] = sqlorm.mapped_column(primary_key=True)
    candidato: sqlorm.Mapped[str] = sqlorm.mapped_column(sqlal.String(64), index=True, 
                                                         unique=True)
    email: sqlorm.Mapped[str] = sqlorm.mapped_column(sqlal.String(120), index=True,
                                                     unique=True)
    contato: sqlorm.Mapped[int] = sqlorm.mapped_column(sqlal.Integer(), index=False,
                                                       unique=True)
    
    # preencher com mais colunas, atributos, campos...

    def __repr__(self):
        return '<Candidato {}>'.format(self.candidato)
    