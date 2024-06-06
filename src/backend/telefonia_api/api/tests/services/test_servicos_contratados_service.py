import unittest
from unittest.mock import MagicMock
from src.services.servicos_contratados_service import Servicos_Contratados_Service

class TestServicosContratadosService(unittest.TestCase):
    def setUp(self):
        self.mock_servicos_contratados_model = MagicMock()
        self.mock_planos_model = MagicMock()
        self.service = Servicos_Contratados_Service()

        # Substituir ServicosContratadosModel e PlanosModel por mock_servicos_contratados_model e mock_planos_model
        self.service.ServicosContratadosModel = self.mock_servicos_contratados_model
        self.service.PlanosModel = self.mock_planos_model

    def test_get_all_services_success(self):
        # Configurar comportamento esperado do mock de ServicosContratadosModel
        self.mock_servicos_contratados_model.query.all.return_value = ["Service1", "Service2"]

        # Chamar método get_all_services do serviço
        response, status_code = self.service.get_all_services()

        # Verificar se o método query.all foi chamado corretamente
        self.mock_servicos_contratados_model.query.all.assert_called_once()

        # Verificar se a resposta retornada é correta
        self.assertEqual(status_code, 200)
        self.assertEqual(response["status"], "success")
        self.assertEqual(len(response["data"]), 2)

    def test_get_all_services_no_services(self):
        # Configurar comportamento esperado do mock de ServicosContratadosModel
        self.mock_servicos_contratados_model.query.all.return_value = []

        # Chamar método get_all_services do serviço
        response, status_code = self.service.get_all_services()

        # Verificar se o método query.all foi chamado corretamente
        self.mock_servicos_contratados_model.query.all.assert_called_once()

        # Verificar se a resposta retornada é correta
        self.assertEqual(status_code, 404)
        self.assertEqual(response["status"], "failed")
        self.assertEqual(response["message"], "No services found")

if __name__ == "__main__":
    unittest.main()
