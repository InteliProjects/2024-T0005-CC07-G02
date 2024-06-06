import unittest
from unittest.mock import MagicMock
from flask import Response
from src.controllers.planos_controller import Planos_Controller

class TestPlanosController(unittest.TestCase):
    def setUp(self):
        self.controller = Planos_Controller("test_planos", __name__)
        self.mock_service = MagicMock()
        self.controller.Planos_Service = self.mock_service

    def test_get_plan_by_id(self):
        expected_response_data = {"id": "1", "name": "Plan A"}
        expected_status_code = 200
        plan_id = "1"

        self.mock_service.get_plan_by_id.return_value = (expected_response_data, expected_status_code)

        with self.controller.test_request_context(f"/{plan_id}"):
            response = self.controller.get_plan_by_id(plan_id)

        self.assertIsInstance(response, Response)
        self.assertEqual(response.status_code, expected_status_code)
        self.assertEqual(response.get_json(), expected_response_data)

    def test_get_plan_by_service_type(self):
        expected_response_data = {"plans": [{"id": "1", "name": "Plan A"}]}
        expected_status_code = 200
        service_type = "type_a"

        self.mock_service.get_plan_by_service_type.return_value = (expected_response_data, expected_status_code)

        with self.controller.test_request_context(f"/{service_type}"):
            response = self.controller.get_plan_by_service_type(service_type)

        self.assertIsInstance(response, Response)
        self.assertEqual(response.status_code, expected_status_code)
        self.assertEqual(response.get_json(), expected_response_data)

    def test_delete_plan(self):
        expected_response_data = {"message": "Plan deleted successfully"}
        expected_status_code = 200
        plan_id = "1"

        self.mock_service.delete_plan.return_value = (expected_response_data, expected_status_code)

        with self.controller.test_request_context(f"/{plan_id}", method="DELETE"):
            response = self.controller.delete_plan(plan_id)

        self.assertIsInstance(response, Response)
        self.assertEqual(response.status_code, expected_status_code)
        self.assertEqual(response.get_json(), expected_response_data)

    def test_create_plan(self):
        expected_response_data = {"message": "Plan created successfully"}
        expected_status_code = 201
        request_data = {"name": "Plan A"}

        self.mock_service.create_plan.return_value = (expected_response_data, expected_status_code)

        with self.controller.test_request_context("/", json=request_data, method="POST"):
            response = self.controller.create_plan()

        self.assertIsInstance(response, Response)
        self.assertEqual(response.status_code, expected_status_code)
        self.assertEqual(response.get_json(), expected_response_data)

    def test_update_plan(self):
        expected_response_data = {"message": "Plan updated successfully"}
        expected_status_code = 200
        plan_id = "1"
        request_data = {"name": "Plan B"}

        self.mock_service.update_plan.return_value = (expected_response_data, expected_status_code)

        with self.controller.test_request_context(f"/{plan_id}", json=request_data, method="PUT"):
            response = self.controller.update_plan(plan_id)

        self.assertIsInstance(response, Response)
        self.assertEqual(response.status_code, expected_status_code)
        self.assertEqual(response.get_json(), expected_response_data)

if __name__ == "__main__":
    unittest.main()