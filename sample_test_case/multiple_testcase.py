import unittest
from selenium import webdriver


class SearchEngineTest(unittest.TestCase):
    def test_Google(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.com")
        print("Title of the page:", self.driver.title)

    def test_Bing(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.bing.com")
        print("Title of the page:", self.driver.title)


if __name__ == "__main__":
    unittest.main()
