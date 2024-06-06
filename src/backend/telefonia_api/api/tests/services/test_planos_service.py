import unittest
from unittest.mock import MagicMock
from src.services.planos_service import Planos_Service

class TestPlanosService(unittest.TestCase):
    def setUp(self):
        self.mock_planos_model = MagicMock()
        self.service = Planos_Service()

        # Substituir PlanosModel por mock_planos_model
        self.service.PlanosModel = self.mock_planos_model

    def test_get_all_plans_success(self):
        # Configurar comportamento esperado do mock de PlanosModel
        self.mock_planos_model.query.all.return_value = ["Plano1", "Plano2"]

        # Chamar método get_all_plans do serviço
        response, status_code = self.service.get_all_plans()

        # Verificar se o método query.all foi chamado corretamente
        self.mock_planos_model.query.all.assert_called_once()

        # Verificar se a resposta retornada é correta
        self.assertEqual(status_code, 200)
        self.assertEqual(response["status"], "success")
        self.assertEqual(len(response["data"]), 2)

    def test_get_all_plans_no_plans(self):
        # Configurar comportamento esperado do mock de PlanosModel
        self.mock_planos_model.query.all.return_value = []

        # Chamar método get_all_plans do serviço
        response, status_code = self.service.get_all_plans()

        # Verificar se o método query.all foi chamado corretamente
        self.mock_planos_model.query.all.assert_called_once()

        # Verificar se a resposta retornada é correta
        self.assertEqual(status_code, 404)
        self.assertEqual(response["status"], "failed")
        self.assertEqual(response["message"], "No plans found")

    def test_get_plan_by_id_success(self):
        # Configurar comportamento esperado do mock de PlanosModel
        self.mock_planos_model.query.filter_by().first.return_value = MagicMock(
            id="1",
            nome_do_plano="Plano Teste",
            descricao="Descrição do Plano Teste",
            valor=100.00
        )

        # Chamar método get_plan_by_id do serviço
        response, status_code = self.service.get_plan_by_id("1")

        # Verificar se o método query.filter_by().first foi chamado corretamente
        self.mock_planos_model.query.filter_by.assert_called_once_with(id="1")
        self.mock_planos_model.query.filter_by().first.assert_called_once()

        # Verificar se a resposta retornada é correta
        self.assertEqual(status_code, 200)
        self.assertEqual(response["status"], "success")
        self.assertEqual(response["data"]["id"], "1")
        self.assertEqual(response["data"]["nome_do_plano"], "Plano Teste")
        self.assertEqual(response["data"]["descricao"], "Descrição do Plano Teste")
        self.assertEqual(response["data"]["valor"], "100.00")

    def test_get_plan_by_id_no_plan(self):
        # Configurar comportamento esperado do mock de PlanosModel
        self.mock_planos_model.query.filter_by().first.return_value = None

        # Chamar método get_plan_by_id do serviço
        response, status_code = self.service.get_plan_by_id("1")

        # Verificar se o método query.filter_by().first foi chamado corretamente
        self.mock_planos_model.query.filter_by.assert_called_once_with(id="1")
        self.mock_planos_model.query.filter_by().first.assert_called_once()

        # Verificar se a resposta retornada é correta
        self.assertEqual(status_code, 404)
        self.assertEqual(response["status"], "failed")
        self.assertEqual(response["message"], "Plan not found")

if __name__ == "__main__":
    unittest.main()
