import requests
import json
import random
from datetime import datetime


def post_user_add(tg_uid, username):
    payload={'tg_uid': tg_uid, 'username': username, 'pref_channel': 'tg'}
    headers = {'Content-type': 'application/json'}
    r = requests.post('https://geohack-ecovector.herokuapp.com/api/token/users/', data=json.dumps(payload), headers=headers)
    print(r.content)
    #r = requests.get('https://geohack-ecovector.herokuapp.com/api/token/users/', headers=headers)
    #print(r.content)


def get_user_add(val):
    headers = {'Content-type': 'application/json'}

    r = requests.get('https://geohack-ecovector.herokuapp.com/api/token/users/', headers=headers)
    parsed_string = json.loads(r.content)
    users_len = len(parsed_string['users'])
    val_list = []
    for i in range(users_len):
        if parsed_string['users'][i][f'{val}']:
            val_list.append(parsed_string['users'][i][f'{val}'])
        else: val_list.append(0)
    print(len(parsed_string['users']))
    return val_list


def post_event_add(name, description, date, place):
    payload={'name': name, 'description': description, 'date': date, 'place': place} #'verified': False
    headers = {'Content-type': 'application/json'}
    r = requests.post('https://geohack-ecovector.herokuapp.com/api/token/events/', data=json.dumps(payload), headers=headers)
    print(r.content)


def get_event_add(val):
    headers = {'Content-type': 'application/json'}

    r = requests.get('https://geohack-ecovector.herokuapp.com/api/token/events/', headers=headers)
    parsed_string = json.loads(r.content)
    users_len = len(parsed_string['events'])
    val_list = []
    for i in range(users_len):
        val_list.append(parsed_string['events'][i][f'{val}'])
    return val_list


def get_user_on_event_add(user_id, event_id):
    headers = {'Content-type': 'application/json'}
    r = requests.get(f'https://geohack-ecovector.herokuapp.com/api/token/users/{user_id}/subscribe/{event_id}', headers=headers)
    if r.status_code == 200:
        print('Add')
    print(r.content)
