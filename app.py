import http.client
import time
import random

from flask import Flask, render_template
import prometheus_client as prom
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

quantidade_usuarios_online = prom.Gauge(
    "quantidade_usuarios_online", "Números de usuários online no momento")


def simulacao_usuarios():
    time.sleep(random.randint(1, 10))
    quantidade_usuarios_online.set(random.randint(1, 100))


def erro_bad_request():
    if random.randint(0, 1) == 0:
        return http.client.BAD_REQUEST


@app.route("/renda-fixa")
def renda_fixa():
    simulacao_usuarios()
    erro_bad_request()
    return render_template("lista.html", title="Renda Fixa")


@app.route("/renda-variavel")
def renda_variavel():
    simulacao_usuarios()
    erro_bad_request()
    return render_template("lista.html", title="Renda Variável")


@app.route("/cripto")
def cripto():
    simulacao_usuarios()
    erro_bad_request()
    return render_template("lista.html", title="Cripto")


@app.route("/fii")
def fii():
    simulacao_usuarios()
    erro_bad_request()
    return render_template("lista.html", title="Fii")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5001")
