import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By

class HelloWorld(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'./chromedriver')
        driver = cls.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.implicitly_wait(10)

    def test_register_new_user(self):
        self.driver.find_element(By.XPATH,'//*[@id="header"]/div/div[2]/div/a/span[2]').click()
        self.driver.find_element(By.XPATH,'//*[@id="header-account"]/div/ul/li[5]/a').click()
        self.driver.find_element(By.ID,'firstname').send_keys('Juan')
        self.driver.find_element(By.ID,'lastname').send_keys('Perez')
        self.driver.find_element(By.ID,'email_address').send_keys('juan@perez.com')
        self.driver.find_element(By.ID,'password').send_keys('12345678')
        self.driver.find_element(By.ID,'confirmation').send_keys('12345678')
        self.driver.find_element(By.XPATH, '//*[@id="form-validate"]/div[2]/button').click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='HelloWorld'))


