from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from pages.login_page import LoginPage


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators

    checkout_button = '//button[@id="checkout"]'

    #getters

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))


    #actions

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click checkout button")

    #methods

    def product_confirmation(self):
        self.get_current_url()
        self.click_checkout_button()

