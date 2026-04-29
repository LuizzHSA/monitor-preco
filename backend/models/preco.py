from database.connection import db
from datetime import datetime

class Preco(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)
    fornecedor_id = db.Column(db.Integer, db.ForeignKey('fornecedor.id'), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    data_coleta = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    alertas = db.relationship('Alerta', backref='preco', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'produto_id': self.produto_id,
            'fornecedor_id': self.fornecedor_id,
            'valor': self.valor,
            'data_coleta': self.data_coleta.isoformat() if self.data_coleta else None,
            'produto_nome': self.produto.nome if self.produto else None,
            'fornecedor_nome': self.fornecedor.nome if self.fornecedor else None
        }
    
    def __repr__(self):
        return f'<Preco {self.valor} - Produto {self.produto_id}>'