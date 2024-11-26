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
    select_product_2 = '//button[@id="add-to-cart-sauce-labs-bike-light"]'
    select_product_3  = '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'
    cart = '//div[@id="shopping_cart_container"]'
    side_menu = '//button[@id="react-burger-menu-btn"]'
    side_menu_about = '//a[@id="about_sidebar_link"]'

    #getters

    def get_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_2)))

    def get_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_3)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_side_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.side_menu)))

    def get_side_menu_about(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.side_menu_about)))


    #actions

    def click_select_product_1(self):
        self.get_product_1().click()
        print("Add to cart product 1")

    def click_select_product_2(self):
        self.get_product_2().click()
        print("Add to cart product 2")

    def click_select_product_3(self):
        self.get_product_3().click()
        print("Add to cart product 3")

    def click_to_cart(self):
        self.get_cart().click()
        print("Click to cart")

    def click_side_menu(self):
        self.get_side_menu().click()
        print("Click side menu")

    def click_side_menu_about(self):
        self.get_side_menu_about().click()
        print("Click About in side menu")

    #methods

    def add_to_cart_product_1(self):
        self.get_current_url()
        self.click_select_product_1()
        self.click_to_cart()

    def add_to_cart_product_2(self):
        self.get_current_url()
        self.click_select_product_2()
        self.click_to_cart()

    def add_to_cart_product_3(self):
        self.get_current_url()
        self.click_select_product_3()
        self.click_to_cart()

    def select_menu_about(self):
        self.get_current_url()
        self.click_side_menu()
        self.click_side_menu_about()
        self.assert_url('https://saucelabs.com/')