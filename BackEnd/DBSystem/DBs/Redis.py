import redis


class Redis:

    def __init__(self, host, port, db, password, decode_responses):
        self.redis_client = redis.StrictRedis(host=host, port=port, db=db, password=password, decode_responses=decode_responses)
