#!/usr/bin/python3
"""Module for the BaseModel class"""

import uuid
import models


class BaseModel:
    """The parent class of other classes"""

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        if kwargs is not None and kwargs != {}:
            for k, v in kwargs.items():
               if k == '__class__' or k == 'duration' or k == 'site':
                   continue
               else:
                   setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.name = args[0]
        models.storage.new(self)

    def __str__(self):
        """returns the string representation of an object"""
        return f"[{self.__class__.__name__}] ({self.id}) ({self.__dict__})"

    def to_dict(self):
        """returns the dictionary representation of an object"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict
