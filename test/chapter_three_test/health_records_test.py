import unittest

from chapter_three.health_records import HealthRecords


class MyTestCase(unittest.TestCase):
    def test_something(self):
        my_health = HealthRecords("Ope", "Ogungbemi", 2000, 6, 31, 34, 300, "Male")
        my_health.set_first_name("Delighted")
        self.assertEqual("Delighted", my_health.get_first_name())
        my_health.set_last_name("Adewuyi")
        self.assertEqual("Adewuyi", my_health.get_last_name())
        my_health.set_year_of_birth(2000)
        self.assertEqual(2000, my_health.get_year_birth())
        my_health.set_month_of_birth(4)
        self.assertEqual(4, my_health.get_month_birth())
        my_health.set_day_of_birth(24)
        self.assertEqual(24, my_health.get_day_of_birth())
        my_health.set_height(24)
        self.assertEqual(24, my_health.get_height())
        my_health.set_weight(250)
        self.assertEqual(250, my_health.get_weight())
        my_health.set_gender("Female")
        self.assertEqual("Female", my_health.get_gender())

    def test_that_health_records_can_calculate_age(self):
        my_health = HealthRecords("Ope", "Ogungbemi", 2000, 6, 31, 34, 300, "Male")
        age = my_health.calculate_age()
        self.assertEqual(23, age)

    def test_that_health_records_can_calculate_maximum_heart_rate(self):
        my_health = HealthRecords("Ope", "Ogungbemi", 2000, 6, 31, 34, 300, "Male")
        maximum = my_health.maximum_heart_rate()
        self.assertEqual(197, maximum)

    def test_that_health_records_can_calculate_body_mass_index(self):
        my_health = HealthRecords("Ope", "Ogungbemi", 2000, 6, 31, 34, 300, "Male")
        my_health.set_weight(200)
        self.assertEqual(200, my_health.get_weight())
        my_health.set_height(24)
        self.assertEqual(24, my_health.get_height())
        result = my_health.calculate_body_mass_index()
        self.assertEqual("244.10", result)

    def test_that_health_records_can_calculate_target_heart_rate(self):
        my_health = HealthRecords("Ope", "Ogungbemi", 2000, 6, 31, 34, 300, "Male")
        range = my_health.calculate_target_heart_rate(50, 70)
        self.assertEqual("98.50 - 137.90", range)
