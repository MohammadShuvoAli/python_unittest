import unittest


class Test(unittest.TestCase):
    def testName(self) :
        list = ("python", "selenium", "unittest", "pytest")
        self.assertIn("python", list) # passed
        # self.assertln("ruby", list) # failed


if __name__ == "__main__":
    unittest.main()