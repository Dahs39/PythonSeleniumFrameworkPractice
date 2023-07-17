# https://rahulshettyacademy.com/angularpractice/shop
from selenium.webdriver.common.by import By


class ShopPage:

    def __init__(self, driver):
        self.driver = driver

    phoneOptionsElements = (By.CSS_SELECTOR, ".card-title")
    def phoneOptions(self):
        return self.driver.find_elements(*ShopPage.phoneOptionsElements)
        # phoneOptions = self.driver.find_elements(By.CSS_SELECTOR, ".card-title")

    # For Nokia Edge
    addToCartBtn = (By.XPATH, "//body[1]/app-root[1]/app-shop[1]/div[1]/div[1]/div[2]/app-card-list[1]/app-card[3]/div[1]/div[2]/button[1]")

    def addPhoneToCart(self):
        return self.driver.find_element(*ShopPage.addToCartBtn)

    # For Samsung Note 8
    addToCartBtn2 = (By.XPATH, "//body[1]/app-root[1]/app-shop[1]/div[1]/div[1]/div[2]/app-card-list[1]/app-card[2]/div[1]/div[2]/button[1]")

    def addPhoneToCart2(self):
        return self.driver.find_element(*ShopPage.addToCartBtn2)

    checkOutBtn = (By.CSS_SELECTOR, ".nav-link.btn.btn-primary")

    def checkout(self):
        return self.driver.find_element(*ShopPage.checkOutBtn)