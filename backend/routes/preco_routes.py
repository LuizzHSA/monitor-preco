from flask import Blueprint, request, jsonify
from database.connection import db
from models.produto import Produto
from models.fornecedor import Fornecedor
from models.preco import Preco
from services.preco_service import PrecoService
from utils.date_utils import eh_data_valida

preco_bp = Blueprint('preco', __name__)

@preco_bp.route('', methods=['POST'])
def create_preco():
    data = request.get_json()
    
    if not data or not data.get('produto_id') or not data.get('fornecedor_id') or not data.get('valor'):
        return jsonify({'error': 'produto_id, fornecedor_id e valor são obrigatórios'}), 400
    
    produto = Produto.query.get(data['produto_id'])
    fornecedor = Fornecedor.query.get(data['fornecedor_id'])
    
    if not produto:
        return jsonify({'error': 'Produto não encontrado'}), 404
    if not fornecedor:
        return jsonify({'error': 'Fornecedor não encontrado'}), 404
    
    preco = PrecoService.criar_preco(
        produto_id=data['produto_id'],
        fornecedor_id=data['fornecedor_id'],
        valor=float(data['valor'])
    )
    
    return jsonify(preco.to_dict()), 201

@preco_bp.route('/produto/<int:produto_id>', methods=['GET'])
def get_precos_produto(produto_id):
    produto = Produto.query.get_or_404(produto_id)
    precos = PrecoService.get_precos_by_produto(produto_id)
    return jsonify([preco.to_dict() for preco in precos])

@preco_bp.route('/fornecedor/<int:fornecedor_id>', methods=['GET'])
def get_precos_fornecedor(fornecedor_id):
    fornecedor = Fornecedor.query.get_or_404(fornecedor_id)
    precos = PrecoService.get_precos_by_fornecedor(fornecedor_id)
    return jsonify([preco.to_dict() for preco in precos])

@preco_bp.route('/periodo', methods=['GET'])
def get_precos_periodo():
    produto_id = request.args.get('produto_id', type=int)
    data_inicio = request.args.get('data_inicio')
    data_fim = request.args.get('data_fim')
    
    if not produto_id:
        return jsonify({'error': 'produto_id é obrigatório'}), 400
    
    if data_inicio and not eh_data_valida(data_inicio):
        return jsonify({'error': 'Formato de data inválido. Use YYYY-MM-DD'}), 400
    if data_fim and not eh_data_valida(data_fim):
        return jsonify({'error': 'Formato de data inválido. Use YYYY-MM-DD'}), 400
    
    from datetime import datetime
    
    inicio = datetime.strptime(data_inicio, '%Y-%m-%d') if data_inicio else None
    fim = datetime.strptime(data_fim, '%Y-%m-%d') if data_fim else None
    
    precos = PrecoService.get_precos_por_periodo(produto_id, inicio, fim)
    return jsonify([preco.to_dict() for preco in precos])

@preco_bp.route('/mes/<int:produto_id>', methods=['GET'])
def get_precos_mes(produto_id):
    produto = Produto.query.get_or_404(produto_id)
    precos = PrecoService.get_precos_do_mes(produto_id)
    return jsonify([preco.to_dict() for preco in precos])

@preco_bp.route('/variacao/<int:produto_id>', methods=['GET'])
def get_variacao(produto_id):
    produto = Produto.query.get_or_404(produto_id)
    dias = request.args.get('dias', default=30, type=int)
    
    variacao = PrecoService.get_maior_variacao(produto_id, dias)
    
    if variacao:
        return jsonify(variacao)
    else:
        return jsonify({'message': 'Não há dados suficientes para calcular variação'}), 404