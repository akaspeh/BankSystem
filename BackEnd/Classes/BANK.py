from BackEnd.Classes.User import *
from BackEnd.Classes.Admin import *
import psycopg2
import psycopg2.extras
import logging
from datetime import date


class BANK:
    def __init__(self, dbsystem):
        self.user = User(dbsystem)
        self.admin = Admin(dbsystem)
        self.dbsystem = dbsystem
    def transaction(self): #ТУТ ПЖ СДЕЛАЙ ЮНИТ ТЕСТ ДОЛБАЕБ
        data = request.get_json()
        with self.dbsystem.postgres.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            try:
                cursor.execute(f"UPDATE CARDS SET balance = balance - {data['amount']} WHERE card = {data['cardholder']} ")
                cursor.execute(f"UPDATE CARDS SET balance = balance + {data['amount']} WHERE card = {data['cardreciver']} ")
                cursor.execute(f"INSERT INTO TRANSACTIONS (data, amount, description, user_id_sender, user_id_reciver)"
                f"VALUES ({date.today()}, {data['amount']}, {data['description']}, {data['cardholder']}, {data['cardreciver']})")
                response = make_response('', 204)
                return response
            except Exception as e:
                abort(403)
                logging.error(e)
    # def transactionUserToUser(self):
    #
    # def withdraw(self,card):
    #
    # def topUp(self,card):
    #
    def createLoan(self):
        data = request.get_json()
        with self.dbsystem.postgres.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            try:
                cursor.execute(f"INSERT INTO LOANS (amount,data,interest_rate,user_id)"
                f"VALUES ({data['amount']},{data['data']},{data['interest_rate']},{data['user_id']})")
                response = make_response('', 201)
                return response
            except Exception as e:
                logging.error(e)
                abort(403)

