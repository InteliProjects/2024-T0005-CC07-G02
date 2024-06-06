from flask import Blueprint, request, Response, json
from src.services.endereco_usuario_service import EnderecoUsuarioService

class EnderecoUsuarioController(Blueprint):
    def __init__(self, name, import_name):
        super().__init__(name, import_name)
        
        self.route("/endereco_usuario", methods=["GET"])(self.get_relacao_por_usuario)
        self.route("/endereco_usuario", methods=["POST"])(self.criar_relacao_endereco_usuario)
        self.route("/endereco_usuario/<string:id_relacao>", methods=["PUT"])(self.atualizar_relacao_endereco_usuario)
        self.route("/endereco_usuario/<string:id_relacao>", methods=["DELETE"])(self.deletar_relacao_endereco_usuario)
    
    def get_relacao_por_usuario(self):
        id_usuario = request.args.get('id_usuario')
        response_data, status_code = EnderecoUsuarioService.get_relacao_por_usuario(id_usuario)
        return Response(
            response=json.dumps(response_data),
            status=status_code,
            mimetype="application/json"
        )
    
    def criar_relacao_endereco_usuario(self):
        dados_relacao = request.json
        response_data, status_code = EnderecoUsuarioService.criar_relacao_endereco_usuario(dados_relacao)
        return Response(
            response=json.dumps(response_data),
            status=status_code,
            mimetype="application/json"
        )
    
    def atualizar_relacao_endereco_usuario(self, id_relacao):
        novos_dados = request.json
        response_data, status_code = EnderecoUsuarioService.atualizar_relacao_endereco_usuario(id_relacao, novos_dados)
        return Response(
            response=json.dumps(response_data),
            status=status_code,
            mimetype="application/json"
        )
    
    def deletar_relacao_endereco_usuario(self, id_relacao):
        response_data, status_code = EnderecoUsuarioService.deletar_relacao_endereco_usuario(id_relacao)
        return Response(
            response=json.dumps(response_data),
            status=status_code,
            mimetype="application/json"
        )

# Define the blueprint
endereco_usuario_blueprint = EnderecoUsuarioController("endereco_usuario", __name__)
