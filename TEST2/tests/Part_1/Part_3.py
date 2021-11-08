import unittest
from src import Part_1


class Tea_Inheritance(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.test_tea = Part_1.Tea('Green Tea')

    def test_name(self):
        self.assertEqual(self.test_tea.name, 'Green Tea')

    def test_price(self):
        self.assertEqual(self.test_tea.price, 30)

    def test_size(self):
        self.assertEqual(self.test_tea.size, 10)

    def test_warmness(self):
        self.assertEqual(self.test_tea.warmness, 0.5)

    def test_sweetness(self):
        self.assertEqual(self.test_tea.sweetness, 0.5)

    def __is_valid_identifier(self):
        identifier = self.test_tea.identifier
        if identifier >= 1000000 and identifier <= 9999999:
            return True
        else:
            return False

    def test_identifier(self):
        is_valid = self.__is_valid_identifier()
        self.assertTrue(is_valid)

    def test_drink(self):
        to_match = "Oh, it's warm!"
        self.assertEqual(self.test_tea.drink(), to_match)

    def test_calory(self):
        to_match = "...it's a tea. Only a few calories"
        self.assertEqual(self.test_tea.calory(), to_match)
