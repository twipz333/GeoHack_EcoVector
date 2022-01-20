# import requests
# import json
# import typing
# from typing import List
#
# api = 'https://geohack-ecovector.herokuapp.com/api/'
# header = {'Content-type': 'application/json'}
# token = 'token'
#
#
# class User():
#
#     def __init__(self, id, tg_uid=None, vk_uid=None, username=None, password=None) -> None:
#         self._id = id
#         self._tg_uid = tg_uid
#         self._vk_uid = vk_uid
#         self._username = username
#         self._password = password
#
#     def identify(self, id=None, tg_uid=None, vk_uid=None, username=None, password=None):
#         print(id)
#         if id:
#             return self._id == uid
#
#     def __str__(self) -> str:
#         return f'{self._uid}'
#
#
# def get_user_list() -> [User]:
#     response = requests.get(api + token + '/users/', headers=header)
#     users = [User]
#     for user in response.json()['users']:
#         users.append(User(**user))
#
#     return users
#
#
# def get_user_id(**kwargs):
#     users = get_user_list()
#     for user in users:
#         if user.identify(kwargs):
#             return user
#
#
# print(get_user_id(id='1'))
# print(get_user_list())

