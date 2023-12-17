from BackEnd.Classes.User import *
import psycopg2
import psycopg2.extras
import logging
from datetime import date
class BANK:
    def __init__(self, dbsystem):
        self.user = User(dbsystem)
        self.dbsystem = dbsystem
    def transactionToUser(self): #ТУТ ПЖ СДЕЛАЙ ЮНИТ ТЕСТ ДОЛБАЕБ
        data = request.get_json()
        with self.dbsystem.postgres.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            try:
                cursor.execute(f"UPDATE CARDS SET balance = balance - data['amount'] WHERE card = data['cardholder'] ")
                cursor.execute(f"UPDATE CARDS SET balance = balance + data['amount'] WHERE card = data['cardreciver'] ")
                cursor.execute(f"INSERT INTO TRANSACTIONS (data, amount, description, user_id_sender, user_id_reciver)"
                f"VALUES (data.today(), data['amount'], data['description'], data['cardholder'],data['cardreciver'])")
            except Exception as e:
                logging.error(e)
    # def transactionUserToUser(self):
    #
    # def withdraw(self,card):
    #
    # def topUp(self,card):
    #
    # def createLoan(self,userid):

