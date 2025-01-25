from robo import *
from flask import Flask

VERSAO = "1.0"

robo = iniciar()
servico_robo = Flask(__name__)

@servico_robo.route("/versao")
def get_versao():
    return VERSAO

@servico_robo.route("/resposta/<mensagem>")
def get_resposta(mensagem):
    resposta = robo.get_response(mensagem.lower())

    return resposta.text

if __name__ == "__main__":
    servico_robo.run(host="0.0.0.0", port=5000)