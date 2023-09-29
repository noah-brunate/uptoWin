#/!/usr/bin/python3
"""my server"""

from flask import Flask
from flask import render_template, url_for
from object import data
import models


app = Flask(__name__)

num1 = models.storage.count('Upcoming')
num2 = models.storage.count('Running')

#@app.before_request
#def execute():
#    data()

@app.route('/uptoWin', strict_slashes=False)
def uptoWin():
    return render_template("index.html", run_count=num1, up_count=num2)

@app.route('/home', strict_slashes=False)
def home():
    return render_template("home.html", run_count=num1, up_count=num2)

@app.route('/upcoming', strict_slashes=False)
def upcoming():
    objs = models.storage.all('Upcoming').values()
    return render_template("upcoming.html", objs=objs, run_count=num2, up_count=num1)

@app.route('/running', strict_slashes=False)
def running():
    objs = models.storage.all('Running').values()
    return render_template("running.html", objs=objs, run_count=num2, up_count=num1)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
