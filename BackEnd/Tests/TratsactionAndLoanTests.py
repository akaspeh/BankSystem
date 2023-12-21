import unittest
from BackEnd.DBSystem.DBsystem import *
from flask_cors import CORS
from flask import Flask, jsonify, request
from BackEnd.Classes.BANK import *
import requests
import json
class LoginTest(unittest.TestCase):

    def setUp(self):
        self.__dbsystem = DBsystem()
        self.BANK = BANK(self.__dbsystem)

    def test_getBalance(self):
        with self.__dbsystem.postgres.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            try:
                cursor.execute(f"SELECT id FROM USERS WHERE email = 'test@test.com'")

                user_id = cursor.fetchall()

                url = f'http://localhost:5000/api/client/balance/{user_id[0][0]}'
                response = requests.get(url, headers={'Content-Type': 'application/json'})
                self.assertEqual(response.json()['balance'], 0)
            except Exception as e:
                logging.error(e)

    def test_create_loan(self):
        with self.__dbsystem.postgres.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            try:

                cursor.execute(f"SELECT id FROM USERS WHERE email = 'test@test.com'")

                user_id = cursor.fetchall()

                fake_json_data = {'amount': 500, 'closingDate': '22-12-2025', 'interestRate': 0.5,
                                  'userId': user_id[0][0]}
                url = 'http://localhost:5000/api/client/loan/create'
                response = requests.post(url, data=json.dumps(fake_json_data), headers={'Content-Type': 'application/json'})
                self.assertEqual(response.status_code, 201)
            except Exception as e:
                logging.error(e)
    def test_getBalance_afterLoan(self):
        with self.__dbsystem.postgres.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            try:
                cursor.execute(f"SELECT id FROM USERS WHERE email = 'test@test.com'")

                user_id = cursor.fetchall()


                url = f'http://localhost:5000/api/client/balance/{user_id[0][0]}'
                response = requests.get(url, headers={'Content-Type': 'application/json'})
                self.assertEqual(response.json()['balance'],500)
            except Exception as e:
                logging.error(e)

    def test_create_transaction(self):
        with self.__dbsystem.postgres.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            try:

                cursor.execute(f"SELECT id FROM USERS WHERE email = 'test@test.com'")

                user_id = cursor.fetchall()
                cursor.execute(f"SELECT id FROM USERS WHERE email = 'admin@email'")

                admin_id = cursor.fetchall()
                fake_json_data = {'amount': 500, 'description': '', 'userIdSender': user_id[0][0],
                                  'userIdReceiver': admin_id[0][0]}

                url = 'http://localhost:5000/api/client/transaction/create'
                response = requests.post(url, data=json.dumps(fake_json_data), headers={'Content-Type': 'application/json'})
                self.assertEqual(response.status_code, 204)
            except Exception as e:
                logging.error(e)


    def test_getBalance_afterTransaction(self):
        with self.__dbsystem.postgres.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            try:
                cursor.execute(f"SELECT id FROM USERS WHERE email = 'test@test.com'")

                user_id = cursor.fetchall()

                url = f'http://localhost:5000/api/client/balance/{user_id[0][0]}'
                response = requests.get(url, headers={'Content-Type': 'application/json'})
                self.assertEqual(response.json()['balance'], 0)
            except Exception as e:
                logging.error(e)

if __name__ == '__main__':
    unittest.main()