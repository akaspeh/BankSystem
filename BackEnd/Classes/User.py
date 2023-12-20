from flask import jsonify, request, make_response, abort
from BackEnd.utils import UserSignInInfo
import psycopg2
import logging

class User:
    def __init__(self, dbsystem):
        self.__isAdmin = False
        self.__dbsystem = dbsystem
    def login(self):
        data = request.get_json()

        if self.__dbsystem.redis_get_element(data['email']) == 'false':
            result_dict = {
                 'userDto': {'id': '', 'userName': '', 'email': '', 'role': ''},
                'status': 'failed'}
            return jsonify(result_dict)
        else:
            temporary = self.__dbsystem.redis_get_element(data['email'])
            if  temporary.decode() == data['password']:
                with self.__dbsystem.postgres.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                    try:
                        cursor.execute(f"SELECT * FROM USERS WHERE email = '{data['email']}'")

                        variable = cursor.fetchall()
                        result_dict = {
                            'userDto': {'id': variable[0]['id'], 'userName': variable[0]['name'],
                                        'email': variable[0]['email'], 'role': variable[0]['role']},
                            'status': 'succeed'}
                        return jsonify(result_dict)
                    except Exception as e:
                        logging.error(e)
            else:
                result_dict = {
                    'userDto': {'id': '', 'userName': '', 'email': '', 'role': ''},
                    'status': 'wrong password'}
                return jsonify(result_dict)
    def sign_in(self):
        data = request.get_json()

        if self.__dbsystem.redis_get_element(data['email']) == 'false':
            self.__dbsystem.redis.redis_client.set(name=data['email'], value=data['password'])

            with self.__dbsystem.postgres.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                try:
                    cursor.execute(f"INSERT INTO USERS(name, email, phone, address, role) "
                                   f"VALUES('{data['firstName'] + ' ' + data['lastName']}', '{data['email']}',"
                                   f"'{data['phone']}', '{data['address']}', 'client') ")

                    cursor.execute(f"SELECT * FROM USERS WHERE email = '{data['email']}'")

                    variable = cursor.fetchall()

                    self.__dbsystem.audit_insert_info(user_name=variable[0]['name'],user_id=variable[0]['id'], operation='Signed In')

                except Exception as e:
                    logging.error(e)
            return jsonify({'status': 'succeed'})
        else:
            return jsonify({'status': 'wrong email'})

    def getBalance(self,userId):
        with self.__dbsystem.postgres.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            try:
                cursor.execute(f"SELECT balance FROM USERS WHERE id = {userId}")

                # Получение результатов
                balance = cursor.fetchall()
                # Формирование объектов LoanDto из результатов

                # Создание объекта LoanListDto
                result_dict = {
                    'userId': userId,
                    'balance': balance[0][0]
                }
                return jsonify(result_dict)

            except Exception as e:
                logging.error(e)
                items = []










