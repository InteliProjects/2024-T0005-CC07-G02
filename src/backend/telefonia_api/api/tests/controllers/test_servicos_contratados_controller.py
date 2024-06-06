import unittest
from unittest.mock import MagicMock
from flask import Response
from src.controllers.servicos_contratados_controller import Servicos_Contratados_Controller

class TestServicosContratadosController(unittest.TestCase):
    def setUp(self):
        self.controller = Servicos_Contratados_Controller("test_servicos_contratados", __name__)
        self.mock_service = MagicMock()
        self.controller.Servicos_Contratados_Service = self.mock_service

    def test_get_all_services(self):
        expected_response_data = {"services": [{"id": "1", "name": "Service A"}]}
        expected_status_code = 200

        self.mock_service.get_all_services.return_value = (expected_response_data, expected_status_code)

        with self.controller.test_request_context("/"):
            response = self.controller.get_all_services()

        self.assertIsInstance(response, Response)
        self.assertEqual(response.status_code, expected_status_code)
        self.assertEqual(response.get_json(), expected_response_data)

    def test_get_service_by_id(self):
        expected_response_data = {"id": "1", "name": "Service A"}
        expected_status_code = 200
        service_id = "1"

        self.mock_service.get_service_by_id.return_value = (expected_response_data, expected_status_code)

        with self.controller.test_request_context(f"/{service_id}"):
            response = self.controller.get_service_by_id(service_id)

        self.assertIsInstance(response, Response)
        self.assertEqual(response.status_code, expected_status_code)
        self.assertEqual(response.get_json(), expected_response_data)

    def test_get_services_by_client(self):
        expected_response_data = {"services": [{"id": "1", "name": "Service A"}]}
        expected_status_code = 200
        user_id = "user123"

        self.mock_service.get_services_by_client.return_value = (expected_response_data, expected_status_code)

        with self.controller.test_request_context("/client/", headers={"user_id": user_id}):
            response = self.controller.get_services_by_client()

        self.assertIsInstance(response, Response)
        self.assertEqual(response.status_code, expected_status_code)
        self.assertEqual(response.get_json(), expected_response_data)

    def test_delete_service(self):
        expected_response_data = {"message": "Service deleted successfully"}
        expected_status_code = 200
        service_id = "1"

        self.mock_service.delete_service.return_value = (expected_response_data, expected_status_code)

        with self.controller.test_request_context(f"/{service_id}", method="DELETE"):
            response = self.controller.delete_service(service_id)

        self.assertIsInstance(response, Response)
        self.assertEqual(response.status_code, expected_status_code)
        self.assertEqual(response.get_json(), expected_response_data)

    def test_create_service(self):
        expected_response_data = {"message": "Service created successfully"}
        expected_status_code = 201
        request_data = {"name": "Service A"}
        user_id = "user123"

        self.mock_service.create_service.return_value = (expected_response_data, expected_status_code)

        with self.controller.test_request_context("/", json=request_data, headers={"user_id": user_id}, method="POST"):
            response = self.controller.create_service()

        self.assertIsInstance(response, Response)
        self.assertEqual(response.status_code, expected_status_code)
        self.assertEqual(response.get_json(), expected_response_data)

    def test_update_service(self):
        expected_response_data = {"message": "Service updated successfully"}
        expected_status_code = 200
        service_id = "1"
        request_data = {"name": "Service B"}

        self.mock_service.update_service.return_value = (expected_response_data, expected_status_code)

        with self.controller.test_request_context(f"/{service_id}", json=request_data, method="PUT"):
            response = self.controller.update_service(service_id)

        self.assertIsInstance(response, Response)
        self.assertEqual(response.status_code, expected_status_code)
        self.assertEqual(response.get_json(), expected_response_data)

if __name__ == "__main__":
    unittest.main()