from BackEnd.utils.TransactionDto import *
import psycopg2
import psycopg2.extras
import logging
from flask import jsonify, request
class Admin:
    def __init__(self, dbsystem):
        self.__isAdmin = False
        self.__dbsystem = dbsystem

    def findAllTransactions(self, user_id):
        with self.__dbsystem.postgres.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            try:
                cursor.execute(f"SELECT * FROM TRANSACTIONS WHERE user_id_sender = {user_id} OR user_id_reciver = {user_id}")

                # Получение результатов
                rows = cursor.fetchall()
                transactions_data = cursor.fetchall()

                # Формирование объектов TransactionDto из результатов
                items = [TransactionDto(*transaction) for transaction in transactions_data]

                # Создание объекта TransactionListDto
                result_dict = {
                    'items': items,
                    'totalCount': len(items)
                }

                return jsonify(result_dict)

            except Exception as e:
                logging.error(e)
