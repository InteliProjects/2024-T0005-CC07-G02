import unittest
from unittest.mock import MagicMock
from src.models.planos_model import Planos

class TestPlanosModel(unittest.TestCase):
    def setUp(self):
        self.mock_db = MagicMock()
        self.model = Planos(nome_do_plano="Plano Teste", descricao="Descrição do plano teste", valor=100.00)

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
        self.model.update(nome_do_plano="Novo Nome do Plano", descricao="Nova descrição do plano", valor=200.00)

        # Verificar se os atributos do modelo foram atualizados corretamente
        self.assertEqual(self.model.nome_do_plano, "Novo Nome do Plano")
        self.assertEqual(self.model.descricao, "Nova descrição do plano")
        self.assertEqual(self.model.valor, 200.00)

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
