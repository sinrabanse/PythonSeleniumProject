from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from pages.login_page import LoginPage


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators

    select_product_1 = '//button[@id="add-to-cart-sauce-labs-backpack"]'
    cart = '//div[@id="shopping_cart_container"]'

    #getters

    def get_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))


    #actions

    def click_select_product_1(self):
        self.get_product_1().click()
        print("Add to cart product 1")

    def click_to_cart(self):
        self.get_cart().click()
        print("Click to cart")

    #methods

    def add_to_cart(self):
        self.get_current_url()
        self.click_select_product_1()
        self.click_to_cart()

