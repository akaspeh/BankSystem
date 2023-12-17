from BackEnd.Classes.User import *
import psycopg2
import psycopg2.extras
import logging
from datetime import date
class BANK:
    def __init__(self, dbsystem):
        self.user = User(dbsystem)
        self.dbsystem = dbsystem
    def transactionToUser(self): #ТУТ ПЖ СДЕЛАЙ ЮНИТ ТЕСТ
        data = request.get_json()
        original_balance = self.get_balance(data['cardholder'])

        with self.dbsystem.postgres.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            try:
                cursor.execute(f"UPDATE CARDS SET balance = balance - {data['amount']} WHERE card = {data['cardholder']} ")
                cursor.execute(f"UPDATE CARDS SET balance = balance + {data['amount']} WHERE card = {data['cardreciver']} ")
                cursor.execute(f"INSERT INTO TRANSACTIONS (data, amount, description, user_id_sender, user_id_reciver)"
                               f"VALUES ('{date.today()}', {data['amount']}, '{data['description']}', {data['cardholder']}, {data['cardreciver']})")

                current_balance = self.get_balance(data['cardholder'])
                if current_balance != original_balance - data['amount']:
                    return jsonify({'error': 'Incorrect balance after transaction'}), 404
                else:
                    return jsonify({'message': 'Transaction successful'}), 202

            except Exception as e:
                logging.error(e)

    def get_balance(self, card_number):
        with self.dbsystem.postgres.conn.cursor() as cursor:
            cursor.execute(f"SELECT balance FROM CARDS WHERE card = {card_number}")
            result = cursor.fetchone()
            return result[0] if result else None

    # def transactionUserToUser(self):
    #
    # def withdraw(self,card):
    #
    # def topUp(self,card):
    #
    # def createLoan(self,userid):

