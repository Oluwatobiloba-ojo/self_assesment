import unittest

from chapter_three.Account import Accounts


class MyTestCase(unittest.TestCase):

    def test_check_balance(self):
        my_account = Accounts()
        self.assertEqual(0, my_account.get_balance())

    def test_that_we_can_deposit(self):
        account = Accounts()
        account.deposit(5000)
        result = 5000
        expected = account.get_balance()
        self.assertEqual(result, expected)

    def test_that_account_can_not_deposit_negative_amount(self):
        account = Accounts()
        account.deposit(1000)
        result = account.get_balance()
        self.assertEqual(1000, result)
        account.deposit(-4000)
        balance = account.get_balance()
        self.assertEqual(1000, balance)

    def test_that_account_can_be_able_to_withdraw_amount(self):
        my_account = Accounts()
        my_account.deposit(5000)
        self.assertEqual(5000, my_account.get_balance())
        my_account.withdraw(2000)
        self.assertEqual(3000, my_account.get_balance())

    def test_that_amount_greater_than_balance_can_not_be_withdraw(self):
        my_account = Accounts()
        my_account.deposit(2000)
        self.assertEqual(2000, my_account.get_balance())
        my_account.withdraw(5000)
        self.assertEqual(2000, my_account.get_balance())

    def test_that_amount_less_that_zero_can_not_be_withdrawal(self):
        my_account = Accounts()
        my_account.deposit(5000)
        self.assertEqual(5000, my_account.get_balance())
        my_account.withdraw(-3000)
        self.assertEqual(5000, my_account.get_balance())

    def test_that_account_can_transfer_from_one_account(self):
        my_account = Accounts()
        delight_account = Accounts()
        my_account.deposit(4000)
        self.assertEqual(4000, my_account.get_balance())
        delight_account.deposit(100)
        self.assertEqual(100, delight_account.get_balance())
        my_account._transfer_to(delight_account, 4000)
        self.assertEqual(0, my_account.get_balance())
        self.assertEqual(4100, delight_account.get_balance())

    def test_that_account_can_transfer_amount_greater_that_balance(self):
        my_account = Accounts()
        tobi_account = Accounts()
        my_account.deposit(5000)
        self.assertEqual(5000, my_account.get_balance())
        tobi_account.deposit(2000)
        self.assertEqual(2000, tobi_account.get_balance())
        tobi_account._transfer_to(my_account, 3000)
        self.assertEqual(5000, my_account.get_balance())
        self.assertEqual(2000, tobi_account.get_balance())

    def test_that_amount_less_than_zero_can_not_be_transfer(self):
        my_account = Accounts()
        tobi_account = Accounts()
        tobi_account.deposit(2000)
        self.assertEqual(2000, tobi_account.get_balance())
        my_account.deposit(1000)
        self.assertEqual(1000, my_account.get_balance())
        tobi_account._transfer_to(my_account, -3000)
        self.assertEqual(2000, tobi_account.get_balance())
        self.assertEqual(1000, my_account.get_balance())
