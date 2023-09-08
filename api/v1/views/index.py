#!/usr/bin/python3

from api.v1.views import my_views
from flask import Flask, jsonify


@my_views.route('/', strict_slashes=False)
def hi():
    return 'Everytging is workig Fine'

@my_views.route('/status', strict_slashes=False)
def myStatus():
    return jsonify({'Dude': 'Everytging is workig Fine'})
