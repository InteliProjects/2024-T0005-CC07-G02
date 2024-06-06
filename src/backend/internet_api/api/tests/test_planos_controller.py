# test_planos_controller.py
import pytest
from flask import Flask, json
from unittest.mock import MagicMock, patch
from flask import Response
from src.controllers.planos_controller import planos_blueprint
from src.services.planos_service import Planos_Service

# Configuração do aplicativo para teste
@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(planos_blueprint)
    app.config['TESTING'] = True
    return app

@pytest.fixture
def client(app):
    return app.test_client()

# Teste unitário para o endpoint get_all_plans do /planos_controller.py
def test_get_all_plans(client):
    with patch.object(Planos_Service, 'get_all_plans') as mock_get_all_plans:
        # Configura o mock para retornar dados específicos para a resposta
        mock_get_all_plans.return_value = ({"status": "success", "data": [{"id": "123", "nome_do_plano": "Plano Básico"}]}, 200)

        response = client.get("/")
        data = json.loads(response.data.decode('utf-8'))

        print(f"Response data: {data}")
        print(f"Status code: {response.status_code}")

        assert response.status_code == 200
        assert data['status'] == 'success'
        assert type(data['data']) is list
        assert data['data'][0]['nome_do_plano'] == 'Plano Básico'
        mock_get_all_plans.assert_called_once()

# Define os dados de teste
mock_plan_data = {
    "id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
    "nome_do_plano": "Internet Movel",
    "descricao": "Descrição do Plano Teste",
    "valor": "99.99",
    "velocidade_contratada": "100"
}

# Teste unitário para o endpoint get_plan_by_id do /planos_controller.py
def test_get_plan_by_id(client):
    with patch.object(Planos_Service, 'get_plan_by_id') as mock_get_plan_by_id:
        # Configura o mock para retornar dados específicos para a resposta
        mock_get_plan_by_id.return_value = ({"status": "success", "data": mock_plan_data}, 200)

        response = client.get("/f47ac10b-58cc-4372-a567-0e02b2c3d479")  # GET pelo ID mockado
        data = json.loads(response.data.decode('utf-8'))

        print(f"Response data: {data}")
        print(f"Status code: {response.status_code}")

        assert response.status_code == 200
        assert data['status'] == 'success'
        assert data['data'] == mock_plan_data
        mock_get_plan_by_id.assert_called_once()

# Teste unitário para o endpoint get_plan_service_type do /planos_controller.py
def test_get_plan_by_service_type(client):
    with patch.object(Planos_Service, 'get_plan_by_service_type') as mock_get_plan_by_service_type:
        # Configura o mock para retornar dados específicos para a resposta
        mock_get_plan_by_service_type.return_value = ({"status": "success", "data": mock_plan_data}, 200)

        response = client.get("/Internet Movel")  # GET pelo tipo de serviço mockado
        data = json.loads(response.data.decode('utf-8'))

        print(f"Response data: {data}")
        print(f"Status code: {response.status_code}")

        assert response.status_code == 200
        assert data['status'] == 'success'
        assert data['data'] == mock_plan_data
        mock_get_plan_by_service_type.assert_called_once()

# Teste unitário para o endpoint delete_plan do /planos_controller.py
def test_delete_plan(client):
    with patch.object(Planos_Service, 'delete_plan') as mock_delete_plan:
        # Configura o mock para retornar dados específicos para a resposta
        mock_delete_plan.return_value = ({"status": "success", "message": "Delete com sucesso"}, 200)
        
        response = client.delete("/f47ac10b-58cc-4372-a567-0e02b2c3d479")
        data = json.loads(response.data.decode('utf-8'))

        print(f"Response data: {data}")
        print(f"Status code: {response.status_code}")
        
        assert response.status_code == 200
        assert data['status'] == 'success'
        mock_delete_plan.assert_called_once_with('f47ac10b-58cc-4372-a567-0e02b2c3d479')

# Teste unitário para o endpoint create_plan do /planos_controller.py
def test_create_plan(client):
    with patch.object(Planos_Service, 'create_plan') as mock_create_plan:
        # Configura o mock para retornar dados específicos para a resposta
        mock_create_plan.return_value = ({"status": "success", "message": "Criado com sucesso", "data": mock_plan_data}, 201)
        
        response = client.post("/", json=mock_plan_data)
        data = json.loads(response.data.decode('utf-8'))
        
        print(f"Response data: {data}")
        print(f"Status code: {response.status_code}")

        assert response.status_code == 201
        assert data['status'] == 'success'
        mock_create_plan.assert_called_once_with(mock_plan_data)

# Teste unitário para o endpoint update_plan do /planos_controller.py
def test_update_plan(client):
    updated_data = {
        "nome_do_plano": "Plano Atualizado",
        "descricao": "Descrição atualizada",
        "valor": "199.99",
        "velocidade_contratada": "200"
    }
    with patch.object(Planos_Service, 'update_plan') as mock_update_plan:
        # Configura o mock para retornar dados específicos para a resposta
        mock_update_plan.return_value = ({"status": "success", "message": "Atualizado com sucesso", "data": updated_data}, 200)
        
        response = client.put("/f47ac10b-58cc-4372-a567-0e02b2c3d479", json=updated_data)
        data = json.loads(response.data.decode('utf-8'))

        print(f"Response data: {data}")
        print(f"Status code: {response.status_code}")
        
        assert response.status_code == 200
        assert data['status'] == 'success'
        mock_update_plan.assert_called_once_with('f47ac10b-58cc-4372-a567-0e02b2c3d479', updated_data)

