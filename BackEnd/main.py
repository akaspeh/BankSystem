
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

    def redis_get_element(self, key):
        value = self.dbsystem.redis.get(key)

        if value is None:
            return 'false'
        else:
            return value

    def login(self):
        data = request.get_json()
        user = UserSignInInfo(email=data['email'], password=data['password'])

        if self.redis_get_element(user.email) == 'false':
            result_dict = {
                'userDto': {'id': '', 'userName': '', 'email': '', 'role': ''},
                'status': 'failed'}
            return jsonify(result_dict)
        else:
            if self.redis_get_element(user.email) is user.password:  # дописати після реляційки цей іф(потрібно просто дістати поля)...
                return;
            else:
                result_dict = {
                    'userDto': {'id': '', 'userName': '', 'email': '', 'role': ''},
                    'status': 'wrong password'}
                return jsonify(result_dict)

    def sign_in(self):
        data = request.get_json()
        user = UserSignInInfo(email=data['email'], password=data['password'], first_name=data['firstName'],
                              last_name=data['lastName'], phone=data['phone'], address=data['address'])

        if self.redis_get_element(user.email) == 'false':
            self.dbsystem.redis.set(key=user.email, value=user.password)  # після цього додати додавання в реляційку екземпляра

            return jsonify({'status': 'succeed'})
        else:
            return jsonify({'status': 'wrong email'})


class UserSignInInfo:

    def __init__(self, email, password, first_name, last_name, phone, address):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.address = address


if __name__ == '__main__':
    Aplication = Application()
    Aplication.run()


