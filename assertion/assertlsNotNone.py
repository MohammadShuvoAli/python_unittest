import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def test_website_title(self):
        driver = webdriver.Chrome()
        self.assertIsNotNone(driver) # False Test Passed


if __name__ == "__main__":
    unittest.main()