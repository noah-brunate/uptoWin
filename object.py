#!/usr/bin/python3

import os
import json
import requests
import models
from models.running import Running
from models.upcoming import Upcoming

def data():
    url = "https://kontests.net/api/v1/all"

    response = requests.get(url)
    objs = response.json()
    print(len(objs))

    if os.path.exists("file.json"):
        with open('file.json', 'r') as file:
            avail_objs = json.load(file)
        for obj in objs:
            num = 0
            if avail_objs == []:
                for v in avail_objs.values():
                    if v['name'] == obj['name']:
                        num = 1
            if num == 0:
                if obj['status'] == 'CODING':
                    val1 = Running(**obj)
                elif obj['status'] == 'BEFORE':
                    val2 = Upcoming(**obj)

    else:
        for obj in objs:
            if obj['status'] == 'CODING':
                val1 = Running(**obj)
            elif obj['status'] == 'BEFORE':
                val2 = Upcoming(**obj)

    models.storage.save()
    print(models.storage.count())

data()
