#!/usr/bin/python3

from object import data
import os
import json
import models
from models.resourses import Resourses
from models.running import Running
from models.upcoming import Upcoming

if os.path.exists("file.json"):
    with open('file.json', 'r') as file:
        new = json.load(file)

    objs = [v for v in new.values()]
#obj1 = Resourses()
    dict1 = {"name":"TProjectEuler+","url":"https://hackerrank.com/contests/projecteuler","start_time":"2014-07-07T15:38:00.000Z","end_time":"2024-07-30T18:30:00.000Z","duration":"317616720.0","site":"HackerRank","in_24_hours":"No","status":"CODING"}
    dict2 = {"name":"1v1 Games by CodeChef","url":"https://www.codechef.com/GAMES","start_time":"2022-10-10 06:30:00 UTC","end_time":"2032-10-10 06:30:00 UTC","duration":"315619200.0","site":"CodeChef","in_24_hours":"No","status":"CODING"}

    dicts = data()
    for v in dicts:
       num = 0
       for k in objs:
           if k['name'] == v['name']:
               num = 1
       if num == 0:
           obj2 = Upcoming(**v)

#obj3 = Upcoming(**dict2)

models.storage.save()


print(models.storage.count())


print("---test1---")
#print(obj2)
print(models.storage.count("Upcoming"))

print("---test2---")
#for v in models.storage.all().values():
#   print(v.to_dict())
#print(obj3)
print("---test3---")

#print(models.storage.all("Upcoming"))
