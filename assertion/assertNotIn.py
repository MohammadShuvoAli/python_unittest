import unittest


class Test(unittest.TestCase):
    def testName(self) :
        list = ("python", "selenium", "unittest", "pytest")
        # self.assertNotIn ("python", list) # failed
        self.assertNotIn("ruby", list) # passed


if __name__ == "__main__":
    unittest.main()