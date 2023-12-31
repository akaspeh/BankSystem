from flask import jsonify
from .DBs.Redis import *
from .DBs.PostGres import *
from .DBs.Mongo import *
from .DBs.Config import *
import logging
import redis
from datetime import *
from BackEnd.Classes.BANK import BANK
from BackEnd.utils.SecurityUtils import Security

class DBsystem:
    def __init__(self):
        self.redis = Redis(host=ConfigRedis.host, port=ConfigRedis.port, db=ConfigRedis.db)
        self.postgres = PostGres(host=ConfigPostgres.host, db=ConfigPostgres.db,
                            username=ConfigPostgres.user, password=ConfigPostgres.password)
        self.mongo1 = MongoClient('mongodb://mymongoadmin:mymongopassword@127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.1.0')



    def create_tables(self):
        with self.postgres.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            try:
                cursor.execute(
                    f"CREATE TABLE IF NOT EXISTS USERS("
                    f"id SERIAL PRIMARY KEY,"
                    f"name text, "
                    f"email text, "
                    f"phone text,"
                    f"address text, "
                    f"balance FLOAT DEFAULT 0,"
                    f"role text)")

                cursor.execute(
                    f"CREATE TABLE IF NOT EXISTS LOANS ("
                    f"id SERIAL PRIMARY KEY, "
                    f"date_open TIMESTAMP,"
                    f"date_close TIMESTAMP,"
                    f"amount FLOAT,"
                    f"interest_rate FLOAT,"
                    f"user_id bigint REFERENCES USERS(id))")

                cursor.execute(
                    f"CREATE TABLE IF NOT EXISTS TRANSACTIONS ("
                    f"id SERIAL PRIMARY KEY, "
                    f"data TIMESTAMP, "
                    f"amount FLOAT, "
                    f"description text,"
                    f"user_id_sender bigint REFERENCES USERS(id),"
                    f"user_id_reciver bigint REFERENCES USERS(id))")
            except Exception as e:
                logging.error(e)

    def createAdmins(self):
        self.adminSignIn('Admin1', 'admin@email', '123456')

    def adminSignIn(self, name, email, password):
        security = Security()
        security.hash.update(email[0:5].encode('utf-8'))
        emailHashed = security.hash.hexdigest()
        if self.redis_get_element(emailHashed) == 'false':
            security.hash.update(password.encode('utf-8'))
            passwordHashed = security.hash.hexdigest()
            self.redis.redis_client.set(name=emailHashed, value=passwordHashed)

            with self.postgres.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                try:
                    cursor.execute(f"INSERT INTO USERS(name, email, role) "
                                   f"VALUES('{name}', '{email}', 'admin')")
                except Exception as e:
                    logging.error(e)



    def redis_get_element(self, key):
        value = self.redis.redis_client.get(key)

        if value is None:
            return 'false'
        else:
            return value


    def audit_insert_info(self, operation, user_name, user_id):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        access_mongo_doc = self.mongo1['SystemEventsTracing']
        collection = access_mongo_doc['AuditCollection']

        document = {'action': operation, 'user_name': user_name, 'user_id': user_id, 'date': now}
        result = collection.insert_one(document)
        print(f'Inserted document id: {result.inserted_id}')

    def get_data_mongo(self, action):
        access_mongo_db = self.mongo1['SystemEventsTracing']
        collection = access_mongo_db['AuditCollection']

        if action == 'signin':
            filter_criteria = {"action": "Signed In"}
        elif action == 'transaction':
            filter_criteria = {"action": "Made a Transaction"}
        elif action == 'loan':
            filter_criteria = {"action": "Applied for a Loan"}
        else:
            filter_criteria = {}

        documents = list(collection.find(filter_criteria, {"_id": 0}))
        return documents
