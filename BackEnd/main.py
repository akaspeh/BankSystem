from flask import Flask
from flask_cors import CORS

from DBSystem.DBsystem import *





class Application:
    def __init__(self):
        self.dbsystem = DBsystem()
        self.flask = Flask(__name__)
        print("wdas")

    def run(self):
        self.dbsystem.create_tables()
        CORS(self.flask, supports_credentials=True, methods=['GET', 'POST', 'PUT', 'DELETE'])
        self.flask.run(debug=True)


if __name__ == '__main__':

    Aplication = Application()
    Aplication.run()

