
import psycopg2
from DBs.Redis import *
from DBs.PostGres import *
from DBs.Mongo import *

from BackEnd.Config import *

import logging
import psycopg2.extras

class DBsystem:
    redis = Redis(host=ConfigRedis.host, port=ConfigRedis.port, db=ConfigRedis.db, password=ConfigRedis.password,
                       decode_responses=True)
    postgres = PostGres(host=ConfigPostgres.host, port=ConfigPostgres.port, db=ConfigPostgres.db,
                        username=ConfigPostgres.user, password = ConfigPostgres.password)

    def create_tables(self):
        with self.postgres.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            try:
                cursor.execute("CREATE TABLE IF NOT EXISTS")

            except Exception as e:
                logging.error(e)



redis_instance = Redis(host=ConfigRedis.host, port=ConfigRedis.port, db=ConfigRedis.db, password=ConfigRedis.password,
                       decode_responses=True)




