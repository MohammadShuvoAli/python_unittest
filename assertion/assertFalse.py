import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def test_website_title(self):
        driver = webdriver.Chrome()
        driver.get("https://www.google.com/")
        page_title = driver.title
        self.assertFalse(page_title == "google")


if __name__ == "__main__":
    unittest.main()