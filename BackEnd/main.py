
from DBSystem.DBsystem import *
from flask_cors import CORS
from flask import Flask, jsonify, request
from Classes.BANK import BANK

class Application:
    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app, supports_credentials=True, methods=['GET', 'POST', 'PUT', 'DELETE'])
        self.app.config['CORS_HEADERS'] = 'Content-Type'
        self.dbsystem = DBsystem()
        self.BANK = BANK(self.dbsystem)
        self.setup_routes()
    def setup_routes(self):
        self.app.route('/api/reg/create-account', methods=['POST'])(self.BANK.user.sign_in)
        self.app.route('/api/auth/login', methods=['POST'])(self.BANK.user.login)
        self.app.route('/api/client/transaction/all/<int:userId>', methods=['GET'])(self.BANK.admin.findAllTransactions)
        self.app.route('/api/client/loan/all/<int:userId>', methods=['GET'])(self.BANK.admin.findAllLoan)
        self.app.route('/api/client/transaction/create', methods=['POST'])(self.BANK.createTransaction)
        self.app.route('/api/client/loan/create', methods=['POST'])(self.BANK.createLoan)
        self.app.route('/api/client/find/<string:search>', methods=['GET'])(self.BANK.admin.clientSearch) #GET, а не POST

    def run(self):
        self.dbsystem.create_tables()
        self.app.run(debug=True)


if __name__ == '__main__':
    Aplication = Application()
    Aplication.run()


