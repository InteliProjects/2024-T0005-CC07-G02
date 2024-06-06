from flask import Blueprint, request, Response, json
from src.services.planos_service import Planos_Service

class Planos_Controller(Blueprint):
  def __init__(self, name, import_name):
    super().__init__(name, import_name)
    
    self.route("/", methods=["GET"])(self.get_all_plans)
    self.route("/<string(36):plan_id>", methods=["GET"])(self.get_plan_by_id)
    self.route("/<string:service_type>", methods=["GET"])(self.get_plan_by_service_type)
    self.route("/<string(36):plan_id>", methods=["DELETE"])(self.delete_plan)
    self.route("/", methods=["POST"])(self.create_plan)
    self.route("/<string(36):plan_id>", methods=["PUT"])(self.update_plan)

  def get_all_plans(self):
    response_data, status_code = Planos_Service.get_all_plans()
    return Response(
      response=json.dumps(response_data),
      status=status_code,
      mimetype="application/json"
    )
  
  def get_plan_by_id(self, plan_id):
    response_data, status_code = Planos_Service.get_plan_by_id(plan_id)
    return Response(
      response=json.dumps(response_data),
      status=status_code,
      mimetype="application/json"
    )
  
  def get_plan_by_service_type(self, service_type):
    response_data, status_code = Planos_Service.get_plan_by_service_type(service_type)
    return Response(
      response=json.dumps(response_data),
      status=status_code,
      mimetype="application/json"
    )
    
  def delete_plan(self, plan_id):
    response_data, status_code = Planos_Service.delete_plan(plan_id)
    return Response(
      response=json.dumps(response_data),
      status=status_code,
      mimetype="application/json"
    )
  
  def create_plan(self):
    request_data = request.json
    
    response_data, status_code = Planos_Service.create_plan(request_data)
    return Response(
      response=json.dumps(response_data),
      status=status_code,
      mimetype="application/json"
    )
  
  def update_plan(self, plan_id):
    request_data = request.json
    
    response_data, status_code = Planos_Service.update_plan(plan_id, request_data)
    return Response(
      response=json.dumps(response_data),
      status=status_code,
      mimetype="application/json"
    )
  
  
# Define the blueprint
planos_blueprint = Planos_Controller("planos", __name__)