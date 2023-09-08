#!/usr//bin/python3

from flask import Blueprint


my_views = Blueprint('my_views', __name__, url_prefix='/api/v1')


from api.v1.views.index import *
from api.v1.views.running import *
from api.v1.views.upcoming import *
from api.v1.views.resourses import *
