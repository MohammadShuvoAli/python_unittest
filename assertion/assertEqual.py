import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def test_website_title(self):
        driver = webdriver.Chrome()
        driver.get("https://www/google.com/")

        page_title = driver.title
        self.assertEqual("Google", page_title, "Page Title Same!!!")


if __name__ == "__main__":
    unittest.main()