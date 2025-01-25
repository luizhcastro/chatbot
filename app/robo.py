from chatterbot import ChatBot
from difflib import SequenceMatcher

CONFIANCA_MINIMA = 0.50

def comparar_mensagens(mensagem_digitada, mensagem_candidata):
    confianca = 0.0
    digitada = mensagem_digitada.text
    candidata = mensagem_candidata.text
    if digitada and candidata:
        confianca = SequenceMatcher(None, digitada, candidata)
        confianca = round(confianca.ratio(), 2)
    return confianca

def iniciar():
    robo = ChatBot("Robô de Atendimento do Hemoba",
                   storage_adapter="chatterbot.storage.SQLStorageAdapter",
                   database_uri="sqlite:///data/chatbot.db",
                   read_only=True,
                   statement_comparison_function=comparar_mensagens,
                   logic_adapters=[{
                       "import_path": "chatterbot.logic.BestMatch"
                   }])
    return robo

if __name__ == "__main__":
    robo = iniciar()