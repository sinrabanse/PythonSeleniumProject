from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class ClientInfoPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators

    first_name_locator = '//input[@id="first-name"]'
    last_name_locator = '//input[@id="last-name"]'
    postal_code_locator = '//input[@id="postal-code"]'
    continue_button = '//input[@id="continue"]'

    #getters

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name_locator)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name_locator)))

    def get_postal_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.postal_code_locator)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))


    #actions

    def fill_first_name(self, client_first_name):
        self.get_first_name().send_keys(client_first_name)
        print("Input Client First Name")

    def fill_last_name(self, client_last_name):
        self.get_last_name().send_keys(client_last_name)
        print("Input Client Last Name")

    def fill_postal_code(self, client_postal_code):
        self.get_postal_code().send_keys(client_postal_code)
        print("Input Client postal code")

    def click_continue_button(self):
        self.get_continue_button().click()
        print("Click Continue Button")

    #methods

    def fill_client(self):
        self.get_current_url()
        self.fill_first_name("Aleks")
        self.fill_last_name("Arkh")
        self.fill_postal_code(1231231)
        self.click_continue_button()

