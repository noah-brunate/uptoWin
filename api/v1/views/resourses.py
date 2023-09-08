#!/usr/bin/python3

import models
from api.v1.views import my_views
from flask import jsonify


@my_views.route('/resourse_list', methods=['GET'], strict_slashes=False)
def resList():
    """returns a list of all the available resourses"""
    res_list = []
    for v in models.storage.all('Resourses').values():
        res_list.append(v.to_dict())
    return jsonify(res_list)
