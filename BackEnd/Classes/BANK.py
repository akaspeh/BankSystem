from BackEnd.Classes.User import *
import psycopg2
import psycopg2.extras
import logging
class BANK:
    def __init__(self, dbsystem):
        self.user = User(dbsystem)
        self.dbsystem = dbsystem
    def transactionToUser(self, card): #ТУТ ПЖ СДЕЛАЙ ЮНИТ ТЕСТ ДОЛБАЕБ
        data = request.get_json()
        with self.dbsystem.postgres.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            try:
                cursor.execute(f"UPDATE CARDS SET balance = balance - data['amount'] WHERE card = card ")
            except Exception as e:
                logging.error(e)
    # def transactionUserToUser(self,card1,card2):
    #
    # def withdraw(self,card):
    #
    # def topUp(self,card):
    #
    # def createLoan(self,userid):

