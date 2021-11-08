import unittest
from src import Part_1


class Product_Methods(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.test_bean = Part_1.Product('A Warm Water')

    def __get_sellability(self):
        sellability = self.test_bean.size / self.test_bean.price

        if sellability < 0.5:
            return "Not so sellable..."
        elif sellability < 1.0:
            return "Kinda sellable."
        else:
            return "Very sellable!"

    def test_sellability(self):
        sellability = self.__get_sellability()
        self.assertEqual(self.test_bean.sellability(), sellability)

    def __get_calory(self):
        calory = self.test_bean.size * self.test_bean.sweetness

        if calory < 10:
            return "...it's light"
        elif calory < 50:
            return "It's adequate."
        else:
            return "It's really heavy..!!"

    def test_calory(self):
        calory = self.__get_calory()
        self.assertEqual(self.test_bean.calory(), calory)
