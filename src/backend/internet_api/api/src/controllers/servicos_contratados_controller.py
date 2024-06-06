from flask import Blueprint, Response, json, request
from src.services.servicos_contratados_service import Servicos_Contratados_Service

class Servicos_Contratados_Controller(Blueprint):
  def __init__(self, name, import_name):
    super().__init__(name, import_name)
        
    self.route("/", methods=["GET"])(self.get_all_services)
    self.route("/<string(36):service_id>", methods=["GET"])(self.get_service_by_id)
    self.route("/<string(36):service_id>", methods=["DELETE"])(self.delete_service)
    self.route("/", methods=["POST"])(self.create_service)
    self.route("/<string(36):service_id>", methods=["PUT"])(self.update_service)
    self.route("/client/", methods=["GET"])(self.get_services_by_client)

  def get_all_services(self):
    response_data, status_code = Servicos_Contratados_Service.get_all_services()
    return Response(
        response=json.dumps(response_data),
        status=status_code,
        mimetype="application/json"
    )
  
  def get_service_by_id(self, service_id):
    response_data, status_code = Servicos_Contratados_Service.get_service_by_id(service_id)
    return Response(
        response=json.dumps(response_data),
        status=status_code,
        mimetype="application/json"
    )
    
  def delete_service(self, service_id):
    response_data, status_code = Servicos_Contratados_Service.delete_service(service_id)
    return Response(
        response=json.dumps(response_data),
        status=status_code,
        mimetype="application/json"
    )
  
  def create_service(self):
    user_id = request.headers.get('user_id')
    request_data = request.json
    
    response_data, status_code = Servicos_Contratados_Service.create_service(request_data, user_id)
    return Response(
        response=json.dumps(response_data),
        status=status_code,
        mimetype="application/json"
    )
  
  def update_service(self, service_id):
    request_data = request.json
    
    response_data, status_code = Servicos_Contratados_Service.update_service(service_id, request_data)
    return Response(
        response=json.dumps(response_data),
        status=status_code,
        mimetype="application/json"
    )
    
  def get_services_by_client(self):
    user_id = request.headers.get('user_id')
    response_data, status_code = Servicos_Contratados_Service.get_services_by_client(user_id)
    return Response(
        response=json.dumps(response_data),
        status=status_code,
        mimetype="application/json"
    )

# Define the blueprint
servicos_contratados_blueprint = Servicos_Contratados_Controller("servicos_contratados", __name__)
