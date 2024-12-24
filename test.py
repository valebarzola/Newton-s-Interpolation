import unittest
from funciones import diferencias_dividas,polinomio

class TestDiferenciasDivididas(unittest.TestCase):
    def test_diferenciasDivididas_withEmptyLists(self):
        self.assertEqual(diferencias_dividas([], []), [])

unittest.main()