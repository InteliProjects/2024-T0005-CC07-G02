import redis

# Substitua 'redis_host' pelo IP ou nome do host do seu servidor Redis
# Substitua '6379' pela porta em que o Redis está executando
# Se você estiver usando senha, adicione-a com o parâmetro 'password'
redis_client = redis.Redis(host='cache-vivinho-1-hlnpck.serverless.use1.cache.amazonaws.com', port=6379, db=0, decode_responses=True, ssl=True)

# Testando a conexão
redis_client.setex('test', 10* 60, '123')
print(redis_client.get('test'))
