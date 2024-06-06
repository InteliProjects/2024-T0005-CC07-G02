from flask import Blueprint
from src.controllers.planos_controller import planos_blueprint
from src.controllers.servicos_contratados_controller import servicos_contratados_blueprint
from src.middlewares.auth_middleware import Auth_Middleware
from src import app

# Main blueprint to be registered in the app
api = Blueprint("api", __name__)

auth_middleware = Auth_Middleware(app)

# Register the blueprints with the main API blueprint
api.register_blueprint(planos_blueprint, url_prefix="/plans")
api.register_blueprint(servicos_contratados_blueprint, url_prefix="/services")

@api.before_app_request
def before_request():
    return auth_middleware.before_request()
