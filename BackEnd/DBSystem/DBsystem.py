
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
                    f"CREATE TABLE IF NOT EXISTS CUSTOMERS ("
                    f"id bigint PRIMARY KEY,"
                    f"name text, "
                    f"email text, "
                    f"phone text, address text, role text)")

                cursor.execute(
                    f"CREATE TABLE IF NOT EXISTS CUSTOMER_PURCHASE ("
                    f"id bigint PRIMARY KEY, "
                    f"date text, "
                    f"amount FLOAT, "
                    f"description text," #можна в дату спробувати тип даних date
                    f"Product_and_services_code bigint REFERENCES CUSTOMERS(id), "
                    f"cusomer_id bigint REFERENCES CUSTOMERS(id))")

                cursor.execute(
                    f"CREATE TABLE IF NOT EXISTS MERCHANTS ("
                    f"id bigint PRIMARY KEY, "
                    f"name text, "
                    f"email text,"
                    f"phone text, "
                    f"address text)")

                cursor.execute(
                    f"CREATE TABLE IF NOT EXISTS PRODUCT_AND_SERVICES ("
                    f"code bigint PRIMARY KEY, "
                    f"description text, "
                    f"merchant_id bigint REFERENCES MERCHANTS(id))")

                cursor.execute(
                    f"CREATE TABLE IF NOT EXISTS ACCOUNTS_TYPES ("
                    f"code int PRIMARY KEY, "
                    f"type text)")

                cursor.execute(
                    f"CREATE TABLE IF NOT EXISTS ACCOUNTS ("
                    f"id bigint PRIMARY KEY, "
                    f"name text, "
                    f"cusomer_id bigint REFERENCES CUSTOMERS(id),"
                    f"account_code int REFERENCES ACCOUNTS_TYPES(code))")

                cursor.execute(
                    f"CREATE TABLE IF NOT EXISTS TRANSACTIONS ("
                    f"id bigint PRIMARY KEY, "
                    f"data TIMESTAMP, "
                    f"amount FLOAT, "
                    f"description text, "
                    f"purchase_id bigint REFERENCES CUSTOMER_PURCHASE(id) ,"
                    f"account_id bigint REFERENCES ACCOUNTS(id))")



            except Exception as e:
                logging.error(e)
