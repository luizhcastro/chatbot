from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json

CONVERSAS = [
    "./conversas/saudacoes.json",
    "./conversas/informacoes.json",
]

def iniciar():
    robo = ChatBot("Robô de Atendimento do Hemoba")
    treinador = ListTrainer(robo)

    return treinador

def carregar_conversas():
    conversas = []
    for arquivo_conversas in CONVERSAS:
        try:
            with open(arquivo_conversas, "r") as arquivo:
                conversas_para_treinamento = json.load(arquivo)
                conversas.append(conversas_para_treinamento["conversas"])
        except FileNotFoundError:
            print(f"Arquivo {arquivo_conversas} não encontrado.")
            continue
        except json.JSONDecodeError:
            print(f"Erro ao decodificar o arquivo {arquivo_conversas}.")
            continue
    return conversas


def treinar(treinador, conversas):
    for conversa in conversas:
        for mensagens_resposta in conversa:
            mensagens = mensagens_resposta["mensagens"]
            resposta = mensagens_resposta["resposta"]

            print(f"treinando o robô. Mensagens: {mensagens}. Resposta: {resposta}")
            for mensagem in mensagens:
                treinador.train([mensagem, resposta])


if __name__ == "__main__":
    treinador = iniciar()

    conversas = carregar_conversas()
    if conversas:
        treinar(treinador, conversas)
