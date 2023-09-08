#/!/usr/bin/python3
"""my server"""

from flask import Flask
from flask import render_template, url_for
from object import data


app = Flask(__name__)


#@app.before_request
#def execute():
#    data()

@app.route('/uptoWin', strict_slashes=False)
def uptoWin():
    return render_template("index.html")

@app.route('/uptoWin/home', strict_slashes=False)
def re_Home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
