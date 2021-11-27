import requests
import json
from datetime import datetime
import unittest

payload={}
headers = {'Content-type': 'application/json'}

class TestUsersRequests(unittest.TestCase):

    def test_get(self):
        r = requests.get('http://localhost:8000/api/hhha/users/',headers=headers)
        self.assertTrue(r.ok)
        
    def test_get_exact_good(self):
        r = requests.get('http://localhost:8000/api/hhha/users/1231',headers=headers)
        self.assertTrue(r.ok)

    def test_get_exact_bad(self):
        r = requests.get('http://localhost:8000/api/hhha/users/0',headers=headers)
        self.assertTrue(r.status_code, '404')

    datetime.now().strftime()

    r = requests.get('http://localhost:8000/api/hhha/users/',headers=headers)
    print(r.content)