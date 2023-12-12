import psycopg2

class PostGresDB:
    def __inti__(self, host, db, username, password):
        conn = psycopg2.connect(host=host, db=db, username=username, password=password)

