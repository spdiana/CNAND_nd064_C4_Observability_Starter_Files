import time
import random
import pymongo
import os
import logging
import requests

from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo
# from prometheus_flask_exporter import PrometheusMetrics
from opentelemetry.exporter.jaeger import JaegerSpanExporter
from opentelemetry.sdk.resources import Resource
from prometheus_flask_exporter.multiprocess import GunicornInternalPrometheusMetrics

from jaeger_client import Config
from flask_opentracing import FlaskTracer
import opentracing

import opentelemetry.instrumentation.requests
from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    ConsoleSpanExporter,
    SimpleExportSpanProcessor,
)
# trace.set_tracer_provider(TracerProvider())
trace.set_tracer_provider(
    TracerProvider(resource=Resource.create({"service.name": "backend"}))
)

# # Configure the tracer to export traces to Jaeger
# jaeger_exporter = JaegerSpanExporter(
#     service_name='backend',
#     collector_host_name='localhost',
#     collector_port=14268,
#     # collector_endpoint='/api/traces?format=jaeger.thrift',
#     # opentelemetry-exporter-jaeger-thrift
# )

# jaeger_exporter = JaegerExporter(
#     service_name='backend',
#     agent_host_name="localhost",
#     agent_port=6831,
# )

trace.get_tracer_provider().add_span_processor(
    SimpleExportSpanProcessor(ConsoleSpanExporter())
)

# trace.get_tracer_provider().add_span_processor(
#     SimpleExportSpanProcessor(jaeger_exporter)
# )

tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("span_1"):
    with tracer.start_as_current_span("span_2"):
        with tracer.start_as_current_span("span_3"):
            print("Hello world from OpenTelemetry Python!")

app = Flask(__name__)
# metrics = PrometheusMetrics(app)
metrics = GunicornInternalPrometheusMetrics.for_app_factory()
metrics.init_app(app)

FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()

app.config['MONGO_DBNAME'] = 'example-mongodb'
app.config['MONGO_URI'] = 'mongodb://example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb'

mongo = PyMongo(app)

# static information as metric
metrics.info('app_info', 'Backend Application info', version='1.0.3')

endpoints = ('endpoint_a', 'endpoint_b', 'endpoint_c', 'endpoint_d', 'not_found', 'error')


@app.route("/")
def hello():
    with tracer.start_as_current_span("example-request"):
        requests.get("http://www.example.com")
    return "hello"


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


@app.route('/endpoint_a')
def first_route():
    time.sleep(random.random() * 1.2)
    return '1'


@app.route('/endpoint_b')
def the_second():
    time.sleep(random.random() * 0.4)
    return '2'


@app.route('/endpoint_c')
def test_3rd():
    time.sleep(random.random() * 0.6)
    return '3'


@app.route('/endpoint_d')
def fourth_one():
    time.sleep(random.random() * 0.8)
    return '4'


@app.route('/not_found')
def not_f():
    time.sleep(random.random() * 0.9)
    return 'error', 404


@app.route('/error')
def oops():
    time.sleep(random.random() * 0.7)
    return 'error', 500


# @app.route('/metrics')
# def metrics():
#     return generate_latest()


if __name__ == "__main__":
    app.run(debug=True, port=5000)
