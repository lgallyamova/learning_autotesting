from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class Test1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r'C:\Users\ludmi\geckodriver')

    def test_search_in_selenium_documentation(self):
        driver = self.driver
        print(driver.capabilities)
        driver.get("https://seleniumhq.github.io/docs/")
        self.assertIn("Selenium", driver.title)
        elem = driver.find_element_by_link_text("Narrative documentation")
        elem.click()
        elem = driver.find_element_by_link_text("WebDriver")
        elem.click()
        elem = driver.find_element_by_link_text("Getting Started")
        elem.click()


    def tearDown(self):
        self.driver.close()

class Test2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r'C:\Users\ludmi\geckodriver')

    def test_search_in_selenium_documentation(self):
        driver = self.driver
        driver.get("https://www.python.org")
        elem = driver.find_element_by_id("id-search-field")
        elem.send_keys('python + selenium')
        elem.send_keys(Keys.ENTER)
        time.sleep(2)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()