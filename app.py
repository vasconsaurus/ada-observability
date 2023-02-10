from flask import Flask, render_Template
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)


@app.route('/renda-fixa')
def renda_fixa():
    return render_template('lista.hmtl', title='Renda Fixa')
