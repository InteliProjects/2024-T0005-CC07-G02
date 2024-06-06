from flask import Blueprint, request, Response, json
from src.services.users_service import User_Service

class Auth_Controller(Blueprint):
  def __init__(self, name, import_name):
    super().__init__(name, import_name)
    
    self.route("/login", methods=["POST"])(self.login)
    self.route("/register", methods=["POST"])(self.registro)
    self.route("/logout", methods=["POST"])(self.logout)
    
  def login(self):
    request_data = request.json
    
    response_data, status_code = User_Service.login(request_data)
    return Response(
      response=json.dumps(response_data),
      status=status_code,
      mimetype="application/json"
    )
    
  def registro(self):
    request_data = request.json
    
    response_data, status_code = User_Service.registro(request_data)
    return Response(
      response=json.dumps(response_data),
      status=status_code,
      mimetype="application/json"
  )
    
  def logout(self):
    request_data = request.json
    
    response_data, status_code = User_Service.decodeToken(request_data)
    return Response(
      response=json.dumps(response_data),
      status=status_code,
      mimetype="application/json"
    )
    
auth_blueprint = Auth_Controller("auth", __name__)