from src import db
import uuid

class Servicos(db.Model):

    __tablename__ = 'servicos'

    id = db.Column( db.String(36), primary_key=True, default=str(uuid.uuid4()) )
    nome_servicos = db.Column( db.String(255), unique = True )
