from django.test import TestCase

from app.calc import subtract
from app.calc import add


class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test that values are added together"""
        self.assertEqual(add(3, 8), 11)
    
    def test_subtract_numbers(self):
        """Test the a number is ssubtracted from another"""
        self.assertEqual(subtract(6, 11), 5)

