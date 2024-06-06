from src import db
import uuid

class Enderecos_Usuarios(db.Model):

    __tablename__ = 'enderecos_usuarios'

    id = db.Column( db.String(36), primary_key=True, default=str(uuid.uuid4()) )
    id_endereco = db.Column( db.String(36), db.ForeignKey('endereco.id'), nullable=False )
    id_usuario = db.Column( db.String(36),db.ForeignKey('usuario.id'), nullable=False, unique = True )

    endereco = db.relationship('Enderecos', backref='enderecos_usuarios')
    usuario = db.relationship('Usuarios', backref='enderecos_usuarios')