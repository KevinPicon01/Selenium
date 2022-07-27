import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By

class SearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'./chromedriver')
        driver = cls.driver
        driver.implicitly_wait(10)
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_search_tee(self):
        driver = self.driver
        search = driver.find_element(By.NAME, 'q')
        search.clear()
        search.send_keys('tee')
        search.submit()

    def test_search_salt(self):
        driver = self.driver
        search = driver.find_element(By.NAME, 'q')
        search.clear()
        search.send_keys('salt shaker')
        search.submit()

        # products = driver.find_elements(By.XPATH, '//*[@id="search"]/div[1]/div[2]/ul/li/div/h2/a')
        # self.assertEqual(len(products), 2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='HelloWorld'))

