import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def test_website_title(self):
        driver = webdriver.Chrome()
        value = None # if value is used then we get True and test passed
        self.assertIsNone(driver) # False Test Failed


if __name__ == "__main__":
    unittest.main()