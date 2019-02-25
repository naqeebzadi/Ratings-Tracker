from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class PageLocators():
    LoginPageEmailField = (By.ID, "email")
    LoginPagePasswordField = (By.ID, "password")
    LoginPageLoginButton = (By.TAG_NAME, "button")
    nat_avg = (By.CSS_SELECTOR, "//*[@id='highcharts-5vx9xre-0']/div/div/span/div/span[1]")


class LogIn(BasePage):
    def enter_mail(self,email):
       entermail=self.driver.find_element(*PageLocators.LoginPageEmailField)
       entermail.send_keys(email)

    def enter_password(self, password):
        enterpswd = self.driver.find_element(*PageLocators.LoginPagePasswordField)
        enterpswd.clear()
        enterpswd.send_keys(password)

    def click_login(self):
        login = self.driver.find_element(*PageLocators.LoginPageLoginButton)
        login.click()
        assert ('https://ratingstracker-staging.ainfo.io/account/super' == self.driver.current_url)
        print(self.driver.current_url)
        print("Successful Login")


class LogInTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://ratingstracker-staging.ainfo.io')
        #time.sleep(3)
        self.driver.maximize_window()

    def test_successful_login(self):

        main_page = LogIn(self.driver)
        main_page.enter_mail("super@super.com")
        main_page.enter_password("classify")
        main_page.click_login()


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


