# Usar uma imagem base do Python (especificamente a versão slim para economizar espaço)
FROM python:3.9

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de dependências para o diretório atual
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos da aplicação para o diretório de trabalho
COPY . .

# Define a variável de ambiente para indicar que a aplicação está rodando em um container
ENV FLASK_RUN_HOST=0.0.0.0

# Expõe a porta que o Flask usará
EXPOSE 80

# Comando para executar a aplicação
CMD ["flask", "run", "--port=80"]
