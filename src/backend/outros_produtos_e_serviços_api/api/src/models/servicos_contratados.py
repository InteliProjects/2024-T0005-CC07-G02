from src import db
import uuid

class Servicos_Contratados(db.Model):
  
  __tablename__ = "servicos_contratados"
  
  id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
  id_cliente = db.Column(db.String(36), nullable=False)
  id_plano = db.Column(db.String(36), db.ForeignKey('planos.id'), nullable=False)  # Chave estrangeira
  data_contratacao = db.Column(db.Date, nullable=False)
  data_cancelamento = db.Column(db.Date)
  plano = db.relationship("Planos", backref="servicos_contratados")
  
  def __init__ (self, id_cliente, id_plano, data_contratacao, data_cancelamento=None):
    self.id_cliente = id_cliente
    self.id_plano = id_plano
    self.data_contratacao = data_contratacao
    self.data_cancelamento = data_cancelamento
  
  def __repr__(self):
    return f"id_cliente: {self.id_cliente}, id_plano: {self.id_plano}, data_contratacao: {self.data_contratacao}"

  def save(self):
    """
    Salva o objeto no banco de dados
    """
    db.session.add(self)
    db.session.commit()
    
  def update(self, id_cliente=None, id_plano=None, data_contratacao=None, data_cancelamento=None):
    """
    Atualiza o objeto no banco de dados
    """
    if id_cliente is not None:
      self.id_cliente = id_cliente
    if id_plano is not None:
      self.id_plano = id_plano
    if data_contratacao is not None:
      self.data_contratacao = data_contratacao
    if data_cancelamento is not None:
      self.data_cancelamento = data_cancelamento
    
    db.session.commit()
    
  def delete(self):
    """
    Deleta o objeto do banco de dados
    """
    db.session.delete(self)
    db.session.commit()
