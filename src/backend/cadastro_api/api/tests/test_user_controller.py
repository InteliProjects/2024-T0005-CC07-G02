# test_user_controller.py
import sys
from pathlib import Path

# Adicione o diretório src ao sys.path
sys.path.append(str(Path(__file__).resolve().parents[2] / 'src'))

import pytest
from flask import Flask, json
from src.controllers.user_controller import usuarios_blueprint
from unittest.mock import patch, MagicMock

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(usuarios_blueprint)
    return app.test_client()

# Teste para GET /usuarios
@patch('src.services.users_service.User_Service.get_all_users')
def test_get_all_usuarios(mock_get_all_users, app):
    mock_users = [
        {'id': 1, 'nome': 'Test User 1'},
        {'id': 2, 'nome': 'Test User 2'}
    ]
    mock_get_all_users.return_value = (mock_users, 200)
    
    response = app.get('/usuarios')
    
    assert response.status_code == 200
    assert json.loads(response.data) == mock_users
    mock_get_all_users.assert_called_once()

# Teste para GET /usuarios/<user_id>
@patch('src.services.users_service.User_Service.get_user_by_id')
def test_get_usuario_by_id(mock_get_user_by_id, app):
    mock_user = {'id': 1, 'nome': 'Test User 1'}
    mock_get_user_by_id.return_value = (mock_user, 200)
    
    response = app.get('/usuarios/1')
    
    assert response.status_code == 200
    assert json.loads(response.data) == mock_user
    mock_get_user_by_id.assert_called_once_with('1')

# Teste para POST /usuarios
@patch('src.services.users_service.User_Service.registro')  # Corrigido para o método correto
def test_create_usuario(mock_registro, app):
    user_data_to_create = {'nome': 'New User', 'email': 'newuser@test.com', 'senha': 'senha123'}  # Adicionei 'senha'
    mock_registro.return_value = ({"message": "User created successfully"}, 201)

    response = app.post('/usuarios', data=json.dumps(user_data_to_create), content_type='application/json')

    assert response.status_code == 201
    assert json.loads(response.data)["message"] == "User created successfully"
    mock_registro.assert_called_once_with(user_data_to_create)  # Corrigido para mock_registro


# Teste para PUT /usuarios/<user_id>
@patch('src.services.users_service.User_Service.update_user')
def test_update_usuario(mock_update_user, app):
    user_data_to_update = {'nome': 'Updated User', 'email': 'updateduser@test.com'}
    mock_update_user.return_value = ({"message": "User updated successfully"}, 200)
    
    response = app.put('/usuarios/1', data=json.dumps(user_data_to_update), content_type='application/json')
    
    assert response.status_code == 200
    assert json.loads(response.data)["message"] == "User updated successfully"
    mock_update_user.assert_called_once_with('1', user_data_to_update)

# Teste para DELETE /usuarios/<user_id>
@patch('src.services.users_service.User_Service.delete_user')
def test_delete_usuario(mock_delete_user, app):
    mock_delete_user.return_value = ({"message": "User deleted successfully"}, 200)
    
    response = app.delete('/usuarios/1')
    
    assert response.status_code == 200
    assert json.loads(response.data)["message"] == "User deleted successfully"
    mock_delete_user.assert_called_once_with('1')
