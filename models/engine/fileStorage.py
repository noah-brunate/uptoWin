#!/usr/bin/python3
"""Module for the filestorage"""

import os
import json
from models.running import Running
from models.resourses import Resourses
from models.upcoming import Upcoming


class FileStorage:
    """The file storage class"""
    __filename = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns a dictionary of objects"""
        new_dict = {}
        for k, v in self.__objects.items():
            if cls:
                name = k.split('.')[0]
                if name == cls:
                    new_dict[k] = v
            else:
                new_dict[k] = v
        return new_dict

    def new(self, obj):
        """Methods adds an object to the __objects"""
        k = obj.__class__.__name__ + '.' + obj.id
        self.__objects[k] = obj

    def save(self):
        """Method serialises __objects to json file"""
        file_path = self.__filename
        dict_obj = {k : v.to_dict() for k, v in self.__objects.items()}
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(dict_obj, file)

    def classes(self):
        """Method returns a dictionary of classes"""
        class_dict = {"Running" : Running, "Upcoming" : Upcoming, "Resourses" : Resourses}
        return class_dict

    def reload(self):
        """Method deserialises the json file to __object"""
        file_path = self.__filename
        new_dict = {}
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                obj_dict = json.load(file)
            for k, dictionary in obj_dict.items():
                class_name = dictionary['__class__']
                new_dict[k] = self.classes()[class_name](**dictionary)
        self.__objects = new_dict

    def count(self, cls=None):
        """Method returns the number of objects of the given cls"""
        num = 0
        if cls:
            obj_dict = self.all(cls)
            for k in obj_dict.keys():
                num += 1
        else:
            num = len(self.all())
        return num
