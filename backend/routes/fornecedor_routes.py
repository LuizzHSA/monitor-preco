from flask import Blueprint, request, jsonify
from database.connection import db
from models.fornecedor import Fornecedor

fornecedor_bp = Blueprint('fornecedor', __name__)

@fornecedor_bp.route('', methods=['GET'])
def get_fornecedores():
    fornecedores = Fornecedor.query.all()
    return jsonify([fornecedor.to_dict() for fornecedor in fornecedores])

@fornecedor_bp.route('', methods=['POST'])
def create_fornecedor():
    data = request.get_json()
    
    if not data or not data.get('nome') or not data.get('cnpj'):
        return jsonify({'error': 'Nome e CNPJ do fornecedor são obrigatórios'}), 400
    
    if Fornecedor.query.filter_by(cnpj=data['cnpj']).first():
        return jsonify({'error': 'Fornecedor com este CNPJ já existe'}), 400
    
    fornecedor = Fornecedor(
        nome=data['nome'],
        cnpj=data['cnpj'],
        contato=data.get('contato')
    )
    
    db.session.add(fornecedor)
    db.session.commit()
    
    return jsonify(fornecedor.to_dict()), 201

@fornecedor_bp.route('/<int:fornecedor_id>', methods=['GET'])
def get_fornecedor(fornecedor_id):
    fornecedor = Fornecedor.query.get_or_404(fornecedor_id)
    return jsonify(fornecedor.to_dict())

@fornecedor_bp.route('/<int:fornecedor_id>', methods=['PUT'])
def update_fornecedor(fornecedor_id):
    fornecedor = Fornecedor.query.get_or_404(fornecedor_id)
    data = request.get_json()
    
    if data.get('nome'):
        fornecedor.nome = data['nome']
    if 'cnpj' in data:
        if Fornecedor.query.filter_by(cnpj=data['cnpj']).first():
            return jsonify({'error': 'Fornecedor com este CNPJ já existe'}), 400
        fornecedor.cnpj = data['cnpj']
    if 'contato' in data:
        fornecedor.contato = data['contato']
    
    db.session.commit()
    return jsonify(fornecedor.to_dict())

@fornecedor_bp.route('/<int:fornecedor_id>', methods=['DELETE'])
def delete_fornecedor(fornecedor_id):
    fornecedor = Fornecedor.query.get_or_404(fornecedor_id)
    db.session.delete(fornecedor)
    db.session.commit()
    
    return jsonify({'message': 'Fornecedor deletado com sucesso'}), 200