import unittest


class AppTesting(unittest.TestCase):
    def test_search(self):
        print('This is search test')

    def test_advanced_search(self):
        print("This is Advanced search test")

    def test_prepaid_recharge(self):
        print("This is prepaid recharge test")

    def test_postpaid_recharge(self):
        print("This is post paid recharge test")


if __name__ == "__main__":
    unittest.main()
