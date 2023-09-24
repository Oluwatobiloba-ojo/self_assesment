import unittest

from chapter_three.Clock import Clock


class MyTestCase(unittest.TestCase):
    def test_something(self):
        myClock = Clock(12, 30, 25)
        myClock.set_minute(10)
        self.assertEqual(10, myClock.get_minute())
        myClock.set_hour(12)
        self.assertEqual(12, myClock.get_hour())
        myClock.set_second(30)
        self.assertEqual(30, myClock.get_second())

    def test_that_hour_second_minute_can_not_pass_24_60_60(self):
        myClock = Clock(12, 29, 30)
        self.assertEqual(12, myClock.get_hour())
        self.assertEqual(29, myClock.get_second())
        self.assertEqual(30, myClock.get_minute())
        myClock.set_hour(35)
        self.assertEqual(12, myClock.get_hour())
        myClock.set_second(65)
        self.assertEquals(29, myClock.get_second())
        myClock.set_minute(60)
        self.assertEqual(30, myClock.get_minute())

    def test_that_clock_will_display_in_hh_mm_so_display(self):
        myClock = Clock(12, 29, 30)
        self.assertLogs("12:30:29", myClock.display())

