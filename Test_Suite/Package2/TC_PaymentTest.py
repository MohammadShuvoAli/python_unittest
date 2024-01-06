import unittest


class PaymentTest(unittest.TestCase):
    def test_payment_in_dollar(self):
        print("This is payment in dollar test")
        self.assertTrue(True)

    def test_payment_in_taka(self):
        print("This is payment in taka test")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()

