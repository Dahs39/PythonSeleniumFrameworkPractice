import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Utilities.Utilities import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        shopItem = self.driver.find_element(By.LINK_TEXT, "Shop")
        shopItem.click()

        # Assert that the right phones have been returned?
        phoneOptions = self.driver.find_elements(By.CSS_SELECTOR, ".card-title")
        for phone in phoneOptions:
            print(phone.text)
            if phone.text == "Nokia Edge":
                addToCartBtn = self.driver.find_element(By.XPATH, "//body[1]/app-root[1]/app-shop[1]/div[1]/div[1]/div[2]/app-card-list[1]/app-card[3]/div[1]/div[2]/button[1]")
                addToCartBtn.click()

        checkoutBtn = self.driver.find_element(By.CSS_SELECTOR, ".nav-link.btn.btn-primary")
        checkoutBtn.click()


        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-default")))

        continueShoppingBtn = self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-default")
        continueShoppingBtn.click()

        # Issue where the Continue Shopping doesn't save your cart so this just adds Samsung Note 8 to cart now
        phoneOptions = self.driver.find_elements(By.CSS_SELECTOR, ".card-title")
        for phone in phoneOptions:
            print(phone.text)
            if phone.text == "Samsung Note 8":
                addToCartBtn = self.driver.find_element(By.XPATH, "//body[1]/app-root[1]/app-shop[1]/div[1]/div[1]/div[2]/app-card-list[1]/app-card[2]/div[1]/div[2]/button[1]")
                addToCartBtn.click()

        checkoutBtn = self.driver.find_element(By.CSS_SELECTOR, ".nav-link.btn.btn-primary")
        checkoutBtn.click()

        # Check cart has the right item, right quantity, right price, right total?

        cartCheckoutBtn = self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-success")
        cartCheckoutBtn.click()

        countryLocation = self.driver.find_element(By.ID, "country")
        countryLocation.send_keys("United States")

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "United States of America")))

        usaLink = self.driver.find_element(By.LINK_TEXT, "United States of America")
        usaLink.click()

        # Using Actions class to click on checkbox
        termsCheckbox = self.driver.find_element(By.CSS_SELECTOR, ".checkbox.checkbox-primary")
        termsCheckbox.click()

        purchaseBtn = self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-success.btn-lg")
        purchaseBtn.click()
