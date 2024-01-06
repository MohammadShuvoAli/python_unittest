import unittest

class Test(unittest.TestCase):
    def testName (self):
        self. assertLessEqual(10, 100) # if a<b or a==b then True
        self.assertLess(10, 100) # if a<b then True
        self.assertGreater(100, 10) # if a>b then True
        self.assertGreaterEqual(100, 100) # if a>b or a==b then True


if __name__ == "__main__":
    unittest.main()