from flask import Flask, escape, request
from guia_do_mochileiro_api.guia_do_mochileiro import obter_citacao_aleatoria

app = Flask(__name__)

@app.route('/guia/quote')
def comissao():
    return obter_citacao_aleatoria()
