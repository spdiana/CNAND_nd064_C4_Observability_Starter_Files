from flask import Flask, render_template, request
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import generate_latest

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# static information as metric
metrics.info('app_info', 'FrontEnd Application info', version='1.0.3')

@app.route('/')
def homepage():
    return render_template("main.html")

@app.route('/error')
def error_page():
    return 'error', 500

@app.route('/metrics')
def metrics():
    return generate_latest()

if __name__ == "__main__":
    app.run()