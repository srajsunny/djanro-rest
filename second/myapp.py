import requests
import json
print("app h")
URL= "http://127.0.0.1:8000/stu/"
data= {'name':'sunny','roll':4, 'city': 'Patna'}
json_data=json.dumps(data)
r=requests.post(url=URL, data=json_data)
data=r.json()
print("yoyo")
print(data)


