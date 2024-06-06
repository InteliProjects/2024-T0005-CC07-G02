from src import db
import uuid

class Planos(db.Model):
  
  __tablename__ = "planos"
  
  id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
  nome_do_plano = db.Column(db.String(50), nullable=False)
  descricao = db.Column(db.String(255), nullable=False)
  valor = db.Column(db.Numeric(10,2), nullable=False)
  velocidade_contratada = db.Column(db.Integer, nullable=False)
  
  def __init__(self, nome_do_plano, descricao,  valor, velocidade_contratada):
    self.nome_do_plano = nome_do_plano
    self.descricao = descricao
    self.valor = valor
    self.velocidade_contratada = velocidade_contratada
  
  def __repr__(self):
    return f"Nome do plano: {self.nome_do_plano}, Preço: {self.valor}"

  def save(self):
    """
    Salva o objeto no banco de dados
    """
    db.session.add(self)
    db.session.commit()
    
  def update(self, nome_do_plano=None, descricao=None, valor=None, velocidade_contratada=None):
    """
    Atualiza o objeto no banco de dados
    """
    if nome_do_plano is not None:
      self.nome_do_plano = nome_do_plano
    if descricao is not None:
      self.descricao = descricao
    if valor is not None:
      self.valor = valor
    if velocidade_contratada is not None:
      self.velocidade_contratada = velocidade_contratada
    
    db.session.commit()
  
  def delete(self):
    """
    Deleta o objeto do banco de dados
    """
    db.session.delete(self)
    db.session.commit()