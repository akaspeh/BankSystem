from pymongo import MongoClient

class Mongo:

    def __init__(self, host, port):
        self.mongo_client = MongoClient(host=host, port=port)