import unittest
from robo import *

class TesteInformacoes(unittest.TestCase):

    def setUp(self):
        self.robo = iniciar()

    def testar_localizacao(self):
        informacoes = ["Onde fica o HEMOBA?", "Qual o endereco do HEMOBA?", "Qual a localizacao do HEMOBA?", "Onde fica?", "Qual o endereco?", "Qual a localizacao?" ]

        for informacoes in informacoes:
            print(f"testando informações {informacoes}")

            resposta = self.robo.get_response(informacoes)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "O HEMOBA de Vitoria da Conquista se localiza no endereco: Av. Crescencio Silveira - Hospital Sao Vicente - Bairro Sao Vicente", 
                resposta.text
            )

    def testar_horario_de_atendimento(self):
        informacoes = ["Qual o horario de funcionamento?", "Que horas abre?", "Que horas fecha?", "Esta aberto agora?", "Ainda esta aberto?", "Que horas comeca a funcionar?"]

        for informacoes in informacoes:
            print(f"testando informações {informacoes}")

            resposta = self.robo.get_response(informacoes.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Horario de funcionamento: Domingo: Fechado | Segunda a Sexta: 07:00 - 13:00 | Sabado: 24h de funcionamento",
                resposta.text
            )
            
    def testar_quem_pode_doar(self):
        informacoes = ["Quem pode doar sangue?", "Eu posso doar?", "Como saber se posso doar sangue?", "Qual criterio para poder doar?", "Posso doar sangue?"]

        for informacoes in informacoes:
            print(f"testando informações {informacoes}")

            resposta = self.robo.get_response(informacoes.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "No link a seguir voce consegue encontrar todos os criterios para doacao de sangue: https://www.gov.br/saude/pt-br/composicao/saes/sangue",
                resposta.text
            )

    def testar_resultado_exame(self):
        informacoes = ["Onde consigo ver o resultado do meu exame?", "Onde encontro o resultado?", "Onde consigo o resultado","Como vejo o resultado?", "Onde pego o resultado?"]

        for informacoes in informacoes:
            print(f"testando informações {informacoes}")

            resposta = self.robo.get_response(informacoes.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Infelizmente hoje voce so consegue obter o resultado dos exames realizados presencialmente na sede do Hemoba em Vitoria da Conquista",
                resposta.text
            )             

    def testar_documentos_necessarios(self):
        informacoes = ["Quais documentos sao necessarios?", "Qual documento preciso levar no dia da doacao?", "Quais os documentos exigidos?"]

        for informacoes in informacoes:
            print(f"testando informações {informacoes}")

            resposta = self.robo.get_response(informacoes.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Para doar sangue, e necessario levar um documento oficial de identidade com foto, como a carteira de identidade, carteira de trabalho, carteira de motorista ou passaporte",
                resposta.text
            ) 

if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteInformacoes))

    executor = unittest.TextTestRunner()
    executor.run(testes)