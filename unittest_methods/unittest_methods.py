import unittest


def setUpModule():  # will be executed before executing any class or any method present in the test class
    print("setUpModule")


def tearDownModule():  # will be executed after completing everything present in the python module
    print('tearDownModule')


class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self):  # execute before all test methods
        print("This is signup test")

    @classmethod
    def tearDown(self):  # Execute after all test methods
        print("This is logout test")

    @classmethod
    def setUpClass(cls):  # Execute once when the class started
        print("Open Application")

    @classmethod
    def tearDownClass(cls):  # Execute once after the class completed
        print("Close Application")

    def test_search(self):
        print('This is search test')

    def test_advanced_search(self):
        print("This is Advanced search test")

    def test_prepaid_recharge(self):
        print("This is prepaid recharge test")

    def test_postpaid_recharge(self):
        print("This is post-paid recharge test")


if __name__ == "__main__":
    unittest.main()
