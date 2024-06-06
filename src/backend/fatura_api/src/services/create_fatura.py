import requests

def fatura_gen(servico, plano, fatura, soma, categoria, auth_token):
    resposta_servicos = mock_requests_get(servico, headers={'Authorization': f'Bearer {auth_token}'})
    # headers = {'Authorization': f'Bearer {auth_token}'}
    # resposta_servicos = requests.get(servico, headers=headers)
    planos = []
    
    if resposta_servicos.status_code == 200:
        data = resposta_servicos.json().get('data')
        for servico in data:
            planos.append(servico.get('id_plano'))
    else:
        return {'error_message': 'Erro ao consultar API1'}

    resposta_planos = requests.get(plano)

    if resposta_planos.status_code == 200:
        data = resposta_planos.json().get('data')
        for plano in data:
            if plano.get('id') in planos:
                plano_info = {
                    "categoria": categoria,  # Adiciona a categoria ao plano
                    "nome_do_plano": plano.get("nome_do_plano"),
                    "valor": plano.get("valor")
                }
                fatura.append(plano_info)
                soma += float(plano.get("valor", 0))
    else:
        return {'error_message': 'Erro ao consultar API2'}

    return {'fatura': fatura, 'soma': soma}


def consultar_servicos_logic(auth_token):
    lista_fatura = []
    soma = 0

    # Tuplas de URLs de serviço, plano e suas categorias
    servicos_e_planos = [
        ('http://10.99.61.189/servicos_contratados_internet',
         'http://10.99.61.189/planos_internet', 'internet'),
        ('http://10.99.61.189/servicos_contratados_telefonia', 
         'http://10.99.61.189/planos_telefonia', 'telefonia'),
        ('http://10.99.61.189/servicos_contratados_outros', 
         'http://10.99.61.189/planos_outros', 'outros'),
        # Adicione mais se necessário
    ]

    print('Consultando APIs')

    for servico_url, plano_url, categoria in servicos_e_planos:
        resultado = fatura_gen(servico_url, plano_url, lista_fatura, soma, categoria, auth_token)
        
        if resultado.get('error_message'):
            return {'message': resultado['error_message']}, 500
        
        lista_fatura = resultado['fatura']
        soma = resultado['soma']

    # Organizar faturas por categoria
    faturas_organizadas = {}
    for item in lista_fatura:
        categoria = item.pop('categoria')  # Remove e captura a categoria
        if categoria not in faturas_organizadas:
            faturas_organizadas[categoria] = []
        faturas_organizadas[categoria].append(item)

    return {'data': faturas_organizadas, 'valor_total': soma}, 200



def mock_requests_get(url, headers=None):
    """
    Esta função simula a resposta da função requests.get com dados mockados.
    """
    # Mock de resposta para servicos_contratados_internet
    if 'servicos_contratados_internet' in url:
        return MockResponse({
            'data': [{'id_plano': '1'}, {'id_plano': '2'}]
        }, 200)
    # Mock de resposta para planos_internet
    elif 'planos_internet' in url:
        return MockResponse({
            'data': [
                {'id': '1', 'nome_do_plano': 'Plano Internet 100MB', 'valor': '99.99'},
                {'id': '2', 'nome_do_plano': 'Plano Internet 200MB', 'valor': '199.99'}
            ]
        }, 200)
    # Adicione mais condições conforme necessário
    else:
        # Retorno genérico para URLs não mapeadas
        return MockResponse({'error_message': 'URL não mapeada'}, 404)

class MockResponse:
    """
    Esta classe simula um objeto de resposta que requests.get normalmente retornaria.
    """
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data
