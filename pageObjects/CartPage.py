from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    continueShoppingBtn = (By.CSS_SELECTOR, ".btn.btn-default")

    def continueShopping(self):
        return self.driver.find_element(*CartPage.continueShoppingBtn)

    cartCheckoutBtn = (By.CSS_SELECTOR, ".btn.btn-success")

    def cartCheckoutPageBtn(self):
        return self.driver.find_element(*CartPage.cartCheckoutBtn)