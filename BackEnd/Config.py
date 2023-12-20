from configparser import ConfigParser

parser = ConfigParser()
class ConfigPostgres:
    host = 'localhost'
    db = "postgres"
    user = "myuser"
    password = "mypassword"
    port = "5432:5432"

class ConfigMongo():
    host = 'localhost'
    db = 'mongo'
    user = 'mymongoadmin'
    password = 'mymongopassword'
    port = 27017

class ConfigRedis():
    host = 'localhost'
    db = 0
    password = "myredispassword"
    port = 6379
