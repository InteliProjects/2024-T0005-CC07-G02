import pytest
from flask import Flask
from src import db
from src.models.fatura import Fatura, ItemFatura
from src.services.fatura_service import Fatura_Service
from unittest.mock import patch, MagicMock

@pytest.fixture(scope='module')
def app():
    """Fixture para configuração do aplicativo Flask para testes."""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['TESTING'] = True
    db.init_app(app)
    with app.app_context():
        db.create_all()
    yield app
    with app.app_context():
        db.drop_all()

@pytest.fixture
def app_context(app):
    """Cria um contexto de aplicação para cada teste."""
    with app.app_context():
        yield

@pytest.fixture
def client(app):
    """Cria um cliente de teste para simular requisições HTTP."""
    return app.test_client()

# Exemplo de dados de teste para uma fatura e itens
mock_fatura_data = {
   #"id": "fatura123",
    "id_cliente": "cliente123",
    "itens": [
        {"id_produto": "produto1", "valor": 100.00},
        {"id_produto": "produto2", "valor": 200.00}
    ]
}

def test_create_fatura(app_context):
    """Testa a criação de uma fatura."""
    with patch.object(Fatura, 'save', autospec=True) as mock_save, \
         patch.object(ItemFatura, 'save', autospec=True) as mock_item_save:
        response = Fatura_Service.create_fatura(id_cliente=mock_fatura_data['id_cliente'], itens=mock_fatura_data['itens'])

        assert response[0]['status'] == 'success'
        assert response[1] == 201
        mock_save.assert_called_once()
        assert mock_item_save.call_count == len(mock_fatura_data['itens'])

def test_get_all_faturas(app_context):
    """Testa a obtenção de todas as faturas de um cliente."""
    with patch('src.models.fatura.Fatura.query') as mock_query:
        mock_query.filter_by.return_value.all.return_value = [MagicMock(spec=Fatura)]
        response = Fatura_Service.get_all_faturas("cliente123")

        assert response[0]['status'] == 'success'
        assert response[1] == 200

def test_get_fatura_by_id(app_context):
    """Testa a obtenção de uma fatura pelo ID."""
    with patch('src.models.fatura.Fatura.query') as mock_query:
        mock_fatura = MagicMock(spec=Fatura)
        mock_fatura.to_dict.return_value = mock_fatura_data  # Garante que to_dict retorne o dicionário esperado
        mock_query.get.return_value = mock_fatura

        # Chamada à função que estava faltando
        response = Fatura_Service.get_fatura_by_id("fatura123")

        assert response[0]['status'] == 'success'

def test_update_fatura(app_context):
    """Testa a atualização de uma fatura."""
    updated_data = {'pago': True}
    with patch('src.models.fatura.Fatura.query') as mock_query:
        mock_query.get.return_value = MagicMock(spec=Fatura, **mock_fatura_data, update=MagicMock())
        response = Fatura_Service.update_fatura("fatura123", **updated_data)

        assert response[0]['status'] == 'success'
        assert response[1] == 200

def test_delete_fatura(app_context):
    """Testa a deleção de uma fatura."""
    with patch('src.models.fatura.Fatura.query') as mock_query:
        # Cria mocks para os itens de fatura, com o método `delete` já mockado.
        mock_item1 = MagicMock(spec=ItemFatura)
        mock_item2 = MagicMock(spec=ItemFatura)

        # Configura a instância mock da fatura para usar os mocks dos itens
        mock_fatura_instance = MagicMock(spec=Fatura, itens=[mock_item1, mock_item2])
        mock_query.get.return_value = mock_fatura_instance

        # Chamada à função que estava faltando
        response = Fatura_Service.delete_fatura("fatura123")

        assert response[0]['status'] == 'success'
        # Agora, verifica se o método `delete` foi chamado em cada mock de item de fatura
        mock_item1.delete.assert_called_once()
        mock_item2.delete.assert_called_once()




# print(test_create_fatura(app_context))
# print(test_get_all_faturas(app_context))
# print(test_get_fatura_by_id(app_context))
# print(test_update_fatura(app_context))
# print(test_delete_fatura(app_context))