#!/usr/bin/python3
from models.upcoming import Upcoming

my_model = Upcoming()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_model_json = {"name":"ProjectEuler+","url":"https://hackerrank.com/contests/projecteuler","start_time":"2014-07-07T15:38:00.000Z","end_time":"2024-07-30T18:30:00.000Z","duration":"317616720.0","site":"HackerRank","in_24_hours":"No","status":"CODING"}
my_new_model = Upcoming(**my_model_json)
dict = my_new_model.to_dict()
print(my_new_model.id)
print(my_new_model)
print(dict)

print("--")
print(my_model is my_new_model)

