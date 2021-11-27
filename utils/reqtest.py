import requests
import json
import random
from datetime import datetime


def post_user_add(uid, tg_uid, username):
    payload={'uid': uid, 'tg_uid': tg_uid, 'username': username}
    headers = {'Content-type': 'application/json'}
    r = requests.post('https://geohack-ecovector.herokuapp.com/api/token/users/', data=json.dumps(payload), headers=headers)
    print(r.content)
    #r = requests.get('https://geohack-ecovector.herokuapp.com/api/token/users/', headers=headers)
    #print(r.content)


def get_user_add():
    headers = {'Content-type': 'application/json'}

    r = requests.get('https://geohack-ecovector.herokuapp.com/api/token/users/', headers=headers)
    print(r.content)
    return r.content
