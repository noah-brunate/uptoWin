#!/usr/bin/python3

import models
from flask import jsonify
from api.v1.views import my_views


@my_views.route('/running_list', methods=['GET'], strict_slashes=False)
def runList():
    """returns a list of the running instances"""
    run_list = []
    for v in models.storage.all('Running').values():
        run_list.append(v.to_dict())
    return jsonify(run_list)

@my_views.route('/running_count', methods=['GET'], strict_slashes=False)
def runCount():
    """returns the count for running instances"""
    num = models.storage.count('Running')
    obj = {'count': num}
    return jsonify(obj)
