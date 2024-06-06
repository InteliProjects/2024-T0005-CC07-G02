from src import db
from src.models.endereco_model import Enderecos
from src.utils import Logging

logger = Logging()

class Endereco_Service:
    @staticmethod
    def get_all_enderecos():
        try:
            enderecos = Enderecos.query.all()
            enderecos_list = [{"id": endereco.id, "nome_endereco": endereco.nome_endereco} for endereco in enderecos]
            return {"status": "success", "data": enderecos_list}, 200
        except Exception as e:
            logger.log_error(str(e))
            return {"status": "failed", "message": "Erro ao buscar endereços"}, 500

    @staticmethod
    def get_endereco_by_id(endereco_id):
        try:
            endereco = Enderecos.query.filter_by(id=endereco_id).first()
            if endereco:
                endereco_data = {
                    "id": endereco.id,
                    "nome_endereco": endereco.nome_endereco
                }
                return {"status": "success", "data": endereco_data}, 200
            else:
                return {"status": "failed", "message": "Endereço não encontrado"}, 404
        except Exception as e:
            logger.log_error(str(e))
            return {"status": "failed", "message": "Erro ao buscar endereço"}, 500

    @staticmethod
    def create_endereco(endereco_data):
        try:
            novo_endereco = Enderecos(nome_endereco=endereco_data["nome_endereco"])
            db.session.add(novo_endereco)
            db.session.commit()
            return {"status": "success", "message": "Endereço criado com sucesso", "data": {"id": novo_endereco.id, "nome_endereco": novo_endereco.nome_endereco}}, 201
        except Exception as e:
            db.session.rollback()
            logger.log_error(str(e))
            return {"status": "failed", "message": "Erro ao criar endereço", "error": str(e)}, 500

    @staticmethod
    def update_endereco(endereco_id, endereco_data):
        try:
            endereco = Enderecos.query.filter_by(id=endereco_id).first()
            if endereco:
                endereco.nome_endereco = endereco_data.get("nome_endereco", endereco.nome_endereco)
                db.session.commit()
                return {"status": "success", "message": "Endereço atualizado com sucesso"}, 200
            else:
                return {"status": "failed", "message": "Endereço não encontrado"}, 404
        except Exception as e:
            db.session.rollback()
            logger.log_error(str(e))
            return {"status": "failed", "message": "Erro ao atualizar endereço"}, 500

    @staticmethod
    def delete_endereco(endereco_id):
        try:
            endereco = Enderecos.query.filter_by(id=endereco_id).first()
            if endereco:
                db.session.delete(endereco)
                db.session.commit()
                return {"status": "success", "message": "Endereço deletado com sucesso"}, 200
            else:
                return {"status": "failed", "message": "Endereço não encontrado"}, 404
        except Exception as e:
            db.session.rollback()
            logger.log_error(str(e))
            return {"status": "failed", "message": "Erro ao deletar endereço"}, 500
