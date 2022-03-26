from unittest import TestCase
import cachipum.juego as juego

class TesteDeCachipum(TestCase):

    def teste_jugador_y_pelota_gana_jugador(self):
        valor_a = 2
        valor_b = 3
        resultado_esperado = 5

        resultado_calculado = juego.jugar(valor_a, valor_b)

        self.assertEqual(resultado_calculado, resultado_esperado)