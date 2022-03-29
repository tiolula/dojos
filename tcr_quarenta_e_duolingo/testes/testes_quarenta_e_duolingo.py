from unittest import TestCase
import negocio.quarenta_e_duolingo as negocio

class TesteDeExemplo(TestCase):

    def teste_de_exemplo(self):
        palavra_apresentada = "quarenta e dois"
        palavra_inserida = "forty two"
        resposta_certa = "forty two"

        resultado = negocio.verificarPTBR(palavra_inserida, resposta_certa)

        self.assertTrue(resultado)