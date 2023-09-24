import unittest

from chapter_three.heart_rate import HeartRate


class MyTestCase(unittest.TestCase):
    def test_something(self):
        my_heart = HeartRate("Opeoluwa", "Ogunbeni", 2000, 4, 25)
        my_heart.set_first_name("Delighted")
        self.assertEqual("Delighted", my_heart.get_first_name())
        my_heart.set_last_name("Adesuyi")
        self.assertEqual("Adesuyi", my_heart.get_last_name())
        my_heart.set_year_of_birth(2001)
        self.assertEqual(2001, my_heart.get_year_birth())
        my_heart.set_month_of_birth(7)
        self.assertEqual(7, my_heart.get_month_birth())
        my_heart.set_day_of_birth(25)
        self.assertEqual(25, my_heart.get_day_of_birth())

    def test_that_target_heart_rate_can_calculate_age(self):
        my_heart = HeartRate("Opeoluwa", "Ogunbeni", 2000, 4, 25)
        age = my_heart.calculate_age()
        self.assertEqual(23, age)

    def test_that_target_heart_rate_can_calculate_maximum_heart_rate(self):
        my_heart = HeartRate("Opeoluwa", "Ogunbeni", 2000, 4, 25)
        maximum_heart_rate = my_heart.maximum_heart_rate()
        self.assertEqual(197, maximum_heart_rate)

    def test_that_target_heart_rate_calculate_target_heart_rate_at_different_range(self):
        my_heart = HeartRate("Opeoluwa", "Ogunbeni", 2000, 4, 25)
        first_range = my_heart.calculate_target_heart_rate(55, 70)
        self.assertEqual("108.35 - 137.90", first_range)

    def test_something2(self):
        my_heart = HeartRate("Opeoluwa", "Ogunbeni", 2000, 4, 25)
        range = my_heart.calculate_target_heart_rate(50, 70)
        self.assertEqual("98.50 - 137.90", range)