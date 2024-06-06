from datetime import datetime, timedelta
from src.models.user_model import Usuarios as UserModel
from src.utils import Logging
import os
import jwt
from src import bcrypt

logger = Logging()

class User_Service:
    @staticmethod
    def get_all_users():
        try:
            users = UserModel.query.all()
            if users: 
                users_list = []
                for user in users:
                    user_data = {
                        'id': user.id,
                        'name': user.name,
                        'email': user.email,
                        'senha': user.senha
                    }
                    users_list.append(user_data)
                return {"status": "success", "data": users_list}, 200
            else: 
                return {"status": "failed", "message": "No users found"}, 404
        except Exception as e:
            return {"status": "failed", "message": "An error ocured", "error": str(e)}, 500
    
    @staticmethod
    def get_user_by_id(user_id):
        try:
            user = UserModel.query.filter_by(id=user_id).first()  # Busca o usuário pelo ID fornecido
            logger.log_info(f"Usuário encontrado com o id {user_id}: {user}")  # Registra no log a informação do usuário encontrado
            if user:
                user_data = {
                    "id": user.id,
                    "nome": user.nome,
                    "email": user.email,
                    "senha": user.senha  # Monta um dicionário com os dados do usuário
                }
                return {"status": "success", "data": user_data}, 200  # Retorna os dados do usuário e o status HTTP 200
            else:
                return {"status": "failed", "message": "User not found"}, 404  # Caso o usuário não seja encontrado, retorna status HTTP 404
        except Exception as e:
            return {"status": "failed", "message": "An error occurred", "error": str(e)}, 500  # Em caso de erro, retorna status HTTP 500

    @staticmethod
    def login(user_data):
        try:
            if "email" in user_data and "senha" in user_data:  # Verifica se os dados necessários foram fornecidos
                user = UserModel.query.filter_by(email=user_data["email"]).first()  # Busca o usuário pelo e-mail fornecido
                if user and bcrypt.check_password_hash(user.senha, user_data["senha"]):  # Verifica se o usuário foi encontrado e se a senha fornecida está correta
                    payload = {
                        'iat': datetime.now(),
                        'exp': datetime.now() + timedelta(days=1),  # Adiciona uma expiração de 1 dia ao token JWT
                        'user_id': user.id,
                        'nome': user.nome,
                        'email': user.email
                    }
                    token = jwt.encode(payload, os.getenv('SECRET_KEY'), algorithm='HS256')  # Gera um token JWT para o usuário
                    logger.log_info(f"Usuário logado com sucesso: {user}")  # Registra no log o login do usuário
                    return {"status": "success", "message": "User logged in successfully", "data": user_data, "token": token}, 200  # Retorna mensagem de sucesso e status HTTP 200
                else:
                    logger.log_info(f"Usuário não encontrado ou senha incorreta: {user}")
                    return {"status": "failed", "message": "User not found or incorrect password"}, 404  # Caso o usuário não seja encontrado ou a senha esteja incorreta, retorna status HTTP 404
            else:
                return {"status": "failed", "message": "Missing required data"}, 400
        except Exception as e:
            return {"status": "failed", "message": "An error occurred", "error": str(e)}, 500
        

    @staticmethod
    def registro(user_data):
        try:
            if "nome" in user_data and "email" in user_data and "senha" in user_data:  # Verifica se os dados necessários foram fornecidos
                user = UserModel.query.filter_by(email=user_data["email"]).first()  # Verifica se o e-mail fornecido já está cadastrado
                if not user:  # Se o e-mail não estiver cadastrado, prossegue com a criação do usuário
                    new_user = UserModel(
                        nome=user_data["nome"],
                        email=user_data["email"],
                        senha= bcrypt.generate_password_hash(user_data["senha"]).decode("utf-8")  # Cria uma nova instância do usuário com os dados fornecidos
                    )
                    new_user.save()  # Salva o novo usuário no banco de dados
                    
                    payload = {
                        'iat': datetime.now(),
                        'exp': datetime.now() + timedelta(days=1),  # Adiciona uma expiração de 1 dia ao token JWT
                        'user_id': new_user.id,
                        'nome': new_user.nome,
                        'email': new_user.email
                    }
                    token = jwt.encode(payload, os.getenv('SECRET_KEY'), algorithm='HS256')  # Gera um token JWT para o usuário
            
            
                    logger.log_info(f"Usuário criado com sucesso: {new_user}")  # Registra no log a criação do usuário
                    return {"status": "success", "message": "User created successfully", "data": user_data, "token": token}, 201  # Retorna mensagem de sucesso e status HTTP 201
                else:
                    logger.log_info(f"Usuário já existente: {user}")  # Registra no log que o e-mail já está cadastrado
                    return {"status": "failed", "message": "User already exists"}, 400
            else:
                return {"status": "failed", "message": "Missing required data"}, 400

        except Exception as e:
            return {"status": "failed", "message": "An error occurred", "error": str(e)}, 500  # Em caso de erro, retorna status HTTP 500

    @staticmethod
    def update_user(user_id, user_data):
        try:
            user = UserModel.query.filter_by(id=user_id).first()  # Busca o usuário pelo ID fornecido
            logger.log_info(f"Usuário encontrado com o id {user_id}: {user}")  # Registra no log a informação do usuário encontrado
            if user:
                user.nome = user_data.get("nome")
                user.email = user_data.get("email")
                user.senha = user_data.get("senha")  # Atualiza os dados do usuário
                user.save()  # Salva as alterações no banco de dados
                return {"status": "success", "message": "User updated successfully", "data": user_data}, 200  # Retorna mensagem de sucesso e status HTTP 200
            else:
                return {"status": "failed", "message": "User not found"}, 404  # Caso o usuário não seja encontrado, retorna status HTTP 404
        except Exception as e:
            return {"status": "failed", "message": "An error occurred", "error": str(e)}, 500  # Em caso de erro, retorna status HTTP 500

    @staticmethod
    def delete_user(user_id):
        try:
            user = UserModel.query.filter_by(id=user_id).first()  # Busca o usuário pelo ID fornecido
            logger.log_info(f"Usuário com o id {user_id}: {user} foi deletado")  # Registra no log a informação do usuário deletado
            if user:
                user.delete()  # Deleta o usuário do banco de dados
                return {"status": "success", "message": "User deleted successfully"}, 200  # Retorna mensagem de sucesso e status HTTP 200
            else:
                return {"status": "failed", "message": "User not found"}, 404  # Caso o usuário não seja encontrado, retorna status HTTP 404
        except Exception as e:
            return {"status": "failed", "message": "An error occurred", "error": str(e)}, 500  # Em caso de erro, retorna status HTTP 500
        