
from DBSystem.DBsystem import *
from flask_cors import CORS
from flask import Flask
from Classes.BANK import BANK

class Application:
    def __init__(self):
        self.dbsystem = DBsystem()
        self.BANK = BANK(self.dbsystem)
        self.app = Flask(__name__)
        CORS(self.app, supports_credentials=True, methods=['GET', 'POST', 'PUT', 'DELETE'])
        self.setup_routes()
    def setup_routes(self):
        self.app.route('/api/reg/create-account', methods=['POST'])(self.BANK.user.login)
        self.app.route('/api/auth/login', methods=['POST'])(self.BANK.user.login)
        self.app.route('/api/client/transaction/all/${userId}', methods=['GET'])(self.BANK.admin.findAllTransactions)
        self.app.route('/api/client/loan/all/${userId}', methods=['GET'])(self.BANK.admin.findAllLoan)
        self.app.route('/api/client/transaction/create', methods=['POST'])(self.BANK.transaction)
        self.app.route('/api/client/loan/create', methods=['POST'])(self.BANK.createLoan)
        self.app.route('/api/client/find/${search}', methods=['POST'])(self.BANK.admin.clientSearch)

    def run(self):
        self.dbsystem.create_tables()
        self.app.run(debug=True)


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


