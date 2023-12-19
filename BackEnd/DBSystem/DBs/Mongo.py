from pymongo import MongoClient

class Mongo:
    def __init__(self, host, port):
        try:
            self.mongo_client = MongoClient(host=host, port=port)
            print("[+] Database connected!")
        except Exception as e:
            print("[+] Database connection error!")
            raise e
