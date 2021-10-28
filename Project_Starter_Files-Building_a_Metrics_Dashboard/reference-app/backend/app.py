import time
import random
import pymongo
import os

from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo
# from prometheus_flask_exporter import PrometheusMetrics
from prometheus_flask_exporter.multiprocess import GunicornInternalPrometheusMetrics

app = Flask(__name__)
# metrics = PrometheusMetrics(app)
metrics = GunicornInternalPrometheusMetrics.for_app_factory()
metrics.init_app(app)

app.config['MONGO_DBNAME'] = 'example-mongodb'
app.config['MONGO_URI'] = 'mongodb://example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb'

mongo = PyMongo(app)

# static information as metric
metrics.info('app_info', 'Backend Application info', version='1.0.3')

endpoints = ('ep_one', 'ep_two', 'ep_three', 'ep_four', 'not_found', 'error')


@app.route('/')
def homepage():
    return "Hello World"


@app.route('/api')
def my_api():
    answer = "something"
    return jsonify(response=answer)


@app.route('/star', methods=['POST'])
def add_star():
    star = mongo.db.stars
    name = request.json['name']
    distance = request.json['distance']
    star_id = star.insert({'name': name, 'distance': distance})
    new_star = star.find_one({'_id': star_id})
    output = {'name': new_star['name'], 'distance': new_star['distance']}
    return jsonify({'result': output})


@app.route('/ep_one')
def first_route():
    time.sleep(random.random() * 0.2)
    return '1'


@app.route('/ep_two')
def the_second():
    time.sleep(random.random() * 0.4)
    return '2'


@app.route('/ep_three')
def test_3rd():
    time.sleep(random.random() * 0.6)
    return '3'


@app.route('/ep_four')
def fourth_one():
    time.sleep(random.random() * 0.8)
    return '4'


@app.route('/not_found')
def not_f():
    time.sleep(random.random() * 0.9)
    return 'error', 404


@app.route('/error')
def oops():
    return 'error', 500


# @app.route('/metrics')
# def metrics():
#     return generate_latest()



if __name__ == "__main__":
    app.run(debug=False, port=5000)
