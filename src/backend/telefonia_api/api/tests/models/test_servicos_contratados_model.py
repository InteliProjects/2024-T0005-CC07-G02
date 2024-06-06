import unittest
from unittest.mock import MagicMock
from src.models.servicos_contratados_model import Servicos_Contratados

class TestServicosContratadosModel(unittest.TestCase):
    def setUp(self):
        self.mock_db = MagicMock()
        self.model = Servicos_Contratados(id_cliente="cliente123", id_plano="plano123", data_contratacao="2022-01-01")

    def test_save_method(self):
        # Configurar comportamento esperado do mock de banco de dados
        self.mock_db.session.add.return_value = None
        self.mock_db.session.commit.return_value = None

        # Chamar método save do modelo
        self.model.save()

        # Verificar se o método session.add e session.commit foram chamados corretamente
        self.mock_db.session.add.assert_called_once_with(self.model)
        self.mock_db.session.commit.assert_called_once()

    def test_update_method(self):
        # Configurar comportamento esperado do mock de banco de dados
        self.mock_db.session.commit.return_value = None

        # Chamar método update do modelo
        self.model.update(id_cliente="novo_cliente", id_plano="novo_plano", data_contratacao="2023-01-01", data_cancelamento="2023-12-31")

        # Verificar se os atributos do modelo foram atualizados corretamente
        self.assertEqual(self.model.id_cliente, "novo_cliente")
        self.assertEqual(self.model.id_plano, "novo_plano")
        self.assertEqual(self.model.data_contratacao, "2023-01-01")
        self.assertEqual(self.model.data_cancelamento, "2023-12-31")

        # Verificar se o método session.commit foi chamado corretamente
        self.mock_db.session.commit.assert_called_once()

    def test_delete_method(self):
        # Configurar comportamento esperado do mock de banco de dados
        self.mock_db.session.delete.return_value = None
        self.mock_db.session.commit.return_value = None

        # Chamar método delete do modelo
        self.model.delete()

        # Verificar se o método session.delete e session.commit foram chamados corretamente
        self.mock_db.session.delete.assert_called_once_with(self.model)
        self.mock_db.session.commit.assert_called_once()

if __name__ == "__main__":
    unittest.main()