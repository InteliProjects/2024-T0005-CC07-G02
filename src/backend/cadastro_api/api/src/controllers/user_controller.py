from flask import Blueprint, request, Response, json
from src.services.users_service import User_Service  

usuarios_blueprint = Blueprint('usuarios', __name__)

@usuarios_blueprint.route('/usuarios', methods=['GET'])
def get_all_usuarios():
    response_data, status_code = User_Service.get_all_users()
    return Response(
        response=json.dumps(response_data),
        status=status_code,
        mimetype='application/json'
    )

@usuarios_blueprint.route('/usuarios/<string:user_id>', methods=['GET'])
def get_usuario_by_id(user_id):
    response_data, status_code = User_Service.get_user_by_id(user_id)
    return Response(
        response=json.dumps(response_data),
        status=status_code,
        mimetype='application/json'
    )

@usuarios_blueprint.route('/usuarios', methods=['POST'])
def create_usuario():
    usuario_data = request.json
    response_data, status_code = User_Service.registro(usuario_data)
    return Response(
        response=json.dumps(response_data),
        status=status_code,
        mimetype='application/json'
    )

@usuarios_blueprint.route('/usuarios/<string:user_id>', methods=['PUT'])
def update_usuario(user_id):
    usuario_data = request.json
    response_data, status_code = User_Service.update_user(user_id, usuario_data)
    return Response(
        response=json.dumps(response_data),
        status=status_code,
        mimetype='application/json'
    )

@usuarios_blueprint.route('/usuarios/<string:user_id>', methods=['DELETE'])
def delete_usuario(user_id):
    response_data, status_code = User_Service.delete_user(user_id)
    return Response(
        response=json.dumps(response_data),
        status=status_code,
        mimetype='application/json'
    )
