from chatterbot import ChatBot
import time

CONFIANCA_MINIMA = 0.7

def configurar():
    time.clock = time.time

    robo = ChatBot("Robô de Atendimento do HEMOBA", read_only = True, logic_adapters = [{"import_path": "chatterbot.logic.BestMatch"}])

    return True, robo

def executar(robo):
    while True:
        mensagem = input("digite alguma coisa...\n")
        resposta = robo.get_response(mensagem.lower())
        if resposta.confidence >= CONFIANCA_MINIMA:
            print(f"HEMOBA >> {resposta.text} [confiança={resposta.confidence}]")
        else:
            print(f"Infelizmente, eu ainda não sei te ajudar com essa pergunta [confiança={resposta.confidence}, resposta={resposta.text}]")
            print("Pergunte outra coisa")

if __name__ == "__main__": 
    configurado, robo = configurar()

    if configurado:
        executar(robo)