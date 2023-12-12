from DBs.Redis import Redis
from BackEnd.Config import ConfigRedis


redis_instance = Redis(host=ConfigRedis.host, port=ConfigRedis.port, db=ConfigRedis.db, password=ConfigRedis.password,
                       decode_responses=True)




