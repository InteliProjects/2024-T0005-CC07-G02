from src.models.servicos_contratados import Servicos_Contratados as ServicosContratadosModel
from src.models.planos_model import Planos as PlanosModel
from src.utils import Logging
from src import db

logger = Logging()

class Servicos_Contratados_Service:
    @staticmethod
    def get_all_services():
        try:
            # Get all services from the database
            services = ServicosContratadosModel.query.all()

            logger.log_info(f"Serviços encontrados: {services}")
            # If services exist
            if services:
                # Create a list of services
                services_list = []
                for service in services:
                    service_data = {
                        "id": service.id,
                        "id_cliente": service.id_cliente,
                        "id_plano": service.id_plano,
                        "data_contratacao": str(service.data_contratacao) if service.data_contratacao else None,
                        "data_cancelamento": str(service.data_cancelamento) if service.data_cancelamento else None
                    }
                    services_list.append(service_data)
                return {"status": "success", "data": services_list}, 200
            else:
                # If services do not exist
                return {"status": "failed", "message": "No services found"}, 404
        except Exception as e:
            return {"status": "failed", "message": "An error occurred", "error": str(e)}, 500
        
    @staticmethod
    def get_service_by_id(service_id):
        try:
            # Get the service from the database
            service = ServicosContratadosModel.query.filter_by(id=service_id).first()

            logger.log_info(f"Serviço encontrado com o id {service_id}: {service}")
            # If the service exists
            if service:
                # Create a dictionary of the service
                service_data = {
                    "id": service.id,
                    "id_cliente": service.id_cliente,
                    "id_plano": service.id_plano,
                    "data_contratacao": str(service.data_contratacao) if service.data_contratacao else None,
                    "data_cancelamento": str(service.data_cancelamento) if service.data_cancelamento else None
                }
                return {"status": "success", "data": service_data}, 200
            else:
                # If the service does not exist
                return {"status": "failed", "message": "Service not found"}, 404
        except Exception as e:
            return {"status": "failed", "message": "An error occurred", "error": str(e)}, 500
        
    @staticmethod
    def get_services_by_client(client_id):
        print(f"client_id: {client_id}")
        try:
            # Obter todos os serviços do banco de dados e juntá-los com os detalhes do plano
            services = db.session.query(ServicosContratadosModel, PlanosModel).\
                filter(ServicosContratadosModel.id_cliente == client_id).\
                join(PlanosModel, ServicosContratadosModel.id_plano == PlanosModel.id).\
                all()

            # Se serviços existirem
            if services:
                # Criar uma lista de serviços com detalhes do plano
                services_list = []
                for service, plan_detail in services:
                    service_data = {
                        "id": service.id,
                        "id_cliente": service.id_cliente,
                        "id_plano": service.id_plano,
                        "plan_details": {
                            "id": plan_detail.id,
                            "nome_do_plano": plan_detail.nome_do_plano,
                            "descricao": plan_detail.descricao,
                            "valor": str(plan_detail.valor)
                        },
                        "data_contratacao": str(service.data_contratacao) if service.data_contratacao else None,
                        "data_cancelamento": str(service.data_cancelamento) if service.data_cancelamento else None
                    }
                    services_list.append(service_data)
                return {"status": "success", "data": services_list}, 200
            else:
                # Se não houver serviços encontrados
                return {"status": "failed", "message": "Nenhum serviço encontrado"}, 404
        except Exception as e:
            return {"status": "failed", "message": "Ocorreu um erro", "error": str(e)}, 500

    @staticmethod
    def create_service(request_data, client_id):
        try:
            # Create a new service
            new_service = ServicosContratadosModel(
                id_cliente=client_id,
                id_plano=request_data["id_plano"],
                data_contratacao=request_data["data_contratacao"],
                data_cancelamento=request_data["data_cancelamento"] if "data_cancelamento" in request_data else None
            )
            new_service.save()
            
            logger.log_info(f"Serviço criado com sucesso: {new_service}")
            
            return {"status": "success", "message": "Service created successfully", "data": request_data}, 201
        except Exception as e:
            return {"status": "failed", "message": "An error occurred", "error": str(e)}, 500
        
    @staticmethod
    def update_service(service_id, request_data):
        try:
            # Get the service from the database
            service = ServicosContratadosModel.query.filter_by(id=service_id).first()

            logger.log_info(f"Serviço encontrado com o id {service_id}: {service}")
            logger.log_info(f"Serviço encontrado com o id {service_id}: atualização: {request_data}")
            # If the service exists
            if service:
                updated_service_data = {
                    "id": service.id,
                    "id_cliente": request_data.get("id_cliente"),
                    "id_plano": request_data.get("id_plano"),
                    "data_contratacao": request_data.get("data_contratacao"),
                    "data_cancelamento": request_data.get("data_cancelamento") if "data_cancelamento" in request_data else None
                }
                # Update the service
                service.update(
                    id_cliente=request_data.get("id_cliente"),
                    id_plano=request_data.get("id_plano"),
                    data_contratacao=request_data.get("data_contratacao"),
                    data_cancelamento=request_data.get("data_cancelamento")
                )
                return {"status": "success", "message": "Service updated successfully", "data": updated_service_data}, 200
            else:
                # If the service does not exist
                return {"status": "failed", "message": "Service not found"}, 404
        except Exception as e:
            return {"status": "failed", "message": "An error occurred", "error": str(e)}, 500
        
    @staticmethod
    def cancel_service(service_id):
        try:
            # Get the service from the database
            service = ServicosContratadosModel.query.filter_by(id=service_id).first()

            logger.log_info(f"Serviço encontrado com o id {service_id}: {service}")
            
            # If the service exists
            if service:
                # Delete the service from the database
                service.patch(data_cancelamento=db.func.current_timestamp())
                logger.log_info(f"Serviço cancelado com sucesso: {service}")
                return {"status": "success", "message": "Service canceled successfully"}, 200
            else:
                # If the service does not exist
                return {"status": "failed", "message": "Service not found"}, 404
        except Exception as e:
            return {"status": "failed", "message": "An error occurred", "error": str(e)}, 500
        