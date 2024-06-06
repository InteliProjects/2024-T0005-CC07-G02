# Grupo-2
<table>
<tr>
<td>
<a href= "https://www.vivo.com.br/"> <img src="artefatos/img/vivo-logo.png" alt="vivo.com.br" border="0" width="20%"></a>
</td>
<td><a href= "https://www.inteli.edu.br/"><img src="artefatos/img/inteli-logo.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0" width="50%"></a>
</td>
</tr>
</table>

# Introdução

Este é o repositório dos arquivos dos alunos do Módulo 7 do curso de Ciência da Computação do Inteli no 1º trimestre de 2024. Durante este trimestre está sendo desenvolvido um projeto em parceria com a Vivo.

# Projeto: *VIVINHO*

# Grupo: *GRUPO 2*

# Integrantes:

* [Enya Arruda](mailto:Enya.Arruda@sou.inteli.edu.br)
* [Fábio Lopes](mailto:Fabio.Lopes@sou.inteli.edu.br)
* [Mariana Görresen](mailto:Mariana.Gorresen@sou.inteli.edu.br)
* [Samuel Lucas](mailto:Samuel.Almeida@sou.inteli.edu.br)
* [Raab Iane](mailto:Raab.Silva@sou.inteli.edu.br)

# Descrição

Nosso projeto visa resolver um problema comum em sistemas de banco de dados antigos: o tempo demorado de resposta às consultas, que pode chegar a 30 segundos. Para melhorar essa experiência e tornar nossas aplicações mais ágeis, seguras e confiáveis, estamos implementando uma solução na nuvem, especificamente na AWS. Esta solução utiliza um método chamado "cache", que armazena temporariamente informações frequentemente acessadas, permitindo que as consultas sejam respondidas em um tempo muito mais curto, geralmente abaixo de 3 segundos. Com isso, esperamos proporcionar aos nossos usuários uma experiência mais rápida e eficiente, garantindo a escalabilidade, elasticidade, tolerância a falhas e disponibilidade do sistema.

# Configuração para desenvolvimento

## Backend

### Pré-requisitos
Python 3.8 ou superior<br>
pip<br>
Docker<br>
Acesso à Internet

### Configuração Local

1. Crie e ative um ambiente virtual para evitar conflitos de dependências:
    ```
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```
2. Instale as dependências necessárias:
    ```
    pip install -r requirements.txt
    ```
3. Antes de iniciar a aplicação, configure o banco de dados:
    ```
    flask db init
    flask db migrate
    flask db upgrade
    ```

### Execução via Docker

1. Use o Docker Compose para iniciar os serviços:
    ```
    docker-compose up -d
    ```
2. Após iniciar os serviços, configure o banco de dados:
    ```
    docker-compose exec web flask db init
    docker-compose exec web flask db migrate
    docker-compose exec web flask db upgrade
    ```

### Configurações Adicionais

**Portas**: Verifique as portas no docker-compose.yml e .env para evitar conflitos.<br>
**Variáveis de Ambiente**: Ajuste as variáveis de ambiente em .env conforme necessário.

### Acessando a API

Acesse e teste a API utilizando a coleção Postman disponível aqui:

[![Run in Postman](https://run.pstmn.io/button.svg)](https://www.postman.com/science-meteorologist-76826278/workspace/umberto-api/collection/23984859-a0e96e62-e0d4-4364-af16-e46d61d2cc32?action=share&creator=23984859)

## Frontend

### Pré-requisitos

Node.js<br>
npm

### Configuração Local

1. Instale as dependências necessárias:
    ```
    npm install
    # ou
    yarn install
    ```

2. Inicie o servidor de desenvolvimento:
    ```
    npm run dev
    # ou
    yarn dev
    ```

# Documentação

Os arquivos da documentação deste projeto estão na pasta [/artefatos](artefatos).

# Releases

* SPRINT1:
    - MVP com deploy da aplicação com arquitetura básica
    - Entendimento de Negócio
    - Requisitos Funcionais e Não Funcionais
    - Entendimento do Usuário

* SPRINT2:
    - Arquitetura corporativa
    - Front-end da aplicação
    - Back-end da aplicação
    - Artigo - versão inicial

* SPRINT3:
    - Modelagem e Implementação
    - Relatório técnico
    - Artigo - 2a versão
 
* SPRINT4:
    - Testes do sistema
    - Definição da aplicação
    - Artigo - 3a versão

* SPRINT5:
    - Apresentação final
    - Refinamentos da aplicação
    - Artigo completo
    - Organização do repositório do Github

## 📋 Licença/License

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/">

<a property="dct:title" rel="cc:attributionURL">Consilium</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName">Inteli, Enya Arruda, Fábio Lopes, Mariana Görresen, Samuel Lucas and Raab Iane</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
