from flask import Flask
import DBSystem.DBsystem

DBSystem = DBSystem()
app = Flask(__name__)


if __name__ == '__main__':

    app.rum(debug=True)

