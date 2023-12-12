import psycopg2

class PostGres:
    def __init__(self, host, db, username, password):
        conn = psycopg2.connect(host=host, db=db, username=username, password=password)

