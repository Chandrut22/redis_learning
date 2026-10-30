import redis 

r = redis.Redis(
    host="localhost",port=6379,db=0,
    decode_responses=True
)

print(r.ping())

# Connection pool (recommended for apps with many callers)
# pool = redis.ConnectionPool(host='localhost', port=6379, db=0, max_connections=20)
# r = redis.Redis(connection_pool=pool)


# Connecting via a URL (e.g. from an env var)
# r = redis.from_url('redis://:password@localhost:6379/0')