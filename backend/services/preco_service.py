from database.connection import db
from models.produto import Produto
from models.fornecedor import Fornecedor
from models.preco import Preco
from models.alerta import Alerta
from utils.date_utils import get_data_inicio_mes, get_data_fim_mes
from datetime import datetime, timedelta

class PrecoService:
    
    @staticmethod
    def criar_preco(produto_id, fornecedor_id, valor):
        preco = Preco(
            produto_id=produto_id,
            fornecedor_id=fornecedor_id,
            valor=valor,
            data_coleta=datetime.utcnow()
        )
        db.session.add(preco)
        db.session.commit()
        return preco
    
    @staticmethod
    def get_precos_by_produto(produto_id):
        return Preco.query.filter_by(produto_id=produto_id).order_by(Preco.data_coleta.desc()).all()
    
    @staticmethod
    def get_precos_by_fornecedor(fornecedor_id):
        return Preco.query.filter_by(fornecedor_id=fornecedor_id).order_by(Preco.data_coleta.desc()).all()
    
    @staticmethod
    def get_ultimo_preco(produto_id, fornecedor_id):
        return Preco.query.filter_by(
            produto_id=produto_id,
            fornecedor_id=fornecedor_id
        ).order_by(Preco.data_coleta.desc()).first()
    
    @staticmethod
    def get_precos_por_periodo(produto_id, data_inicio=None, data_fim=None):
        query = Preco.query.filter_by(produto_id=produto_id)
        
        if data_inicio:
            query = query.filter(Preco.data_coleta >= data_inicio)
        if data_fim:
            query = query.filter(Preco.data_coleta <= data_fim)
            
        return query.order_by(Preco.data_coleta.desc()).all()
    
    @staticmethod
    def get_precos_do_mes(produto_id):
        data_inicio = get_data_inicio_mes()
        data_fim = get_data_fim_mes()
        return PrecoService.get_precos_por_periodo(produto_id, data_inicio, data_fim)
    
    @staticmethod
    def get_maior_variacao(produto_id, dias=30):
        data_limite = datetime.utcnow() - timedelta(days=dias)
        
        precos = Preco.query.filter(
            Preco.produto_id == produto_id,
            Preco.data_coleta >= data_limite
        ).order_by(Preco.data_coleta.asc()).all()
        
        if len(precos) < 2:
            return None
            
        valores = [preco.valor for preco in precos]
        max_variacao = max(valores) - min(valores)
        
        return {
            'max_variacao': max_variacao,
            'preco_maximo': max(valores),
            'preco_minimo': min(valores),
            'data_inicio': precos[0].data_coleta,
            'data_fim': precos[-1].data_coleta
        }