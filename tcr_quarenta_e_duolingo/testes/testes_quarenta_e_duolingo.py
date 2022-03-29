from unittest import TestCase
import negocio.quarenta_e_duolingo as negocio

class TesteTraducao(TestCase):

    def teste_palavra_inserida_eh_a_palavra_certa(self):
        palavra_apresentada = "quarenta e dois"
        palavra_inserida = "forty two"
        resposta_certa = "forty two"

        resultado = negocio.verificarPTBR(palavra_inserida, resposta_certa)

        self.assertTrue(resultado)

    def teste_palavra_inserida_nao_eh_a_palavra_certa(self):
        palavra_apresentada = "quarenta e dois"
        palavra_inserida = "fort two"
        resposta_certa = "forty two"

        resultado = negocio.verificarPTBR(palavra_inserida, resposta_certa)

        self.assertFalse(resultado)