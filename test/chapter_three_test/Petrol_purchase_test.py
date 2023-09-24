import unittest

from chapter_three.petrol_purchase import Petrol


class MyTestCase(unittest.TestCase):
    def test_something(self):
        my_petrol = Petrol("Webui", "Coal", 50, 120, 5)
        my_location = "Canada"
        my_petrol.set_location(my_location)
        location = my_petrol.get_location()
        self.assertEqual(my_location, location)
        types = "Coal Oil"
        my_petrol.set_types(types)
        petrol_t = my_petrol.get_types()
        self.assertEqual(types, petrol_t)
        quantity = 20
        my_petrol.calculate_quantity(quantity)
        self.assertEqual(quantity, my_petrol.get_quantity())
        price = 120
        my_petrol.set_price_per_litre(price)
        self.assertEqual(price, my_petrol.get_price())
        discount = 9
        my_petrol.percentage_discount(discount)
        self.assertEqual(discount, my_petrol.get_discount())

    def test_net_purchase_amount(self):
        my_petrol = Petrol("Webui", "Coal", 50, 120, 5)
        my_petrol.calculate_quantity(50)
        self.assertEqual(50, my_petrol.get_quantity())
        my_petrol.set_price_per_litre(500)
        self.assertEqual(500, my_petrol.get_price())
        my_petrol.percentage_discount(10)
        self.assertEqual(10, my_petrol.get_discount())

        net_purchase = my_petrol.get_purchase_amount()
        self.assertEqual(net_purchase, 24999.9)

