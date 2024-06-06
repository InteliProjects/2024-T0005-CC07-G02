from datetime import timedelta
from flask import Flask, jsonify, request
import requests
from redis import Redis
import jwt
from dotenv import load_dotenv
import os
import json

app_gateway = Flask(__name__)

# Conexão com o Redis (ajuste as configurações conforme necessário)
redis_client = Redis(host='cache-vivinho-1-hlnpck.serverless.use1.cache.amazonaws.com', port=6379, db=0, decode_responses=True, ssl=True)

# Definindo o mapeamento dos caminhos para as URLs das APIs
API_ENDPOINTS = {
    "planos_internet": "http://ec2-54-147-135-22.compute-1.amazonaws.com/api/plans/",
    "servicos_contratados_internet": "http://ec2-54-147-135-22.compute-1.amazonaws.com/api/services/client/",
    "planos_telefonia": "http://10.110.93.30/api/plans/",
    "servicos_contratados_telefonia": "http://10.110.93.30/api/services/client/",
    "planos_outros": "http://10.97.254.93/api/plans/",
    "servicos_contratados_outros": "http://10.97.254.93/api/services/client/",
    "fatura": "http://10.96.161.113/api/fatura/",
}

# Função auxiliar para decodificar o JWT e extrair o user_id
def get_user_id_from_jwt(token):
    load_dotenv()
    secret_key = os.getenv('SECRET_KEY')
    try:
        decoded_token = jwt.decode(token, secret_key, algorithms=['HS256'])
        return decoded_token.get('user_id')
    except jwt.ExpiredSignatureError:
        print("O token expirou.")
        return None
    except jwt.InvalidTokenError:
        print("Token inválido.")
        return None

@app_gateway.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_gateway(path):
    user_id = None
    
    # Tenta extrair o user_id do JWT no cabeçalho de autorização
    if 'Authorization' in request.headers:
        try:
            token = request.headers['Authorization'].split(' ')[1]  # Remove "Bearer" se estiver presente
            user_id = get_user_id_from_jwt(token)
            print(user_id)
        except IndexError:
            return jsonify({"error": "Token de autorização malformado."}), 400

    # Identifica a chave do serviço baseado na primeira parte do caminho
    path_parts = path.split('/')
    service_key = path_parts[0]
    resource_id = '/'.join(path_parts[1:])
    if resource_id == user_id:
        cache_key = f"user:{user_id}:{service_key}/"
    else:
        cache_key = f"user:{user_id}:{service_key}/{resource_id}"

    if request.method == 'GET' and user_id:
        cached_data = redis_client.get(cache_key)
        print(cache_key)
        if cached_data:
            transformed_str = cached_data.replace("'", '"')
            data_obj = json.loads(transformed_str)
            print(data_obj)
            return data_obj, 200, request.headers.items()

    if service_key in API_ENDPOINTS:
        # Ajusta a URL base para a API destino sem adicionar o 'path' novamente
        api_url = API_ENDPOINTS[service_key] + resource_id
        print(f"Encaminhando solicitação para {api_url}")
        
        # Copia os headers, possivelmente modificando ou removendo alguns
        # headers = {key: value for key, value in request.headers if key != 'Host'}
        # Copia apenas o header de autenticação, se presente
        headers = {}
        if 'Authorization' in request.headers:
            headers['Authorization'] = request.headers['Authorization']
        if request.method in ['POST', 'PUT']:
            headers['Content-Type'] = 'application/json'

        # Encaminha a solicitação para a API correspondente
        response = requests.request(
            method=request.method, 
            url=api_url, 
            headers=headers, 
            data=request.data, 
            params=request.args
        )

        t = json.loads(response.text)

        # Para DELETE, remove a entrada do cache
        if request.method == 'DELETE':
            redis_client.delete(cache_key)

        # Se a resposta é bem-sucedida e é uma requisição GET, armazena no cache
        if response.status_code == 200 and request.method == 'GET':
            redis_client.setex(cache_key, 10 * 60, str(t))

        return (response.content, response.status_code, response.headers.items())
    elif service_key == "health":
        return "API Gateway is running", 200
    else:
        return "Serviço não encontrado", 404

if __name__ == '__main__':
    app_gateway.run(host='0.0.0.0', port=5000)
    
