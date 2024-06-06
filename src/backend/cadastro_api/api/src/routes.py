from flask import Blueprint
from src.controllers.auth_controller import auth_blueprint
from src.controllers.endereco_controller import endereco_blueprint
from src.controllers.servicos_controller import servicos_blueprint
from src.controllers.servico_usuario_controller import servico_usuario_blueprint
from src.controllers.endereco_usuario_controller import endereco_usuario_blueprint

api = Blueprint('api', __name__)

api.register_blueprint(auth_blueprint, url_prefix='/auth')
api.register_blueprint(endereco_blueprint, url_prefix='/endereco')
api.register_blueprint(servicos_blueprint, url_prefix='/servicos')
api.register_blueprint(servico_usuario_blueprint, url_prefix='/servico_usuario')
api.register_blueprint(endereco_usuario_blueprint, url_prefix='/endereco_usuario')

