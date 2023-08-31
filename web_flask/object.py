#!/usr/bin/python3

import requests
import models
from models.running import Running
from models.upcoming import Upcoming


url = "https://kontests.net/api/v1/all"

response = requests.get(url)
objs = response.json()
for obj in objs:
    if obj['status'] == 'CODING':
        val = Running(obj)
    elif obj['status'] == 'BEFORE':
        val = Upcoming(obj)
    storage.new(val)
    storage.save()
