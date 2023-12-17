
from BackEnd.DBSystem.DBs.Redis import *
from BackEnd.DBSystem.DBs.PostGres import *
from BackEnd.DBSystem.DBs.Mongo import *
from BackEnd.Config import *
import logging




class DBsystem:
    def __init__(self):
        self.redis = Redis(host=ConfigRedis.host, port=ConfigRedis.port, db=ConfigRedis.db, password=ConfigRedis.password,
                      decode_responses=True)
        self.postgres = PostGres(host=ConfigPostgres.host, db=ConfigPostgres.db,
                            username=ConfigPostgres.user, password=ConfigPostgres.password)
        self.mongo = Mongo(host=ConfigMongo.host, port=ConfigMongo.port)

    def create_tables(self):
        with self.postgres.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            try:
                cursor.execute(
                    f"CREATE TABLE IF NOT EXISTS USERS ("
                    f"id SERIAL PRIMARY KEY,"
                    f"name text, "
                    f"email text, "
                    f"phone text,"
                    f"address text, "
                    f"role text)")

                cursor.execute(
                    f"CREATE TABLE IF NOT EXISTS LOANS ("
                    f"loan_id SERIAL PRIMARY KEY, "
                    f"amount FLOAT,"
                    f"data TIMESTAMP,"
                    f"interest_rate FLOAT,"
                    f"user_id bigint REFERENCES USERS(id))")

                cursor.execute(
                    f"CREATE TABLE IF NOT EXISTS CARDS ("
                    f"card SERIAL PRIMARY KEY, "
                    f"balance FLOAT,"
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
    def redis_get_element(self, key):
        value = self.dbsystem.redis.get(key)

        if value is None:
            return 'false'
        else:
            return value



