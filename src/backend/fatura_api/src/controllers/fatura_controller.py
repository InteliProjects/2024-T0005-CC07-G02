from flask import Blueprint, Response, json, request
from src.services.fatura_service import Fatura_Service
from src.services.create_fatura import consultar_servicos_logic
from src.middlewares.auth_middleware import Auth_Middleware


class Fatura_Controller(Blueprint):
  def __init__(self, name, import_name):
    super().__init__(name, import_name)
        
    self.route("/", methods=["GET"])(self.get_all_faturas)
    self.route("/<string(36):fatura_id>", methods=["GET"])(self.get_fatura_by_id)
    self.route("/<string(36):fatura_id>", methods=["DELETE"])(self.delete_fatura)
    self.route("/", methods=["POST"])(self.create_fatura)
    self.route("/<string(36):fatura_id>", methods=["PUT"])(self.update_fatura)
    self.route("/api/", methods=["GET"])(self.create_fatura_from_apis)

  def get_all_faturas(self):
    user_id = request.headers.get('user_id')
    response_data, status_code = Fatura_Service.get_all_faturas(user_id)
    return Response(
        response=json.dumps(response_data),
        status=status_code,
        mimetype="application/json"
    )
  
  def get_fatura_by_id(self, fatura_id):
    response_data, status_code = Fatura_Service.get_fatura_by_id(fatura_id)
    return Response(
        response=json.dumps(response_data),
        status=status_code,
        mimetype="application/json"
    )
    
  def delete_fatura(self, fatura_id):
    response_data, status_code = Fatura_Service.delete_fatura(fatura_id)
    return Response(
        response=json.dumps(response_data),
        status=status_code,
        mimetype="application/json"
    )
  
  def create_fatura(self):
    request_data = request.json
    
    # Extract 'id_cliente' and 'itens' from the request data
    user_id = request.headers.get('user_id')
    itens = request_data.get('itens', [])  # Default to an empty list if not provided

    # Pass 'id_cliente' and 'itens' as separate arguments to the service method
    response_data, status_code = Fatura_Service.create_fatura(user_id, itens)
    return Response(
        response=json.dumps(response_data),
        status=status_code,
        mimetype="application/json"
    )
  
  def update_fatura(self, fatura_id):
    request_data = request.json
    
    # Extract data from request
    user_id = request.headers.get('user_id')
    itens = request_data.get('itens', [])
    pago = request_data.get('pago')  # Assuming these are also part of your request
    data_pagamento = request_data.get('data_pagamento')
    
    # Pass all parameters to the service
    response_data, status_code = Fatura_Service.update_fatura(
        fatura_id, id_cliente=user_id, itens=itens, pago=pago, data_pagamento=data_pagamento
    )
    return Response(
        response=json.dumps(response_data),
        status=status_code,
        mimetype="application/json"
    )

  def create_fatura_from_apis(self):
    request_data = request.json
    user_id = request.headers.get('user_id')
    auth_token = request.headers.get('Authorization')
    
    # Chamada à lógica para consultar serviços e compilar itens da fatura
    response_data, status_code = consultar_servicos_logic(auth_token)
    
    if status_code == 200:
        # Se a consulta foi bem-sucedida, criar a fatura no banco de dados
        itens = response_data.get('data', {}).get('valor_total', [])
        response_data_db, status_code_db = Fatura_Service.create_fatura(user_id, itens)
        
        return Response(
            response=json.dumps(response_data_db),
            status=status_code_db,
            mimetype="application/json"
        )
    else:
        # Em caso de falha na consulta, retornar o erro
        return Response(
            response=json.dumps({"error": "Falha ao consultar serviços."}),
            status=status_code,
            mimetype="application/json"
        )
  

# Define the blueprint
fatura_blueprint = Fatura_Controller("Fatura", __name__)
