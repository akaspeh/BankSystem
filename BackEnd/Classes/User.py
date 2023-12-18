from flask import jsonify, request, make_response, abort
from BackEnd.utils import UserSignInInfo

class User:
    def __init__(self, dbsystem):
        self.__isAdmin = False
        self.__dbsystem = dbsystem
    def login(self):
        data = request.get_json()
        # user = UserSignInInfo(email=data['email'], password=data['password'])

        # if self.__dbsystem.redis_get_element(user.email) == 'false':
        #     result_dict = {
        #         'userDto': {'id': '', 'userName': '', 'email': '', 'role': ''},
        #         'status': 'failed'}
        #     return jsonify(result_dict)
        # else:
        #     if self.__dbsystem.redis_get_element(
        #             user.email) is user.password:  # дописати після реляційки цей іф(потрібно просто дістати поля)...
        #         return
        #     else:
        result_dict = {
            'userDto': {'id': '', 'userName': '', 'email': '', 'role': ''},
            'status': 'wrong password'}
        return jsonify(result_dict)
    def sign_in(self):
        data = request.get_json()
        user = UserSignInInfo(email=data['email'], password=data['password'], name=data['name']
                              , phone=data['phone'], address=data['address'])

        if self.__dbsystem.redis_get_element(user.email) == 'false':
            self.__dbsystem.redis.set(key=user.email,
                                    value=user.password)  # після цього додати додавання в реляційку екземпляра

            return jsonify({'status': 'succeed'})
        else:
            return jsonify({'status': 'wrong email'})







