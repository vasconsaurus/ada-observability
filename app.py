from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)


@app.route("/renda-fixa")
@metrics.counter("efetivacao_renda_variavel",
                 "Número de papéis de renda fixa efetivados",
                 label={"tipo": "ACOES"})
def renda_fixa():
    return render_template("lista.html", title="Renda Fixa")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5001")
