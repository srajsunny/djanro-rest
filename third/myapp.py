import requests
import json

URL='http://127.0.0.1:8000/'

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
        print("hahahhahHSADDADAFDFADDAD",data)
    json_data=json.dumps(data)
    r=requests.get(url=URL, data=json_data)
    data=r.json()
    print(data)
#get_data()  

def create_data():
    data={'name':'aman', 'roll':4, 'city': 'Gorakhpur'}
    json_data=json.dumps(data)
    r=requests.post(url=URL, data=json_data)
    data=r.json()
    print(data)
#create_data

def update_data():
    data={'id':4,'name':'rahul brooo', 'city': 'Indiaa','roll': 11}
    json_data=json.dumps(data)
    r=requests.put(url=URL, data=json_data)
    data=r.json()
    print(data)

update_data()

