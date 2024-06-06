from flask import Blueprint, request, Response, json
from src.services.endereco_services import Endereco_Service

class Enderecos_Controller(Blueprint):
    def __init__(self, name, import_name):
        super().__init__(name, import_name)
        
        self.route("/", methods=["GET"])(self.get_all_enderecos)
        self.route("/<string(36):endereco_id>", methods=["GET"])(self.get_endereco_by_id)
        self.route("/", methods=["POST"])(self.create_endereco)
        self.route("/<string(36):endereco_id>", methods=["PUT"])(self.update_endereco)
        self.route("/<string(36):endereco_id>", methods=["DELETE"])(self.delete_endereco)
    
    def get_all_enderecos(self):
        response_data, status_code = Endereco_Service.get_all_enderecos()
        return Response(
            response=json.dumps(response_data),
            status=status_code,
            mimetype="application/json"
        )
    
    def get_endereco_by_id(self, endereco_id):
        response_data, status_code = Endereco_Service.get_endereco_by_id(endereco_id)
        return Response(
            response=json.dumps(response_data),
            status=status_code,
            mimetype="application/json"
        )
        
    def create_endereco(self):
        endereco_data = request.json
        response_data, status_code = Endereco_Service.create_endereco(endereco_data)
        return Response(
            response=json.dumps(response_data),
            status=status_code,
            mimetype="application/json"
        )
    
    def update_endereco(self, endereco_id):
        endereco_data = request.json
        response_data, status_code = Endereco_Service.update_endereco(endereco_id, endereco_data)
        return Response(
            response=json.dumps(response_data),
            status=status_code,
            mimetype="application/json"
        )
        
    def delete_endereco(self, endereco_id):
        response_data, status_code = Endereco_Service.delete_endereco(endereco_id)
        return Response(
            response=json.dumps(response_data),
            status=status_code,
            mimetype="application/json"
        )

# Define the blueprint
endereco_blueprint = Enderecos_Controller("endereco", __name__)
