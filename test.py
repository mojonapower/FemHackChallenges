import unittest
from src.modules import calc
import math


class TestCalc(unittest.TestCase):
    #Testeo conversión de unidades de medida y calculos matematicos
    def test_kmH_to_MS(self):
        result = calc.kmH_to_MS(1)
        self.assertEqual(result, 0.277778)
    
    def test_Km_to_M(self):
        result = calc.Km_to_M(1)
        self.assertEqual(result, 1000)
    
    def test_rad_to_grados(self):
        result = calc.rad_to_grados(math.pi)
        self.assertEqual(result,180)

    def test_grados_to_rad(self):
        result = calc.grados_to_rad(180)
        self.assertEqual(round(result, 2),3.14)

    def test_velocidadY(self):
        result = calc.velocidadY(15,53)
        self.assertEqual(round(result, 2),11.98)
        
    def test_velocidadX(self):
        result = calc.velocidadX(15,53)
        self.assertEqual(round(result, 2),9.03)

    def test_hmax(self):
        result = calc.hmax(11.98,9.8)
        self.assertEqual(round(result, 2),7.32)
    
    def test_tiempoLanzamiento(self):
        result = calc.tiempoLanzamiento(11.98,9.8)
        self.assertEqual(round(result, 2),1.22)
    
    def test_xmax(self):
        result = calc.xmax(9.03,1.22)
        self.assertEqual(round(result, 2),22.03)#

class TestDraw(unittest.TestCase):
    pass
