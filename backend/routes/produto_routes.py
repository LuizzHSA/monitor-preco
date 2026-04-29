from flask import Blueprint, request, jsonify
from database.connection import db
from models.produto import Produto

produto_bp = Blueprint('produto', __name__)

@produto_bp.route('', methods=['GET'])
def get_produtos():
    produtos = Produto.query.all()
    return jsonify([produto.to_dict() for produto in produtos])

@produto_bp.route('', methods=['POST'])
def create_produto():
    data = request.get_json()
    
    if not data or not data.get('nome'):
        return jsonify({'error': 'Nome do produto é obrigatório'}), 400
    
    produto = Produto(
        nome=data['nome'],
        descricao=data.get('descricao'),
        categoria=data.get('categoria')
    )
    
    db.session.add(produto)
    db.session.commit()
    
    return jsonify(produto.to_dict()), 201

@produto_bp.route('/<int:produto_id>', methods=['GET'])
def get_produto(produto_id):
    produto = Produto.query.get_or_404(produto_id)
    return jsonify(produto.to_dict())

@produto_bp.route('/<int:produto_id>', methods=['PUT'])
def update_produto(produto_id):
    produto = Produto.query.get_or_404(produto_id)
    data = request.get_json()
    
    if data.get('nome'):
        produto.nome = data['nome']
    if 'descricao' in data:
        produto.descricao = data['descricao']
    if 'categoria' in data:
        produto.categoria = data['categoria']
    
    db.session.commit()
    return jsonify(produto.to_dict())

@produto_bp.route('/<int:produto_id>', methods=['DELETE'])
def delete_produto(produto_id):
    produto = Produto.query.get_or_404(produto_id)
    db.session.delete(produto)
    db.session.commit()
    
    return jsonify({'message': 'Produto deletado com sucesso'}), 200