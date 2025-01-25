import unittest
from robo import *

class TesteInformacoes(unittest.TestCase):

    def setUp(self):
        self.robo = iniciar()

    def testar_localizacao(self):
        mensagens = ["Onde fica o HEMOBA?", "Qual o endereço do HEMOBA?", "Qual a localização do HEMOBA?", "Onde fica?", "Qual o endereço?", "Qual a localização?"]

        for mensagem in mensagens:
            print(f"testando a mensagem: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "O o HEMOBA de Vitória da Conquista se localiza no endereço: Av. Crescencio Silveira - Hospital São Vicente - Bairro São Vicente", 
                resposta.text
            )

    def testar_horario_funcionamento(self):
        mensagens = ["Qual o horário de funcionamento?", "Que horas abre?", "Que horas fecha?", "Está aberto agora?", "Ainda está aberto?", "Que horas começa a funcionar?"]

        for mensagem in mensagens:
            print(f"testando a mensagem: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Horário de funcionamento: Domingo: Fechado | Segunda a Sexta: 07:00 - 13:00 | Sábado: 24h de funcionamento", 
                resposta.text
            )

    def testar_requisitos_doacao(self):
        mensagens = ["Quem pode doar sangue?", "Eu posso doar?", "Como saber se posso doar sangue?", "Qual critério para poder doar?", "Posso doar sangue?"]

        for mensagem in mensagens:
            print(f"testando a mensagem: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "No link a seguir você consegue encontrar todos os critérios para doação de sangue: https://www.gov.br/saude/pt-br/composicao/saes/sangue", 
                resposta.text
            )

    def testar_resultado_exame(self):
        mensagens = ["Onde consigo ver o resultado do meu exame?", "Onde encontro o resultado?", "Onde consigo o resultado", "Como vejo o resultado?", "Onde pego o resultado?"]

        for mensagem in mensagens:
            print(f"testando a mensagem: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Infelizmente hoje você só consegue obter o resultado dos exames realizados presencialmente na sede do Hemoba em Vitória da Conquista", 
                resposta.text
            )

    def testar_documentos_doacao(self):
        mensagens = ["O que preciso levar no dia da doação?", "O que preciso para poder doar?", "Quais documentos são necessários?", "Qual documento preciso levar no dia da doação?", "Quais os documentos exigidos?"]

        for mensagem in mensagens:
            print(f"testando a mensagem: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Para doar sangue, é necessário levar um documento oficial de identidade com foto, como a carteira de identidade, carteira de trabalho, carteira de motorista ou passaporte.", 
                resposta.text
            )

if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteInformacoes))

    executor = unittest.TextTestRunner()
    executor.run(testes)