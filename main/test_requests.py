import requests
import json
from datetime import datetime
import unittest

headers = {'Content-type': 'application/json'}

class TestUsersGetRequests(unittest.TestCase):
   
    def test_get(self):
        r = requests.get('http://localhost:8000/api/hhha/users/',headers=headers)
        self.assertTrue(r.ok)
        
    def test_get_exact_good(self):
        r = requests.get('http://localhost:8000/api/hhha/users/1',headers=headers)
        self.assertTrue(r.ok)

    def test_get_exact_bad(self):
        r = requests.get('http://localhost:8000/api/hhha/users/0',headers=headers)
        self.assertEqual(r.status_code, 404)

class TestUsersPostRequests(unittest.TestCase):

    def test_post(self):
        payload = {
            'id':'1000',
            'tg_uid': 'test_tg_uid',
            'vk_uid': 'test_vk_uid',
            'email': 'test_email',
            'username': 'test_username',
            'password': 'test_password',
            'phone': '89851267355'
        }
        #payload={'tg_uid': tg_uid, 'username': username, 'pref_channel': 'tg', "is_staff": False}
        r = requests.post('http://localhost:8000/api/hhha/users/', data=json.dumps(payload), headers=headers)
        print(r.content)
        self.assertEqual(r.status_code, 201)

    def test_bad(self):
        payload = {}
        r = requests.post('http://localhost:8000/api/hhha/users/', data=json.dumps(payload), headers=headers)
        self.assertEqual(r.status_code, 400)

    def test_not_importent(self):
        payload = {
            'tg_uid': 'test_tg_uid',
            'vk_uid': 'test_vk_uid',
            'email': 'test_email',
            'username': 'test_username',
            'password': 'test_password',
        }
        r = requests.post('http://localhost:8000/api/hhha/users/', data=json.dumps(payload), headers=headers)
        self.assertEqual(r.status_code, 400)

class TestUsersDeleteRequests(unittest.TestCase):
    
    def test_delete(self):
        payload = {
            'id': '1000',
        }
        r = requests.delete('http://localhost:8000/api/hhha/users/', data=json.dumps(payload), headers=headers)
        self.assertEqual(r.status_code, 200)

    def test_wrong(self):
        payload = {
            'id': 'bad_test_uid',
        }
        r = requests.delete('http://localhost:8000/api/hhha/users/', data=json.dumps(payload), headers=headers)
        self.assertEqual(r.status_code, 404)            

    def test_bad(self):
        payload = {}
        r = requests.delete('http://localhost:8000/api/hhha/users/', data=json.dumps(payload), headers=headers)
        self.assertEqual(r.status_code, 400)              


if __name__ == '__main__':
    unittest.main()