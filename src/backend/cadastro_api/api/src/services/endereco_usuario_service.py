from src import db
from src.models.endereco_usuario_model import Enderecos_Usuarios

from src.utils import Logging

class EnderecoUsuarioService:
    @staticmethod
    def criar_relacao_endereco_usuario(dados_relacao):
        try:
            nova_relacao = Enderecos_Usuarios(
                id_endereco=dados_relacao["id_endereco"],
                id_usuario=dados_relacao["id_usuario"]
            )
            db.session.add(nova_relacao)
            db.session.commit()
            return {"status": "success", "message": "Relação endereço-usuário criada com sucesso"}, 201
        except Exception as e:
            db.session.rollback()
            return {"status": "failed", "message": "Erro ao criar relação endereço-usuário", "error": str(e)}, 500

    @staticmethod
    def get_relacao_por_usuario(id_usuario):
        try:
            relacao = Enderecos_Usuarios.query.filter_by(id_usuario=id_usuario).first()
            if relacao:
                dados_relacao = {
                    "id": relacao.id,
                    "id_endereco": relacao.id_endereco,
                    "id_usuario": relacao.id_usuario
                }
                return {"status": "success", "data": dados_relacao}, 200
            else:
                return {"status": "failed", "message": "Relação endereço-usuário não encontrada"}, 404
        except Exception as e:
            return {"status": "failed", "message": "Erro ao buscar relação endereço-usuário", "error": str(e)}, 500

    @staticmethod
    def atualizar_relacao_endereco_usuario(id_relacao, novos_dados):
        try:
            relacao = Enderecos_Usuarios.query.filter_by(id=id_relacao).first()
            if relacao:
                relacao.id_endereco = novos_dados.get("id_endereco", relacao.id_endereco)
                relacao.id_usuario = novos_dados.get("id_usuario", relacao.id_usuario)
                db.session.commit()
                return {"status": "success", "message": "Relação endereço-usuário atualizada com sucesso"}, 200
            else:
                return {"status": "failed", "message": "Relação endereço-usuário não encontrada"}, 404
        except Exception as e:
            db.session.rollback()
            return {"status": "failed", "message": "Erro ao atualizar relação endereço-usuário", "error": str(e)}, 500

    @staticmethod
    def deletar_relacao_endereco_usuario(id_relacao):
        try:
            relacao = Enderecos_Usuarios.query.filter_by(id=id_relacao).first()
            if relacao:
                db.session.delete(relacao)
                db.session.commit()
                return {"status": "success", "message": "Relação endereço-usuário deletada com sucesso"}, 200
            else:
                return {"status": "failed", "message": "Relação endereço-usuário não encontrada"}, 404
        except Exception as e:
            db.session.rollback()
            return {"status": "failed", "message": "Erro ao deletar relação endereço-usuário", "error": str(e)}, 500
