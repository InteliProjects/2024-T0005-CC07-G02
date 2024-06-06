import unittest
from unittest.mock import MagicMock
from werkzeug.datastructures import Headers
from flask import Flask, request, jsonify
from src.middlewares.auth_middleware import Auth_Middleware

class TestJwtMiddleware(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.middleware = Auth_Middleware(self.app)

        # Mock do método before_request
        self.middleware.before_request = MagicMock()

        # Registrar o middleware no aplicativo Flask
        self.app.before_request(self.middleware.before_request)

        # Criar um cliente de teste para enviar solicitações HTTP
        self.client = self.app.test_client()

    def test_middleware_before_request_valid_token(self):
        # Token JWT válido para testar
        valid_token = "valid_jwt_token"

        # Adicionar token ao cabeçalho de autorização
        headers = Headers({"Authorization": f"Bearer {valid_token}"})

        # Enviar uma solicitação de teste com o cabeçalho de autorização contendo o token JWT válido
        response = self.client.get("/", headers=headers)

        # Verificar se o método before_request foi chamado
        self.middleware.before_request.assert_called_once()

        # Verificar se não houve resposta de erro
        self.assertNotEqual(response.status_code, 401)

    def test_middleware_before_request_invalid_token(self):
        # Token JWT inválido para testar
        invalid_token = "invalid_jwt_token"

        # Adicionar token inválido ao cabeçalho de autorização
        headers = Headers({"Authorization": f"Bearer {invalid_token}"})

        # Enviar uma solicitação de teste com o cabeçalho de autorização contendo o token JWT inválido
        response = self.client.get("/", headers=headers)

        # Verificar se o método before_request foi chamado
        self.middleware.before_request.assert_called_once()

        # Verificar se a resposta foi um erro de autorização (status code 401)
        self.assertEqual(response.status_code, 401)

if __name__ == "__main__":
    unittest.main()