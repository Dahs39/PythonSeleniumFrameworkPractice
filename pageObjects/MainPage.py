# https://rahulshettyacademy.com/angularpractice/
from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    shopBtn = (By.LINK_TEXT, "Shop")

    def shopLink(self):
        return self.driver.find_element(*MainPage.shopBtn)
        # driver.find_element(By.LINK_TEXT, "Shop")