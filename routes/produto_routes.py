from flask import Blueprint, request
from controllers.produto_controllers import create_produto

produto_routes = Blueprint('produto_routes', __name__)

@produto_routes.route('/Produto', methods=['POST'])
def produtos_post():
    produto_data = request.json
    return create_produto(request.json)

