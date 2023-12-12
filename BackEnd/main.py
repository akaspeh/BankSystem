
from DBSystem.DBsystem import *
from flask_cors import CORS
from flask import jsonify, request, Flask
class Application:
    def __init__(self):
        self.dbsystem = DBsystem()
        self.app = Flask(__name__)
        CORS(self.app, supports_credentials=True, methods=['GET', 'POST', 'PUT', 'DELETE'])
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/api/auth/login', methods=['POST'])(self.get_user)

    def get_user(self):
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

    def run(self):
        self.dbsystem.create_tables()
        self.app.run(debug=True)


if __name__ == '__main__':
    Aplication = Application()
    Aplication.run()


