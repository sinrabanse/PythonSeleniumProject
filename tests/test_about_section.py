import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import CartPage
from pages.client_info_page import ClientInfoPage
from pages.finish_page import FinishPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.payment_page import PaymentPage


def test_about_section ():
    driver = webdriver.Chrome()

    print("Start Test")

    login = LoginPage(driver)
    login.autorization()

    mp = MainPage(driver)
    mp.select_menu_about()

    print("Finish Test")

    time.sleep(5)
    driver.quit()