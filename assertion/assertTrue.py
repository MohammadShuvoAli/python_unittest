import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def test_website_title(self):
        driver = webdriver.Chrome()
        driver.get("https://www.google.com/")
        page_title = driver.title
        self.assertTrue(page_title == "Google") # True


if __name__ == "__main__":
    unittest.main()