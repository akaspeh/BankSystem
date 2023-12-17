import psycopg2
import psycopg2.extras

class PostGres:
    def __init__(self, host, db, username, password):
        self.conn = psycopg2.connect(host=host, database=db, user=username, password=password)
        self.conn.autocommit = True