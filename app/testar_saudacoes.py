import unittest
from robo import *

class TesteSaudacoes(unittest.TestCase):

    def setUp(self):
        self.robo = iniciar()

    def testar_oi_ola(self):
        saudacoes = ["ola", "oi", "oi, tudo bem?", "tudo bem?", "oie"]

        for saudacao in saudacoes:
            print(f"testando saudação {saudacao}")

            resposta = self.robo.get_response(saudacao)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Ola, sou o robo de atendimento do HEMOBA. Como posso te ajudar?",
                resposta.text
            )


    def testar_bom_dia_boa_tarde_boa_noite(self):
        saudacoes = ["Bom dia", "Boa tarde", "Boa noite"]

        for saudacao in saudacoes:
            print(f"testando saudação {saudacao}")

            resposta = self.robo.get_response(saudacao)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Ola, sou o robo de atendimento do HEMOBA. Como posso te ajudar?",
                resposta.text
            )

if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteSaudacoes))

    executor = unittest.TextTestRunner()
    executor.run(testes)