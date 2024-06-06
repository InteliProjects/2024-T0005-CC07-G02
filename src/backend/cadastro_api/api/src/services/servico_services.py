from src import db
from src.models.servico_model import Servicos as ServicoModel
from src.utils import Logging

class Servico_Service:
    @staticmethod
    def criar_servico(dados_servico):
        try:
            novo_servico = ServicoModel(nome_servico=dados_servico["nome_servico"])
            db.session.add(novo_servico)
            db.session.commit()
            return {"status": "success", "message": "Serviço criado com sucesso", "data": {"id": novo_servico.id, "nome_servico": novo_servico.nome_servico}}, 201
        except Exception as e:
            db.session.rollback()
            return {"status": "failed", "message": "Erro ao criar serviço", "error": str(e)}, 500

    @staticmethod
    def get_servico_por_id(id_servico):
        try:
            servico = ServicoModel.query.filter_by(id=id_servico).first()
            if servico:
                dados_servico = {
                    "id": servico.id,
                    "nome_servico": servico.nome_servico
                }
                return {"status": "success", "data": dados_servico}, 200
            else:
                return {"status": "failed", "message": "Serviço não encontrado"}, 404
        except Exception as e:
            return {"status": "failed", "message": "Erro ao buscar serviço", "error": str(e)}, 500

    @staticmethod
    def get_todos_servicos():
        try:
            servicos = ServicoModel.query.all()
            lista_servicos = [{"id": servico.id, "nome_servico": servico.nome_servico} for servico in servicos]
            return {"status": "success", "data": lista_servicos}, 200
        except Exception as e:
            return {"status": "failed", "message": "Erro ao buscar serviços", "error": str(e)}, 500

    @staticmethod
    def atualizar_servico(id_servico, novos_dados):
        try:
            servico = ServicoModel.query.filter_by(id=id_servico).first()
            if servico:
                servico.nome_servico = novos_dados.get("nome_servico", servico.nome_servico)
                db.session.commit()
                return {"status": "success", "message": "Serviço atualizado com sucesso"}, 200
            else:
                return {"status": "failed", "message": "Serviço não encontrado"}, 404
        except Exception as e:
            db.session.rollback()
            return {"status": "failed", "message": "Erro ao atualizar serviço", "error": str(e)}, 500

    @staticmethod
    def deletar_servico(id_servico):
        try:
            servico = ServicoModel.query.filter_by(id=id_servico).first()
            if servico:
                db.session.delete(servico)
                db.session.commit()
                return {"status": "success", "message": "Serviço deletado com sucesso"}, 200
            else:
                return {"status": "failed", "message": "Serviço não encontrado"}, 404
        except Exception as e:
            db.session.rollback()
            return {"status": "failed", "message": "Erro ao deletar serviço", "error": str(e)}, 500
