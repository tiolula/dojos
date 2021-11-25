from unittest import TestCase

from guia_do_mochileiro_api.guia_do_mochileiro import obter_citacao_aleatoria


class TestCitacaoAletoria(TestCase):
    def test_citacao_aleatoria_retorna_nao_entre_em_panico(self):
        
        citacao_esperada = 'NÃO ENTRE EM PÂNICO!'
        citacao_obtida = obter_citacao_aleatoria()

        self.assertEqual(citacao_esperada, citacao_obtida)
