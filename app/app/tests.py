"""sample tests"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):

    def test_add_number(self):
        res = calc.add(4,5)
        self.assertEqual(res, 9)

    def test_subtract_number(self):
        """Subtract numbers"""
        res = calc.subtract(10,5)
        self.assertEqual(res, 5)
        
        