from flask import Blueprint
from src.controllers.fatura_controller import fatura_blueprint
from src.middlewares.auth_middleware import Auth_Middleware
from src import app

# Main blueprint to be registered in the app
api = Blueprint("api", __name__)

auth_middleware = Auth_Middleware(app)

# Register the blueprints with the main API blueprint
api.register_blueprint(fatura_blueprint, url_prefix="/fatura")


@api.before_app_request
def before_request():
    return auth_middleware.before_request()