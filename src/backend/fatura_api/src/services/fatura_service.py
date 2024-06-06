import boto3
import json
from src.utils import Logging

logger = Logging()

# Configurações do cliente SQS
sqs_client = boto3.client('sqs', region_name='', aws_access_key_id='', aws_secret_access_key='')
queue_url = ''

class Fatura_Service:
    @staticmethod
    def send_message_to_queue(action, data):
        """Envia uma mensagem para a fila SQS com a ação e os dados fornecidos."""
        message_body = json.dumps({"action": action, "data": data})
        response = sqs_client.send_message(QueueUrl=queue_url, MessageBody=message_body)
        return response['MessageId']

    @staticmethod
    def create_fatura(id_cliente, itens=[]):
        message_id = Fatura_Service.send_message_to_queue("create_fatura", {"id_cliente": id_cliente, "itens": itens})
        logger.log_info(f"Fatura enviada para a fila SQS para criação: MessageId {message_id}")
        return {"status": "success", "message": "Fatura enviada para processamento", "data": {"id_cliente": id_cliente, "itens": itens}}, 202

    @staticmethod
    def update_fatura(id, id_cliente=None, itens=[], pago=None, data_pagamento=None):
        message_id = Fatura_Service.send_message_to_queue("update_fatura", {"id": id, "id_cliente": id_cliente, "itens": itens, "pago": pago, "data_pagamento": data_pagamento})
        logger.log_info(f"Pedido de atualização de fatura enviado para a fila SQS: MessageId {message_id}")
        return {"status": "success", "message": "Pedido de atualização enviado para processamento"}, 202

    @staticmethod
    def get_all_faturas(client_id):
        # Enviar pedido de listagem pode ser menos comum, dependendo da arquitetura do sistema
        message_id = Fatura_Service.send_message_to_queue("get_all_faturas", {"client_id": client_id})
        logger.log_info(f"Pedido de listagem de faturas enviado para a fila SQS: MessageId {message_id}")
        return {"status": "success", "message": "Pedido de listagem enviado para processamento"}, 202

    @staticmethod
    def get_fatura_by_id(id):
        message_id = Fatura_Service.send_message_to_queue("get_fatura_by_id", {"id": id})
        logger.log_info(f"Pedido de obtenção de fatura por ID enviado para a fila SQS: MessageId {message_id}")
        return {"status": "success", "message": "Pedido de obtenção enviado para processamento"}, 202

    @staticmethod
    def delete_fatura(id):
        message_id = Fatura_Service.send_message_to_queue("delete_fatura", {"id": id})
        logger.log_info(f"Pedido de exclusão de fatura enviado para a fila SQS: MessageId {message_id}")
        return {"status": "success", "message": "Pedido de exclusão enviado para processamento"}, 202
