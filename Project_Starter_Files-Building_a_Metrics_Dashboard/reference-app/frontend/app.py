import time
import random

from flask import Flask, render_template, request
# from prometheus_flask_exporter import PrometheusMetrics
from prometheus_flask_exporter.multiprocess import GunicornInternalPrometheusMetrics

app = Flask(__name__)
# metrics = PrometheusMetrics(app)
metrics = GunicornInternalPrometheusMetrics.for_app_factory()
metrics.init_app(app)

# static information as metric
metrics.info('app_info', 'FrontEnd Application info', version='1.0.3')

endpoints = ('endpoint_a', 'endpoint_b', 'endpoint_c', 'endpoint_d', 'not_found', 'error')


@app.route('/')
def homepage():
    return render_template("main.html")


@app.route('/not_found')
def not_f():
    time.sleep(random.random() * 0.15)
    return 'error', 404


@app.route('/error')
def oops():
    time.sleep(random.random() * 0.13)
    return 'error', 500


if __name__ == "__main__":
    app.run(debug=False, port=5001)
