#/!/usr/bin/python3
"""my server"""

form flask import Flask


app = Flask(__name__)


app.route('/', strict_slashes=False)
