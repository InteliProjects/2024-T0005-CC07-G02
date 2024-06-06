from src import db
import uuid

class Usuarios(db.Model):

    __tablename__ = 'usuarios'

    id = db.Column( db.String(36), primary_key=True, default=str(uuid.uuid4()) )
    nome = db.Column( db.String(255), nullable=False )
    email = db.Column( db.String(255), nullable=False, unique=True )
    senha = db.Column( db.String(255), nullable=False )
    
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
    
    def __repr__(self):
        return f"Nome: {self.nome}, Email: {self.email}"
    
    def save(self):
        """
        Salva o objeto no banco de dados
        """
        db.session.add(self)
        db.session.commit()
        
    def update(self, nome_do_plano=None, descricao=None, valor=None):
        """
        Atualiza o objeto no banco de dados
        """
        if nome_do_plano is not None:
            self.nome_do_plano = nome_do_plano
        if descricao is not None:
            self.descricao = descricao
        if valor is not None:
            self.valor = valor
        
        db.session.commit()
    
    def delete(self):
        """
        Deleta o objeto do banco de dados
        """
        db.session.delete(self)
        db.session.commit()