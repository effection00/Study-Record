import unittest
from src import Part_1


class Product_Fields(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.test_bean = Part_1.Product('A Cold Drink')

    def test_name(self):
        self.assertEqual(self.test_bean.name, 'A Cold Drink')

    def test_price(self):
        self.assertEqual(self.test_bean.price, 30)

    def test_size(self):
        self.assertEqual(self.test_bean.size, 20)

    def test_warmness(self):
        self.assertEqual(self.test_bean.warmness, 0.5)

    def test_sweetness(self):
        self.assertEqual(self.test_bean.sweetness, 0.5)

    def __is_valid_identifier(self):
        identifier = self.test_bean.identifier
        if identifier >= 1000000 and identifier <= 9999999:
            return True
        else:
            return False

    def test_identifier(self):
        is_valid = self.__is_valid_identifier()
        self.assertTrue(is_valid)
