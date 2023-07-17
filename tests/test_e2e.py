import pytest
from pageObjects.PurchaseConfirmationPage import PurchaseConfirmationPage
from pageObjects.CartPage import CartPage
from pageObjects.MainPage import MainPage
from pageObjects.ShopPage import ShopPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Utilities.Utilities import BaseClass


class TestOrderingPhone(BaseClass):
    def test_orderingPhone(self):
        mainPage = MainPage(self.driver)
        shopPage = ShopPage(self.driver)
        cartPage = CartPage(self.driver)
        purchaseConfirmationPage = PurchaseConfirmationPage(self.driver)

        mainPage.shopLink().click()
        # shopItem = self.driver.find_element(By.LINK_TEXT, "Shop")
        # shopItem.click()

        # Assert that the right phones have been returned?
        phoneOptions = shopPage.phoneOptions()
        # phoneOptions = self.driver.find_elements(By.CSS_SELECTOR, ".card-title")
        for phone in phoneOptions:
            print(phone.text)
            if phone.text == "Nokia Edge":
                shopPage.addPhoneToCart().click()
                # addToCartBtn = self.driver.find_element(By.XPATH, "//body[1]/app-root[1]/app-shop[1]/div[1]/div[1]/div[2]/app-card-list[1]/app-card[3]/div[1]/div[2]/button[1]")
                # addToCartBtn.click()

        shopPage.checkout().click()
        # checkoutBtn = self.driver.find_element(By.CSS_SELECTOR, ".nav-link.btn.btn-primary")
        # checkoutBtn.click()

        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-default")))

        cartPage.continueShopping().click()
        # continueShoppingBtn = self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-default")
        # continueShoppingBtn.click()

        # Issue where the Continue Shopping doesn't save your cart so this just adds Samsung Note 8 to cart now
        phoneOptions = shopPage.phoneOptions()
        # phoneOptions = self.driver.find_elements(By.CSS_SELECTOR, ".card-title")
        for phone in phoneOptions:
            print(phone.text)
            if phone.text == "Samsung Note 8":
                shopPage.addPhoneToCart2().click()
                # addToCartBtn = self.driver.find_element(By.XPATH, "//body[1]/app-root[1]/app-shop[1]/div[1]/div[1]/div[2]/app-card-list[1]/app-card[2]/div[1]/div[2]/button[1]")
                # addToCartBtn.click()

        shopPage.checkout().click()
        # checkoutBtn = self.driver.find_element(By.CSS_SELECTOR, ".nav-link.btn.btn-primary")
        # checkoutBtn.click()

        # Check cart has the right item, right quantity, right price, right total?

        cartPage.cartCheckoutPageBtn().click()
        # cartCheckoutBtn = self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-success")
        # cartCheckoutBtn.click()

        purchaseConfirmationPage.typeCountryName().send_keys("United States")
        # countryLocation = self.driver.find_element(By.ID, "country")
        # countryLocation.send_keys("United States")

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "United States of America")))

        purchaseConfirmationPage.selectUSA().click()
        # usaLink = self.driver.find_element(By.LINK_TEXT, "United States of America")
        # usaLink.click()

        purchaseConfirmationPage.clickTermsCheckbox().click()
        # termsCheckbox = self.driver.find_element(By.CSS_SELECTOR, ".checkbox.checkbox-primary")
        # termsCheckbox.click()

        purchaseConfirmationPage.confirmPurchase().click()
        # purchaseBtn = self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-success.btn-lg")
        # purchaseBtn.click()

class TestSubmitAccountInfo(BaseClass):
    def test_submittingAccountInformation(self):
        nameSpace = self.driver.find_element(By.CSS_SELECTOR, ".form-control")
        nameSpace.send_keys("David")

        emailSpace = self.driver.find_element(By.NAME, "email")
        emailSpace.send_keys("testEmail@gmail.com")

        passwordSpace = self.driver.find_element(By.ID, "exampleInputPassword1")
        passwordSpace.send_keys("test123")

        iceCreamCheckBox = self.driver.find_element(By.ID, "exampleCheck1")
        iceCreamCheckBox.click()

        genderDropdown = Select(self.driver.find_element(By.ID, "exampleFormControlSelect1"))
        genderDropdown.select_by_visible_text('Female')

        employmentStatus = self.driver.find_element(By.ID, "exampleFormControlSelect1")
        employmentStatus.click()

        bday = self.driver.find_element(By.NAME, "bday")
        bday.send_keys("01/01/2001")

        submitBtn = self.driver.find_element(By.CLASS_NAME, "btn-success")
        submitBtn.click()
