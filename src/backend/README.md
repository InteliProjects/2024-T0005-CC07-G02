# Projeto Morto API

Bem-vindo ao repositório da Morto API! Este guia rápido ajudará você a configurar e rodar o projeto localmente ou utilizando Docker, conforme sua preferência.

## Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Docker (para execução via Docker)
- Acesso à Internet para download de dependências

## Configuração Local

Para rodar o projeto localmente, siga estes passos:

1. **Configurar o Ambiente Virtual:**

   É recomendado o uso de um ambiente virtual para evitar conflitos de dependências. Para criá-lo e ativá-lo, execute:

   ```
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

2. **Instalar Dependências:**

   Com o ambiente virtual ativado, instale as dependências necessárias com:

   ```
   pip install -r requirements.txt
   ```

3. **Configurar o Banco de Dados:**

   Antes de iniciar a aplicação, você precisará configurar o banco de dados executando:

   ```
   flask db init
   flask db migrate
   flask db upgrade
   ```

## Execução via Docker

Para rodar o projeto utilizando Docker, siga estes passos:

1. **Iniciar os Serviços:**

   Utilize o Docker Compose para construir e iniciar os serviços definidos:

   ```
   docker-compose up -d
   ```

2. **Configurar o Banco de Dados:**

   Após iniciar os serviços Docker, é necessário configurar o banco de dados. Você pode fazer isso executando os comandos Flask diretamente no serviço Docker. Exemplo:

   ```
   docker-compose exec web flask db init
   docker-compose exec web flask db migrate
   docker-compose exec web flask db upgrade
   ```

## Configurações Adicionais

- **Atenção às Portas:** Certifique-se de que as portas especificadas no arquivo `docker-compose.yml` e no arquivo `.env` estejam disponíveis e não entrem em conflito com outros serviços.

- **Variáveis de Ambiente:** Para customizações adicionais, você pode ajustar as variáveis de ambiente definidas no arquivo `.env`.

## Acessando a API

A API pode ser acessada e testada utilizando o seguinte link do Postman:

[![Run in Postman](https://run.pstmn.io/button.svg)](https://www.postman.com/science-meteorologist-76826278/workspace/umberto-api/collection/23984859-a0e96e62-e0d4-4364-af16-e46d61d2cc32?action=share&creator=23984859)

Utilize esta coleção para explorar os endpoints disponíveis e testar a funcionalidade da API.

---

Com estas instruções, você deve ser capaz de configurar e executar a Morto API tanto localmente quanto via Docker. Se tiver alguma dúvida ou encontrar problemas, sinta-se livre para abrir uma issue no repositório.