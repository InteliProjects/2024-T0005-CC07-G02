from src import db
import uuid
from datetime import date

class Fatura(db.Model):
  
    __tablename__ = "faturas"
  
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    id_cliente = db.Column(db.String(36), nullable=False)
    data_pagamento = db.Column(db.Date, nullable=True)  # Data de pagamento (None se não pago)
    pago = db.Column(db.Boolean, default=False, nullable=False)
    itens = db.relationship("ItemFatura", backref="fatura", lazy=True)
  
    def __init__(self, id_cliente, data_pagamento=None, pago=False):
        self.id_cliente = id_cliente
        self.data_pagamento = data_pagamento
        self.pago = pago
  
    def __repr__(self):
        return f"Fatura(id={self.id}, id_cliente={self.id_cliente}, pago={self.pago})"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data_pagamento=None, pago=None):
        if data_pagamento is not None:
            self.data_pagamento = data_pagamento
        if pago is not None:
            self.pago = pago
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'id_cliente': self.id_cliente,
            'data_pagamento': self.data_pagamento.isoformat() if self.data_pagamento else None,
            'pago': self.pago,
            # Assuming you want to include items as well
            'itens': [item.to_dict() for item in self.itens] if self.itens else []
        }

class ItemFatura(db.Model):
  
    __tablename__ = "itens_fatura"
  
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    id_fatura = db.Column(db.String(36), db.ForeignKey('faturas.id'), nullable=False)
    id_produto = db.Column(db.String(36), nullable=False)
    valor = db.Column(db.Float, nullable=False)
  
    def __init__(self, id_fatura, id_produto, valor):
        self.id_fatura = id_fatura
        self.id_produto = id_produto
        self.valor = valor
  
    def __repr__(self):
        return f"ItemFatura(id={self.id}, id_fatura={self.id_fatura}, id_produto={self.id_produto}, valor={self.valor})"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'id_fatura': self.id_fatura,
            'id_produto': self.id_produto,
            'valor': self.valor
        }