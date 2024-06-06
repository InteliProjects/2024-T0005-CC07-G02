from flask import Blueprint, request, Response, json
from src.services.servico_usuario_service import ServicoUsuarioService

class ServicoUsuarioController(Blueprint):
    def __init__(self, name, import_name):
        super().__init__(name, import_name)
        
        self.route("/servico_usuario", methods=["POST"])(self.criar_relacao_servico_usuario)
        self.route("/servico_usuario/usuario/<string:id_usuario>", methods=["GET"])(self.buscar_relacao_por_usuario)
        self.route("/servico_usuario/<string:id_relacao>", methods=["PUT"])(self.atualizar_relacao_servico_usuario)
        self.route("/servico_usuario/<string:id_relacao>", methods=["DELETE"])(self.deletar_relacao_servico_usuario)
    
    def criar_relacao_servico_usuario(self):
        dados_relacao = request.json
        response_data, status_code = ServicoUsuarioService.criar_relacao_servico_usuario(dados_relacao)
        return Response(
            response=json.dumps(response_data),
            status=status_code,
            mimetype='application/json'
        )
    
    def buscar_relacao_por_usuario(self, id_usuario):
        response_data, status_code = ServicoUsuarioService.buscar_relacao_por_usuario(id_usuario)
        return Response(
            response=json.dumps(response_data),
            status=status_code,
            mimetype='application/json'
        )
    
    def atualizar_relacao_servico_usuario(self, id_relacao):
        novos_dados = request.json
        response_data, status_code = ServicoUsuarioService.atualizar_relacao_servico_usuario(id_relacao, novos_dados)
        return Response(
            response=json.dumps(response_data),
            status=status_code,
            mimetype='application/json'
        )
    
    def deletar_relacao_servico_usuario(self, id_relacao):
        response_data, status_code = ServicoUsuarioService.deletar_relacao_servico_usuario(id_relacao)
        return Response(
            response=json.dumps(response_data),
            status=status_code,
            mimetype='application/json'
        )

# Define the blueprint
servico_usuario_blueprint = ServicoUsuarioController("servico_usuario", __name__)
