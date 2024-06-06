from src import db
from src.models.servico_usuario_model import Servicos_Usuarios  # Ajuste o caminho conforme sua estrutura de projeto
from src.utils import Logging

logger = Logging()

class ServicoUsuarioService:
    @staticmethod
    def criar_relacao_servico_usuario(dados_relacao):
        try:
            nova_relacao = Servicos_Usuarios(
                id_servico=dados_relacao["id_servico"],
                id_usuario=dados_relacao["id_usuario"]
            )
            db.session.add(nova_relacao)
            db.session.commit()
            return {"status": "success", "message": "Relação serviço-usuário criada com sucesso"}, 201
        except Exception as e:
            db.session.rollback()
            return {"status": "failed", "message": "Erro ao criar relação serviço-usuário", "error": str(e)}, 500

    @staticmethod
    def buscar_relacao_por_usuario(id_usuario):
        try:
            relacoes = Servicos_Usuarios.query.filter_by(id_usuario=id_usuario).all()
            if relacoes:
                dados_relacoes = [{"id": relacao.id, "id_servico": relacao.id_servico, "id_usuario": relacao.id_usuario} for relacao in relacoes]
                return {"status": "success", "data": dados_relacoes}, 200
            else:
                return {"status": "failed", "message": "Relações serviço-usuário não encontradas"}, 404
        except Exception as e:
            return {"status": "failed", "message": "Erro ao buscar relações serviço-usuário", "error": str(e)}, 500

    @staticmethod
    def atualizar_relacao_servico_usuario(id_relacao, novos_dados):
        try:
            relacao = Servicos_Usuarios.query.filter_by(id=id_relacao).first()
            if relacao:
                relacao.id_servico = novos_dados.get("id_servico", relacao.id_servico)
                relacao.id_usuario = novos_dados.get("id_usuario", relacao.id_usuario)
                db.session.commit()
                return {"status": "success", "message": "Relação serviço-usuário atualizada com sucesso"}, 200
            else:
                return {"status": "failed", "message": "Relação serviço-usuário não encontrada"}, 404
        except Exception as e:
            db.session.rollback()
            return {"status": "failed", "message": "Erro ao atualizar relação serviço-usuário", "error": str(e)}, 500

    @staticmethod
    def deletar_relacao_servico_usuario(id_relacao):
        try:
            relacao = Servicos_Usuarios.query.filter_by(id=id_relacao).first()
            if relacao:
                db.session.delete(relacao)
                db.session.commit()
                return {"status": "success", "message": "Relação serviço-usuário deletada com sucesso"}, 200
            else:
                return {"status": "failed", "message": "Relação serviço-usuário não encontrada"}, 404
        except Exception as e:
            db.session.rollback()
            return {"status": "failed", "message": "Erro ao deletar relação serviço-usuário", "error": str(e)}, 500
