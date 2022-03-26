from unittest import TestCase
import cachipum.juego as juego

class TesteDeCachipum(TestCase):

    def teste_jugador_y_pelota_gana_jugador(self):
        opcion_a = "jugador"
        opcion_b = "pelota"
        ganador_esperado = "jugador"

        ganador = juego.jugar(opcion_a, opcion_b)

        self.assertEqual(ganador, ganador_esperado)