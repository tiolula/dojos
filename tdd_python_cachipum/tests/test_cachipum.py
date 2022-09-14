from unittest import TestCase
import src.juego as juego

class TestDeCachipum(TestCase):

    def test_ejemplo(self):
        a = 1
        b = 2
        esperado = 3

        resultado = juego.sumar(a, b)

        self.assertEqual(esperado, resultado)
