#!/usr/bin/python3

from flask import Flask, jsonify, make_response
from api.v1.views import my_views


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(my_views)


@app.errorhandler(404)
def notFound(error):
    return make_response(jsonify({'error': 'Page not found'}), 404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, threaded=True)
