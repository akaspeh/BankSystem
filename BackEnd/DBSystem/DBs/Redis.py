import redis

class Redis:
    def __init__(self, host, port, db):
        self.redis_client = redis.Redis(host=host, port=port, db=db)