from database.connection import db
from datetime import datetime

class Alerta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)
    preco_id = db.Column(db.Integer, db.ForeignKey('preco.id'), nullable=False)
    mensagem = db.Column(db.Text, nullable=False)
    data_alerta = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    lido = db.Column(db.Boolean, default=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'produto_id': self.produto_id,
            'preco_id': self.preco_id,
            'mensagem': self.mensagem,
            'data_alerta': self.data_alerta.isoformat() if self.data_alerta else None,
            'lido': self.lido,
            'produto_nome': self.produto.nome if self.produto else None,
            'preco_valor': self.preco.valor if self.preco else None
        }
    
    def __repr__(self):
        return f'<Alerta {self.mensagem}>'