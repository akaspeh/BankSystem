
from BackEnd.DBSystem.DBs.Redis import *
from BackEnd.DBSystem.DBs.PostGres import *
from BackEnd.DBSystem.DBs.Mongo import *
from BackEnd.Config import *
import logging
from flask_cors import CORS
from flask import jsonify, request , Flask

app = Flask(__name__)
CORS(app, supports_credentials=True, methods=['GET', 'POST', 'PUT', 'DELETE'])


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
                cursor.execute(f"CREATE TABLE IF NOT EXISTS users (id bigint, email text, password text, firstname text, lastname text,"
                           f"phone text, address text)")

            except Exception as e:
                logging.error(e)

    @app.route('/api/auth/login', methods=['POST'])
    def get_user():
        data = request.get_json()
        email = data['email']
        password = data['password']

        print(email)

        # Перетворюємо об'єкт на словник перед серіалізацією в JSON
        result_dict = {
            'userDto': {
                'id': "awdad",
                'userName': "adawda",
                'email': "awdada",
                'role': "awdawd",
            },
            'status': "failed",
        }

        return jsonify(result_dict)