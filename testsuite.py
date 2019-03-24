from selenium import webdriver
import unittest
from time import sleep
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import HTMLTestRunner
class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

class PageLocators():
    LoginPageEmailField = (By.ID, "email")
    LoginPagePasswordField = (By.ID, "password")
    LoginPageLoginButton = (By.TAG_NAME, "button")
    properties_link=(By.XPATH, "//a[@href='/property/properties']")
    aggregate_link=(By.XPATH, "//a[@href='/property/aggregate']")
    responses_link = (By.XPATH, "//a[@href='/property/responses/']")
    reviews_link = (By.XPATH, "//a[@href='/account/reviews/']")
    search_field=(By.XPATH, "//*[@id='DataTables_Table_1_filter']/label/input")
    imp_usr=(By.XPATH, "//*[@id='DataTables_Table_1']/tbody/tr[1]/td[3]/a ")

class Login(BasePage):
    def enter_mail(self,email):
       entermail=self.driver.find_element(*PageLocators.LoginPageEmailField)
       entermail.send_keys(email)
    def search_text(self):
       txt=self.driver.find_element(*PageLocators.search_field)
       txt.send_keys("user")
       print("Searching user")
       txt.send_keys((Keys.ENTER))
       self.driver.assertTrue(self.driver.is_element_present(*PageLocators.search_field))
       #self.driver.assertTrue(self.driver.is_element_presentis_element_present(By.XPATH, "@id='DataTables_Table_1_filter']/label/input"))
    def enter_password(self, password):
        enterpswd = self.driver.find_element(*PageLocators.LoginPagePasswordField)
        enterpswd.send_keys(password)

    def click_login(self):
        login=self.driver.find_element(*PageLocators.LoginPageLoginButton)
        login.click()
        assert ('https://ratingstracker-staging.ainfo.io/account/super' == self.driver.current_url)
        print(self.driver.current_url)
        print("Successful Login")

    def click_properties(self):
        properties = self.driver.find_element(*PageLocators.properties_link)
        properties.click()
        assert ('https://ratingstracker-staging.ainfo.io/property/properties' == self.driver.current_url)
        print(self.driver.current_url)

    def click_aggregate(self):
        aggregate=self.driver.find_element(*PageLocators.aggregate_link)
        aggregate.click()
        assert ('' in self.driver.current_url)
        print(self.driver.current_url)

    def click_responses(self):
        responses = self.driver.find_element(*PageLocators.responses_link)
        responses.click()
        assert ('' in self.driver.current_url)
        print(self.driver.current_url)

    def click_reviews(self):
        reviews = self.driver.find_element(*PageLocators.reviews_link)
        reviews.click()
        assert ('' in self.driver.current_url)
        print(self.driver.current_url)
    def impersonate_user(self):
        usr=self.driver.find_element(*PageLocators.imp_usr)
        usr.click()

class basic_test(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        inst.driver = webdriver.Chrome()
        inst.driver.get('https://ratingstracker-staging.ainfo.io/')
        #time.sleep(3)
        self.driver.maximize_window()

    def test_successful_login(self):
        main_page=Login(self.driver)
        main_page.enter_mail("super@super.com")
        main_page.enter_password("root")
        main_page.click_login()
        main_page.search_text()
        main_page.impersonate_user()
        ''' 
        main_page.click_properties()
        self.driver.back()
        main_page.click_aggregate()
        self.driver.back()
        main_page.click_responses()
        self.driver.back()
        main_page.click_responses()
        self.driver.back()
        '''
    @classmethod
    def tearDownClass(inst):
        inst.driver.quit()

class search_test(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        inst.driver = webdriver.Chrome()
        inst.driver.get('https://ratingstracker-staging.ainfo.io/')
        #time.sleep(3)
        self.driver.maximize_window()

    def test_successful_login(self):
        main_page=Login(self.driver)
        main_page.enter_mail("super@super.com")
        main_page.enter_password("root")
        main_page.click_login()
        main_page.search_text()
        main_page.impersonate_user()
        ''' 
        main_page.click_properties()
        self.driver.back()
        main_page.click_aggregate()
        self.driver.back()
        main_page.click_responses()
        self.driver.back()
        main_page.click_responses()
        self.driver.back()
        '''
    @classmethod
    def tearDownClass(inst):
        inst.driver.quit()


if __name__ == "__main__":
    unittest.main()







