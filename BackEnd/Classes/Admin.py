import psycopg2
import psycopg2.extras
class Admin:
    def __init__(self, dbsystem):
        self.__isAdmin = False
        self.__dbsystem = dbsystem

    def findAllTransactions(self, user_id):
        with self.__dbsystem.postgres.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            try:
                cursor.execute(
                    f"Select  ")

            except Exception as e:
                logging.error(e)