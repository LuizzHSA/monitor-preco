from database.connection import db
from models.produto import Produto
from models.fornecedor import Fornecedor
from models.preco import Preco
from models.alerta import Alerta
from services.preco_service import PrecoService
from datetime import datetime, timedelta

class AlertaService:
    
    @staticmethod
    def criar_alerta(produto_id, preco_id, mensagem):
        alerta = Alerta(
            produto_id=produto_id,
            preco_id=preco_id,
            mensagem=mensagem
        )
        db.session.add(alerta)
        db.session.commit()
        return alerta
    
    @staticmethod
    def verificar_variacoes_preco():
        produtos = Produto.query.all()
        alertas_criados = []
        
        for produto in produtos:
            variacao = PrecoService.get_maior_variacao(produto.id, dias=7)
            if variacao and variacao['max_variacao'] > 0.1:  # 10% de variação
                mensagem = f"Variação significativa no preço do produto '{produto.nome}': R${variacao['max_variacao']:.2f}"
                ultimo_preco = PrecoService.get_ultimo_preco(produto.id)
                
                if ultimo_preco:
                    alerta = AlertaService.criar_alerta(
                        produto_id=produto.id,
                        preco_id=ultimo_preco.id,
                        mensagem=mensagem
                    )
                    alertas_criados.append(alerta)
        
        return alertas_criados
    
    @staticmethod
    def verificar_preco_alto(produto_id, limite_superior):
        ultimo_preco = PrecoService.get_ultimo_preco(produto_id)
        
        if ultimo_preco and ultimo_preco.valor > limite_superior:
            mensagem = f"Preço acima do limite: R${ultimo_preco.valor:.2f} (limite: R${limite_superior:.2f})"
            
            alerta = AlertaService.criar_alerta(
                produto_id=produto_id,
                preco_id=ultimo_preco.id,
                mensagem=mensagem
            )
            return alerta
        
        return None
    
    @staticmethod
    def verificar_preco_baixo(produto_id, limite_inferior):
        ultimo_preco = PrecoService.get_ultimo_preco(produto_id)
        
        if ultimo_preco and ultimo_preco.valor < limite_inferior:
            mensagem = f"Preço abaixo do limite: R${ultimo_preco.valor:.2f} (limite: R${limite_inferior:.2f})"
            
            alerta = AlertaService.criar_alerta(
                produto_id=produto_id,
                preco_id=ultimo_preco.id,
                mensagem=mensagem
            )
            return alerta
        
        return None
    
    @staticmethod
    def get_alertas_nao_lidos():
        return Alerta.query.filter_by(lido=False).order_by(Alerta.data_alerta.desc()).all()
    
    @staticmethod
    def marcar_alerta_como_lido(alerta_id):
        alerta = Alerta.query.get(alerta_id)
        if alerta:
            alerta.lido = True
            db.session.commit()
        return alerta
    
    @staticmethod
    def get_alertas_por_produto(produto_id):
        return Alerta.query.filter_by(produto_id=produto_id).order_by(Alerta.data_alerta.desc()).all()