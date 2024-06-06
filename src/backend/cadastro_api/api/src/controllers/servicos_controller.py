from flask import Blueprint, request, Response, json
from src.services.servico_services import Servico_Service 

class ServicosController(Blueprint):
    def __init__(self, name, import_name):
        super().__init__(name, import_name)

        self.route("/", methods=["GET"])(self.get_all_servicos)
        self.route("/<string(36):servico_id>", methods=["GET"])(self.get_servico_by_id)
        self.route("/", methods=["POST"])(self.create_servico)
        self.route("/<string(36):servico_id>", methods=["PUT"])(self.update_servico)
        self.route("/<string(36):servico_id>", methods=["DELETE"])(self.delete_servico)

    def get_all_servicos(self):
        response_data, status_code = Servico_Service.get_all_servicos()
        return Response(
            response=json.dumps(response_data),
            status=status_code,
            mimetype="application/json"
        )

    def get_servico_by_id(self, servico_id):
        response_data, status_code = Servico_Service.get_servico_by_id(servico_id)
        return Response(
            response=json.dumps(response_data),
            status=status_code,
            mimetype="application/json"
        )

    def create_servico(self):
        request_data = request.json
        response_data, status_code = Servico_Service.create_servico(request_data)
        return Response(
            response=json.dumps(response_data),
            status=status_code,
            mimetype="application/json"
        )

    def update_servico(self, servico_id):
        request_data = request.json
        response_data, status_code = Servico_Service.update_servico(servico_id, request_data)
        return Response(
            response=json.dumps(response_data),
            status=status_code,
            mimetype="application/json"
        )

    def delete_servico(self, servico_id):
        response_data, status_code = Servico_Service.delete_servico(servico_id)
        return Response(
            response=json.dumps(response_data),
            status=status_code,
            mimetype="application/json"
        )

servicos_blueprint = ServicosController("servicos", __name__)
