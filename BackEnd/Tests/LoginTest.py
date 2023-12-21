import unittest
from BackEnd.DBSystem.DBsystem import *
from flask_cors import CORS
from flask import Flask, jsonify, request
from BackEnd.Classes.User import *
import requests
import json
class LoginTest(unittest.TestCase):

    def setUp(self):
        self.user_data = User
        self.__dbsystem = DBsystem()

    def test_failed_login(self):
        fake_json_data = {'email': 'record@gmail.com', 'password' : '12345678'}

        url = 'http://localhost:5000/api/auth/login'
        response = requests.post(url, data=json.dumps(fake_json_data), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.json()['status'],'failed')

    def test_sign_in(self):
        fake_json_data = {'email': 'test@test.com', 'password': 'test1pas', 'address': '', 'firstName':'tester',
                          'lastName':'','phone':'00000000'}
        url = 'http://localhost:5000/api/reg/create-account'
        response = requests.post(url, data=json.dumps(fake_json_data), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.json()['status'], 'succeed')

    def test_sign_in_failed(self):
        fake_json_data = {'email': 'test@test.com', 'password': 'test1pas', 'address': '', 'firstName':'tester',
                          'lastName':'','phone':'00000000'}
        url = 'http://localhost:5000/api/reg/create-account'
        response = requests.post(url, data=json.dumps(fake_json_data), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.json()['status'], 'wrong email')


if __name__ == '__main__':
    unittest.main()