from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from LogIn import LogIn

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class PageLocators():
    search_field = (By.XPATH, "//*[@id='DataTables_Table_1_filter']/label/input")
    imp_usr = (By.XPATH, "//*[@id='DataTables_Table_1']/tbody/tr[3]/td[3]/a ")
    map_link = (By.XPATH, "//a[@href='/property/maps']")
    properties_link = (By.XPATH, "//a[@href='/property/properties']")
    comps_link = (By.XPATH, "//a[@href='/property/competition/']")
    usr_link = (By.XPATH, "//a[@href='/account/user/']")
    # ora_link = (By.XPATH, "//a[@href='/report/']")
    summ_link = (By.XPATH, "//a[@href='/property/reviews/']")
    stop_link = (By.XPATH, "//a[@href='/impersonate/stop/']")


class UserImpersonate(BasePage):
    def search_text(self):
        txt = self.driver.find_element(*PageLocators.search_field)
        txt.send_keys("user")
        print("Searching user")
        txt.send_keys(Keys.ENTER)

    def impersonate_user(self):
        usr = self.driver.find_element(*PageLocators.imp_usr)
        print(usr.text)
        usr.click()
        assert ('https://ratingstracker-staging.ainfo.io/property/properties' == self.driver.current_url)
        time.sleep(10)
        print('Impersonated as User')

    def click_map(self):
        mapy = self.driver.find_element(*PageLocators.map_link)
        mapy.click()
        time.sleep(4)
        assert ('https://ratingstracker-staging.ainfo.io/property/maps' == self.driver.current_url)
        print(self.driver.current_url)

    def click_properties(self):
        properties = self.driver.find_element(*PageLocators.properties_link)
        properties.click()
        assert ('https://ratingstracker-staging.ainfo.io/property/properties' == self.driver.current_url)
        print(self.driver.current_url)

    def click_competition(self):
        comp = self.driver.find_element(*PageLocators.comps_link)
        comp.click()
        time.sleep(4)
        assert ('https://ratingstracker-staging.ainfo.io/property/competition/' == self.driver.current_url)
        print(self.driver.current_url)

    def click_user(self):
        userz = self.driver.find_element(*PageLocators.usr_link)
        userz.click()
        time.sleep(4)
        assert ('https://ratingstracker-staging.ainfo.io/account/user/' == self.driver.current_url)
        print(self.driver.current_url)

    def click_summary(self):
        summary = self.driver.find_element(*PageLocators.summ_link)
        summary.click()
        time.sleep(4)
        assert ('https://ratingstracker-staging.ainfo.io/property/reviews/' == self.driver.current_url)
        print(self.driver.current_url)
        #national_average = self.driver.find_element(*PageLocators.nat_avg)
        #print("National Average Of this user is " + national_average.text)
    def click_stop(self):
        stp = self.driver.find_element(*PageLocators.stop_link)
        stp.click()
        assert ('https://ratingstracker-staging.ainfo.io/account/super' == self.driver.current_url)
        print(self.driver.current_url)


class UserTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://ratingstracker-staging.ainfo.io/account/super')
        time.sleep(3)
        self.driver.maximize_window()

    def test_impersonate_user(self):

        main_page = LogIn(self.driver)
        main_page.enter_mail("super@super.com")
        main_page.enter_password("classify")
        main_page.click_login()
        nav_page = UserImpersonate(self.driver)
        nav_page.search_text()
        nav_page.impersonate_user()
        nav_page.click_map()
        nav_page.click_competition()
        nav_page.click_user()
        nav_page.click_summary()
        nav_page.click_stop()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()



