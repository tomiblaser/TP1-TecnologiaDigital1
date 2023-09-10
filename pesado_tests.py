import unittest

from pesado import cant_ceros, cant_unos, mas_unos_que_ceros, prefijo, \
                    es_pesado, densidad


class TestNumerosPesados(unittest.TestCase):

    def test_cant_ceros(self):
        self.assertEqual(cant_ceros("10010"),3)
        self.assertEqual(cant_ceros("00aswed1279"),2)
        self.assertEqual(cant_ceros("11111"),0)
        self.assertEqual(cant_ceros(""),0)

    def test_cant_unos(self):
        self.assertEqual(cant_unos("10010"),2)
        self.assertEqual(cant_unos("11aswed79"),2)
        self.assertEqual(cant_unos("0000"),0)
        self.assertEqual(cant_unos(""),0)
        
    def test_mas_unos_que_ceros(self):
        self.assertEqual(mas_unos_que_ceros("10010"),False)
        self.assertEqual(mas_unos_que_ceros("10110"),True)
        self.assertEqual(mas_unos_que_ceros("asd1da101"),True)
        self.assertEqual(mas_unos_que_ceros(""),False)
        self.assertEqual(mas_unos_que_ceros("asdqwe"),False)
        
    def test_prefijo(self):
        self.assertEqual(prefijo("Ditella",4),"Dite")
        self.assertEqual(prefijo("Ditella",7),"Ditella")
        self.assertEqual(prefijo("Ditella",0),"")
        
    def test_es_pesado(self):
        self.assertEqual(es_pesado(57),True)
        self.assertEqual(es_pesado(13),True)
        self.assertEqual(es_pesado(40),False)
        self.assertEqual(es_pesado(15),True)
        self.assertEqual(es_pesado(51),False)
        self.assertEqual(es_pesado(23),False)
        self.assertEqual(es_pesado(0),False)
        
    def test_densidad(self):
        self.assertEqual(densidad(29,33),0.75)
        self.assertEqual(densidad(1,4),2/3)
        self.assertEqual(densidad(2,6),0.25)
        self.assertEqual(densidad(2,3),0.0)
        
unittest.main()
