import requests
import json
from datetime import datetime

payload={}
headers = {'Content-type': 'application/json'}

r = requests.delete('http://localhost:8000/api/hhha/users/',data=json.dumps(payload),headers=headers)
print(r.content)

datetime.now().strftime()

r = requests.get('http://localhost:8000/api/hhha/users/',headers=headers)
print(r.content)