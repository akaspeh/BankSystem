from BackEnd.utils.TransactionDto import *
from BackEnd.utils.LoanDto import *
from BackEnd.utils.UserDto import *
import psycopg2
import psycopg2.extras
import logging
from flask import jsonify, request,make_response
class Admin:
    def __init__(self, dbsystem):
        self.__isAdmin = False
        self.__dbsystem = dbsystem

    def findAllTransactions(self, userId):
        with self.__dbsystem.postgres.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            try:
                cursor.execute(f"SELECT * FROM TRANSACTIONS WHERE user_id_sender = {userId} OR user_id_reciver = {userId}")

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
                items = []
                result_dict = {
                    'items': items,
                    'totalCount': len(items)
                }
                return jsonify(result_dict)

    def findAllLoan(self,userId):
        with self.__dbsystem.postgres.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            try:
                cursor.execute(
                    f"SELECT * FROM LOANS WHERE user_id = {userId}")

                # Получение результатов
                rows = cursor.fetchall()
                loans_data = cursor.fetchall()

                # Формирование объектов TransactionDto из результатов
                items = [LoanDto(*loan) for loan in loans_data]

                # Создание объекта TransactionListDto
                result_dict = {
                    'items': items,
                    'totalCount': len(items)
                }

                return jsonify(result_dict)

            except Exception as e:
                logging.error(e)
                items = []
                result_dict = {
                    'items': items,
                    'totalCount': len(items)
                }
                return jsonify(result_dict)

    def clientSearch(self, search):
        with self.__dbsystem.postgres.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            try:
                query = """
                    SELECT *
                    FROM USERS
                    WHERE name ILIKE %s
                    """

                cursor.execute(query, ('%' + search + '%',))

                # Получение результатов
                rows = cursor.fetchall()
                user_data = cursor.fetchall()

                # Формирование объектов TransactionDto из результатов
                items = [UserDto(*user) for user in user_data]

                # Создание объекта TransactionListDto
                result_dict = {
                    'items': items,
                    'totalCount': len(items)
                }

                return jsonify(result_dict)

            except Exception as e:
                logging.error(e)
                items = []
                result_dict = {
                    'items': items,
                    'totalCount': len(items)
                }
                return jsonify(result_dict)