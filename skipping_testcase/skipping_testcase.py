import unittest


class AppTesting(unittest.TestCase):

    @unittest.SkipTest # decorator
    def test_search(self):
        print("This is search test")

    @unittest.skip("Skipping Test Not Ready Yet!!!")
    def test_advancedsearch(self):
        print("This is advance search method")

    @unittest.skipIf(1 == 1, "1==1 : True")
    def test_prepaidrecharge(self):
        print("This is pre—paid recharge")

    def test_postpaidreachrge(self):
        print("This is post—paid recharge")

    def test_loginbygamil(self):
        print("This is login by email")

    def test_loginbytwitter(self):
        print("This is login by twitter")

if __name__ == "__main__":
    unittest.main()