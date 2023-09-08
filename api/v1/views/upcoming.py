#!/usr/bin/python3

import models
from flask import jsonify
from api.v1.views import my_views


@my_views.route('/upcoming_list', methods=['GET'], strict_slashes=False)
def upList():
    """returns a list of the Upcoming instances"""
    up_list = []
    for v in models.storage.all('Upcoming').values():
        up_list.append(v.to_dict())
    return jsonify(up_list)

@my_views.route('/upcoming_count', methods=['GET'], strict_slashes=False)
def upCount():
    """returns the count for Upcoming instances"""
    num = models.storage.count('Upcoming')
    obj = {'count': num}
    return jsonify(obj)

