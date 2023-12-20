from BackEnd.Classes.User import *
from BackEnd.Classes.Admin import *
import psycopg2
import psycopg2.extras
import logging
from datetime import date
from datetime import datetime
from flask_cors import CORS

class BANK:
    def __init__(self, dbsystem):
        self.user = User(dbsystem)
        self.admin = Admin(dbsystem)
        self.dbsystem = dbsystem
    def createTransaction(self):
        data = request.get_json()
        with self.dbsystem.postgres.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            try:
                today = date.today().strftime("%Y-%m-%d")
                cursor.execute(f"UPDATE USERS SET balance = balance - {data['amount']} WHERE id = {data['userIdSender']} ")
                cursor.execute(f"UPDATE USERS SET balance = balance + {data['amount']} WHERE id = {data['userIdReceiver']} ")
                cursor.execute(f"INSERT INTO TRANSACTIONS (data, amount, description, user_id_sender, user_id_reciver)"
                f"VALUES ('{today}', {data['amount']}, '{data['description']}', {data['userIdSender']}, {data['userIdReceiver']})")
                response = make_response('', 204)
                return response
            except Exception as e:
                logging.error(e)
                abort(403)

    def createLoan(self):
        data = request.get_json()
        print(data)
        with self.dbsystem.postgres.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            try:
                cursor.execute(f"INSERT INTO LOANS (amount, date_open, date_close, interest_rate, user_id)"
                f"VALUES ({data['amount']}, '{date.today()}', '{datetime.strptime(data['closingDate'], '%d-%m-%Y')}',"
                               f"{data['interestRate']}, {data['userId']})")
                cursor.execute(f"UPDATE USERS SET balance = balance+{data['amount']} WHERE id = {data['userId']}")
                response = make_response('', 201)
                return response

            except Exception as e:
                logging.error(e)
                abort(403)

