from models.produto_models import Produto
from db import db
import json
from flask import make_response

def create_produto(produto_data):
    novo_produto = Produto(
        nome=produto_data['nome'],
        categoria=produto_data['categoria'],
        preco=produto_data['preco'],
    )
    db.session.add(novo_produto)
    db.session.commit()
    response = make_response(
        json.dumps({
            'mensagem': 'Produto cadastrado com sucesso.',
            'produto': novo_produto.json()
        }, sort_keys=False)
    )
    response.headers['content-Type'] = 'appication/json'
    return response