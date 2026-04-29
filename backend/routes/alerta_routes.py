from flask import Blueprint, request, jsonify
from database.connection import db
from models.produto import Produto
from models.fornecedor import Fornecedor
from models.preco import Preco
from models.alerta import Alerta
from services.alerta_service import AlertaService
from services.preco_service import PrecoService

alerta_bp = Blueprint('alerta', __name__)

@alerta_bp.route('', methods=['GET'])
def get_alertas():
    nao_lidos = request.args.get('nao_lidos', default='false').lower() == 'true'
    
    if nao_lidos:
        alertas = AlertaService.get_alertas_nao_lidos()
    else:
        alertas = Alerta.query.order_by(Alerta.data_alerta.desc()).all()
    
    return jsonify([alerta.to_dict() for alerta in alertas])

@alerta_bp.route('/<int:alerta_id>', methods=['GET'])
def get_alerta(alerta_id):
    alerta = Alerta.query.get_or_404(alerta_id)
    return jsonify(alerta.to_dict())

@alerta_bp.route('/produto/<int:produto_id>', methods=['GET'])
def get_alertas_produto(produto_id):
    alertas = AlertaService.get_alertas_por_produto(produto_id)
    return jsonify([alerta.to_dict() for alerta in alertas])

@alerta_bp.route('/verificar-variacoes', methods=['POST'])
def verificar_variacoes():
    alertas_criados = AlertaService.verificar_variacoes_preco()
    return jsonify({
        'message': f'{len(alertas_criados)} novos alertas criados',
        'alertas': [alerta.to_dict() for alerta in alertas_criados]
    })

@alerta_bp.route('/verificar-preco-alto', methods=['POST'])
def verificar_preco_alto():
    data = request.get_json()
    
    if not data or not data.get('produto_id') or not data.get('limite_superior'):
        return jsonify({'error': 'produto_id e limite_superior são obrigatórios'}), 400
    
    produto = Produto.query.get(data['produto_id'])
    if not produto:
        return jsonify({'error': 'Produto não encontrado'}), 404
    
    alerta = AlertaService.verificar_preco_alto(
        produto_id=data['produto_id'],
        limite_superior=float(data['limite_superior'])
    )
    
    if alerta:
        return jsonify(alerta.to_dict())
    else:
        return jsonify({'message': 'Nenhum alerta criado - preço dentro do limite'}), 200

@alerta_bp.route('/verificar-preco-baixo', methods=['POST'])
def verificar_preco_baixo():
    data = request.get_json()
    
    if not data or not data.get('produto_id') or not data.get('limite_inferior'):
        return jsonify({'error': 'produto_id e limite_inferior são obrigatórios'}), 400
    
    produto = Produto.query.get(data['produto_id'])
    if not produto:
        return jsonify({'error': 'Produto não encontrado'}), 404
    
    alerta = AlertaService.verificar_preco_baixo(
        produto_id=data['produto_id'],
        limite_inferior=float(data['limite_inferior'])
    )
    
    if alerta:
        return jsonify(alerta.to_dict())
    else:
        return jsonify({'message': 'Nenhum alerta criado - preço dentro do limite'}), 200

@alerta_bp.route('/<int:alerta_id>/marcar-lido', methods=['PUT'])
def marcar_lido(alerta_id):
    alerta = AlertaService.marcar_alerta_como_lido(alerta_id)
    if alerta:
        return jsonify(alerta.to_dict())
    else:
        return jsonify({'error': 'Alerta não encontrado'}), 404

@alerta_bp.route('<int:alerta_id>', methods=['DELETE'])
def delete_alerta(alerta_id):
    alerta = Alerta.query.get_or_404(alerta_id)
    db.session.delete(alerta)
    db.session.commit()
    
    return jsonify({'message': 'Alerta deletado com sucesso'}), 200