import requests
import json
import random
import time
from datetime import datetime
import pandas as pd

headers = {'Accept': 'application/json',
           'Content-Type': 'application/json', }
params = (('options', 'keyValues'),)

d = '2019-06-1 18:47:05'
d = pd.to_datetime(d)
d = datetime.timestamp(d)
date = "2019-11-"
time = " 18:47:05"
temp = [18, 19, 20, 21, 22, 23, 24, 25, 26]
fan = [1, 2, 3, 4, 5]
swing = ['OFF', 'ON']
ranum = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ['Manas Kabre', 'Shashank G', 'Tanvi K', 'Harshita Edwankar',
         'Raju Rastogi', 'Farhan Akhtar', 'Hritik Roshan', 'George Mathew', 'Joseph Jacob']
Ac_id = ['urn:ngsi-ld:ACFinalp:1/attrs','urn:ngsi-ld:ACFinalp:2/attrs','urn:ngsi-ld:ACFinalp:3/attrs']
id_var = 1
hour = list(range(1, 24))
mini = list(range(1, 60))
sec = list(range(1, 60))
time = " "
for i in range(1, 31):
    date = "2019-11-"
    date += str(i)
    for j in range(10):
        name = "AC_ChangeMaker_"
        name += str(id_var)
        id_var += 1
        time = " " + str(random.choice(hour)) + ":" + \
            str(random.choice(mini)) + ":" + str(random.choice(sec))
        date += time
        d = pd.to_datetime(date)
        d = datetime.timestamp(d)
        print(d)
        data = {}
        if(random.choice(ranum) == 0):
            # data = {'id': name, 'type': 'AC_Change', 'address': {'streetAddress': 'check',
            #                                                 'postOfficeBoxNumber': '18', 'addressLocality': 'Antwerpen', 'addressCountry': 'op'},
            #         'testtime': d,
            #         'AC_Id': 1,
            #         'temp': 0,
            #         'fan': 0,
            #         'swing': swing[0],
            #         'name': random.choice(names)
            #         }
            data = {
                "testtime": {
                    "value": d,
                    "type": "Number"
                },
                "temp": {
                    "value": 0,
                    "type": "Number"
                },
                "fan": {
                    "value": 0,
                    "type": "Number"
                }, "swing": {
                    "value": swing[0],
                    "type": "Text"
                },
                "name": {
                    "value": random.choice(names),
                    "type": "Text"
                }
            }
        else:
            # data = {'id': name, 'type': 'AC_Change', 'address': {'streetAddress': 'check',
            #                                                 'postOfficeBoxNumber': '18', 'addressLocality': 'Antwerpen', 'addressCountry': 'op'},
            #         'testtime': d,
            #         'AC_Id': 1,
            #         'temp': random.choice(temp),
            #         'fan': random.choice(fan),
            #         'swing': random.choice(swing),
            #         'name': random.choice(names)
            #         }
            data = {
                "testtime": {
                    "value": d,
                    "type": "Number"
                },
                "temp": {
                    "value": random.choice(temp),
                    "type": "Number"
                },
                "fan": {
                    "value": random.choice(fan),
                    "type": "Number"
                }, "swing": {
                    "value": random.choice(swing),
                    "type": "Text"
                },
                "name": {
                    "value": random.choice(names),
                    "type": "Text"
                }
            }
        url = 'http://0.0.0.0:1026/v2/entities/' + random.choice(Ac_id)
        response = requests.patch(
            url, headers=headers, data=json.dumps(data))
        print(response)
