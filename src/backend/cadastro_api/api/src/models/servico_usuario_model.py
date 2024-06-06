from src import db
import uuid

class Servicos_Usuarios(db.Model):

    __tablename__ = 'servicos_usuarios'

    id = db.Column( db.String(36), primary_key=True, default=str(uuid.uuid4()) )
    id_servico = db.Column( db.String(36), db.ForeignKey('servicos.id'), nullable=False )
    id_usuario = db.Column( db.String(36),db.ForeignKey('usuarios.id'), nullable=False, unique = True )

    servico = db.relationship('Servicos', backref='servicos_usuarios')
    usuario = db.relationship('Usuarios', backref='enderecos_usuarios')