
import unittest

from chapter_three.Car import Car


class MyTestCase(unittest.TestCase):
    def test_something(self):
        myCar = Car("Camry", "2021", 30000.00)
        myCar.set_model("Toyota")
        self.assertEqual("Toyota", myCar.get_model())
        myCar.set_year("2021")
        self.assertEqual('2021', myCar.get_year())
        myCar.set_price(10000)
        self.assertEqual(10000, myCar.get_price())

    def test_that_negative_price_can_not_be_in_the_value(self):
        myCar = Car("Camry", 2001, 1000.00)
        myCar.set_price(-3000)
        self.assertEqual(1000.00, myCar.get_price())

    def test_the_discount_of_two_car_object(self):
        myCar = Car("Camry", 2001, 1000.00)
        camry = Car("Camry", 2001, 1000.00)
        myCar.set_price(10000)
        self.assertEqual(10000, myCar.get_price())
        camry.set_price(20000)
        self.assertEqual(20000, camry.get_price())
        myCar.discount(5)
        self.assertEqual(9500, myCar.get_price())
        camry.discount(7)
        self.assertEqual(18600, camry.get_price())
