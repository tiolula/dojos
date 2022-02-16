from unittest import TestCase
import cachipum.juego as juego

class TesteDeCachipum(TestCase):

    def teste_suma_2_y_3_retornando_5(self):
        valor_a = 2
        valor_b = 3
        resultado_esperado = 5

        resultado_calculado = juego.suma(valor_a, valor_b)

        self.assertEqual(resultado_calculado, resultado_esperado)