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
from PIL import Image


class TestOrderingPhone(BaseClass):

    # Test will order a Samsung Note 8 phone
    def test_orderingPhone(self):
        mainPage = MainPage(self.driver)
        shopPage = ShopPage(self.driver)
        cartPage = CartPage(self.driver)
        purchaseConfirmationPage = PurchaseConfirmationPage(self.driver)

        mainPage.shopLink().click()

        phoneOptions = shopPage.phoneOptions()

        for phone in phoneOptions:
            print(phone.text)
            if phone.text == "Nokia Edge":
                shopPage.addPhoneToCart().click()

        shopPage.checkout().click()

        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-default")))

        cartPage.continueShopping().click()

        phoneOptions = shopPage.phoneOptions()

        for phone in phoneOptions:
            print(phone.text)
            if phone.text == "Samsung Note 8":
                shopPage.addPhoneToCart2().click()

        shopPage.checkout().click()

        cartPage.cartCheckoutPageBtn().click()

        purchaseConfirmationPage.typeCountryName().send_keys("United States")

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "United States of America")))

        purchaseConfirmationPage.selectUSA().click()

        purchaseConfirmationPage.clickTermsCheckbox().click()

        purchaseConfirmationPage.confirmPurchase().click()
        self.driver.save_screenshot("PurchaseCompleted.png")

class TestSubmitAccountInfo(BaseClass):

    # Test will submit all details needed for registering an account
    def test_submittingAccountInformation(self):
        mainPage = MainPage(self.driver)

        mainPage.enterNameBox().send_keys("David")

        mainPage.enterEmailBox().send_keys("testEmail@gmail.com")

        mainPage.enterPasswordBox().send_keys("test123")

        mainPage.iceCreamCheckBox().click()

        genderDropdown = Select(self.driver.find_element(By.ID, "exampleFormControlSelect1"))
        genderDropdown.select_by_visible_text('Female')

        mainPage.chooseEmploymentStatus().click()

        mainPage.chooseBday().send_keys("01/01/2001")

        mainPage.submitForm().click()

        self.driver.save_screenshot("InfoSubmitCompleted.png")
