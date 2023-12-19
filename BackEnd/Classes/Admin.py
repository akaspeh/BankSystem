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
                cursor.execute(f"SELECT * FROM TRANSACTIONS "
                               f"WHERE user_id_sender = {userId} "
                               f"OR user_id_reciver = {userId}")

                # Получение результатов
                transactions_data = cursor.fetchall()

                # Формирование объектов TransactionDto из результатов
                items = [TransactionDto(transaction['id'], transaction['data'].strftime("%d-%m-%Y"), transaction['amount'],
                                        transaction['description'], transaction['user_id_sender'],
                                        transaction['user_id_reciver']).to_dict() for transaction in transactions_data]

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

    def findAllLoan(self, userId):
        with self.__dbsystem.postgres.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            try:
                cursor.execute(f"SELECT * FROM LOANS WHERE user_id = {userId}")

                # Получение результатов
                loans_data = cursor.fetchall()

                # Формирование объектов LoanDto из результатов

                items = [
                    LoanDto(id = loan['user_id'], amount=loan['amount'], interestRate=loan['interest_rate'], openingDate=loan['date_open'].strftime("%d-%m-%Y"),
                            closingDate=loan['date_close'].strftime("%d-%m-%Y")).to_dict() for loan in loans_data]

                # Создание объекта LoanListDto
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
                    WHERE name LIKE %s
                    """

                cursor.execute(query, ('%' + search + '%',))

                # Получение результатов
                user_data = cursor.fetchall()

                # Формирование объектов ClientListDto из результатов
                items = [UserDto(user['id'], user['name'], user['email'], user['role']).to_dict() for user in user_data]

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