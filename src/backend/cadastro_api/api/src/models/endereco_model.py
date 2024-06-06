from src import db
import uuid

class Enderecos(db.Model):

    __tablename__ = 'enderecos'

    id = db.Column( db.String(36), primary_key=True, default=str(uuid.uuid4()) )
    nome_endereco = db.Column( db.String(255), nullable=False, unique = True )
