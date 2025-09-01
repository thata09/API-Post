from db import db

class Produto(db.Model):
    _tablename__ = 'produtos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    categoria = db.Column(db.String(80), nullable=False)
    preco = db.Column(db.Integer, nullable=False)

    def json(self):
        return {
            'id': self.id,
            'modelo': self.modelo,
            'marca': self.marca,
            'ano': self.ano
        }