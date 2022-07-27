import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Assertion(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('http://demo-store.seleniumacademy.com/')

    def test_search_field_exists(self):
        self.assertTrue(self.is_elements_present(By.NAME, 'q'))

    def test_language_option(self):
        self.assertTrue(self.is_elements_present(By.ID, 'select-language'))




    # def test_search(self):
    #     driver = self.driver
    #     search = driver.find_element(By.NAME, 'q')
    #     search.send_keys('hola')
    #     search.submit()
    #     try:
    #         driver.find_elements(By.XPATH, '//*[@id="search"]/div[1]/div[2]/div/span[2]/span')
    #         assert True
    #     except NoSuchElementException:
    #         assert False

    def tearDown(self):
        self.driver.quit()

    # def is_elements_present(self, how, what):
    #     try:
    #         self.driver.find_element(by=how, value=what)
    #         return True
    #     except NoSuchElementException:
    #         return False