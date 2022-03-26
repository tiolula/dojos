from unittest import TestCase
import cachipum.juego as juego

class TesteDeCachipum(TestCase):

    def teste_jugador_y_pelota_gana_jugador(self):
        valor_a = "jugador"
        valor_b = "pelota"
        resultado_esperado = "jugador"

        resultado_calculado = juego.jugar(valor_a, valor_b)

        self.assertEqual(resultado_calculado, resultado_esperado)