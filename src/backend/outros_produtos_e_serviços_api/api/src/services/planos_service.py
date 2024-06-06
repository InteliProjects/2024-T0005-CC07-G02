import os
from src.models.planos_model import Planos as PlanosModel
from src.utils import Logging

logger = Logging()

class Planos_Service:
    @staticmethod
    def get_all_plans():
        try:
            # Get all plans from the database
            plans = PlanosModel.query.all()

            logger.log_info(f"Planos encontrados: {plans}")
            # If plans exist
            if plans:
                # Create a list of plans
                plans_list = []
                for plan in plans:
                    plan_data = {
                        "id": plan.id,
                        "nome_do_plano": plan.nome_do_plano,
                        "descricao": plan.descricao,
                        "valor": str(plan.valor)
                    }
                    plans_list.append(plan_data)
                return {"status": "success", "data": plans_list}, 200
            else:
                # If plans do not exist
                return {"status": "failed", "message": "No plans found"}, 404
        except Exception as e:
            return {"status": "failed", "message": "An error occurred", "error": str(e)}, 500

    @staticmethod
    def get_plan_by_id(plan_id):
        try:
            # Get plan from the database
            plan = PlanosModel.query.filter_by(id=plan_id).first()
            
            logger.log_info(f"Plano encontrado com o id {plan_id}: {plan}")
            
            # If plan exists
            if plan:
                plan_data = {
                    "id": plan.id,
                    "nome_do_plano": plan.nome_do_plano,
                    "descricao": plan.descricao,
                    "valor": str(plan.valor)
                }
                return {"status": "success", "data": plan_data}, 200
            else:
                # If plan does not exist
                return {"status": "failed", "message": "Plan not found"}, 404
        except Exception as e:
            return {"status": "failed", "message": "An error occurred", "error": str(e)}, 500
    
    @staticmethod
    def get_plan_by_service_type(service_type):
        try:
            # Get plan from the database
            plan = PlanosModel.query.filter_by(nome_do_plano=service_type).first()

            logger.log_info(f"Plano encontrado com o tipo de serviço {service_type}: {plan}")

            # If plan exists
            if plan:
                plan_data = {
                    "id": plan.id,
                    "nome_do_plano": plan.nome_do_plano,
                    "descricao": plan.descricao,
                    "valor": str(plan.valor)
                }
                return {"status": "success", "data": plan_data}, 200
            else:
                # If plan does not exist
                return {"status": "failed", "message": "Plan not found"}, 404
        except Exception as e:
            return {"status": "failed", "message": "An error occurred", "error": str(e)}, 500
    
    @staticmethod
    def create_plan(plan_data):
        try:            
            # Create a new plan
            new_plan = PlanosModel(
                nome_do_plano=plan_data["nome_do_plano"],
                descricao=plan_data["descricao"],
                valor=plan_data["valor"]
            )
            new_plan.save()
            
            logger.log_info(f"Plano criado com sucesso: {new_plan}")
            
            return {"status": "success", "message": "Plan created successfully", "data": plan_data}, 201
        except Exception as e:
            return {"status": "failed", "message": "An error occurred", "error": str(e)}, 500
    
    @staticmethod
    def update_plan(plan_id, plan_data):
        try:
            # Get plan from the database
            plan = PlanosModel.query.filter_by(id=plan_id).first()

            logger.log_info(f"Plano encontrado com o id {plan_id}: {plan}")
            logger.log_info(f"Plano encontrado com o id {plan_id}: atualização: {plan_data}")
        
            # If plan exists
            if plan:
                updated_plan_data = {
                    "id": plan.id,
                    "nome_do_plano": plan_data["nome_do_plano"],
                    "descricao": plan_data["descricao"],
                    "valor": plan_data["valor"]
                }
                # Update plan
                plan.update(
                    nome_do_plano=updated_plan_data.get("nome_do_plano"),
                    descricao=updated_plan_data.get("descricao"),
                    valor=updated_plan_data.get("valor")
                )
                
                return {"status": "success", "message": "Plan updated successfully", "data": updated_plan_data}, 200
            else:
                # If plan does not exist
                return {"status": "failed", "message": "Plan not found"}, 404
        except Exception as e:
            return {"status": "failed", "message": "An error occurred", "error": str(e)}, 500
    
    @staticmethod
    def delete_plan(plan_id):
        try:
            # Get plan from the database
            plan = PlanosModel.query.filter_by(id=plan_id).first()

            logger.log_info(f"Plano com o id {plan_id}: {plan} foi deletado")

            # If plan exists
            if plan:
                # Delete plan
                plan.delete()
                return {"status": "success", "message": "Plan deleted successfully"}, 200
            else:
                # If plan does not exist
                return {"status": "failed", "message": "Plan not found"}, 404
        except Exception as e:
            return {"status": "failed", "message": "An error occurred", "error": str(e)}, 500
