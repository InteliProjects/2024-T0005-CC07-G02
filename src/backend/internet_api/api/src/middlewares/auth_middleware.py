import jwt
import os
from flask import Flask, jsonify, request, g
from werkzeug.datastructures import Headers

class Auth_Middleware:
    # Chave secreta para assinar o token JWT
    SECRET_KEY = os.environ.get('SECRET_KEY')

    def __init__(self, app):
        self.app = app
        self.sessions = {}

    def __call__(self, environ, start_response):
        return self.app(environ, start_response)

    def before_request(self):
        auth_header = request.headers.get('Authorization')

        if auth_header is None:
            return jsonify({'error': 'Authorization header is required'}), 401

        auth_parts = auth_header.split(' ')
        if len(auth_parts) != 2 or auth_parts[0].lower() != 'bearer':
            return jsonify({'error': 'Invalid Authorization header'}), 401
        
        token = auth_parts[1] # assumindo que o token está no formato 'Bearer <token'
        # token = jwt.encode({'sub': '1234567890', 'user_id': '0f4f87e7-6505-4937-8ee1-9c25b9d9f423', 'name': 'Jonye', 'iat': 1516239022}, self.SECRET_KEY, algorithm='HS256')
        # print('TOKEN:')
        # print(token)
        
        # Decodificação do token para obter o header e o payload
        try:
            header = jwt.get_unverified_header(token)
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=['HS256'])
            print('HEADER:')
            print(header)
            print('PAYLOAD:')
            print(payload)
            user_id = payload.get('user_id')
            self.sessions[user_id] = payload
            
            modified_headers = Headers(request.headers)
            modified_headers.add('user_id', user_id)
            
            request.headers = modified_headers
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Expired token'}), 401
        except jwt.InvalidTokenError:
            print('Invalid token')
            return jsonify({'error': 'Invalid token'}), 401