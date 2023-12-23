from flask import jsonify, request, make_response, abort
import psycopg2
import logging
from BackEnd.utils.SecurityUtils import Security

class User:
    def __init__(self, dbsystem):
        self.__isAdmin = False
        self.__dbsystem = dbsystem
    def login(self):
        data = request.get_json()
        security = Security()

        security.hash.update(data['email'][0:5].encode('utf-8'))
        emailHashed = security.hash.hexdigest()



        if self.__dbsystem.redis_get_element(emailHashed) == 'false':
            result_dict = {
                 'userDto': {'id': '', 'userName': '', 'email': '', 'role': ''},
                'status': 'failed'}
            return jsonify(result_dict)
        else:
            security.hash.update(data['password'].encode('utf-8'))
            passwordHashed = security.hash.hexdigest()
            temporary = self.__dbsystem.redis_get_element(emailHashed)
            if  temporary.decode() == passwordHashed:
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
        security = Security()
        security.hash.update(data['email'][0:5].encode('utf-8'))
        emailHashed = security.hash.hexdigest()
        if self.__dbsystem.redis_get_element(emailHashed) == 'false':


            security.hash.update(data['password'].encode('utf-8'))
            passwordHashed = security.hash.hexdigest()

            self.__dbsystem.redis.redis_client.set(name=emailHashed, value= passwordHashed)

            with self.__dbsystem.postgres.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                try:
                    cursor.execute(f"INSERT INTO USERS(name, email, phone, address, role) "
                                   f"VALUES('{data['firstName'] + ' ' + data['lastName']}', '{data['email']}',"
                                   f"'{data['phone']}', '{data['address']}', 'client') ")

                    cursor.execute(f"SELECT * FROM USERS WHERE email = '{data['email']}'")

                    variable = cursor.fetchall()

                    self.__dbsystem.audit_insert_info(user_name=variable[0]['name'], user_id=variable[0]['id'], operation='Signed In')
                except Exception as e:
                    logging.error(e)
            return jsonify({'status': 'succeed'})
        else:
            return jsonify({'status': 'wrong email'})

    def getBalance(self,userId):
        with self.__dbsystem.postgres.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            try:
                cursor.execute(f"SELECT balance FROM USERS WHERE id = {userId}")

                balance = cursor.fetchall()

                result_dict = {
                    'userId': userId,
                    'balance': balance[0][0]
                }
                return jsonify(result_dict)

            except Exception as e:
                logging.error(e)










