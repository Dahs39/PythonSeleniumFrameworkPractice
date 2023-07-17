from selenium.webdriver.common.by import By


class PurchaseConfirmationPage:

    def __init__(self, driver):
        self.driver = driver

    countryTextElement = (By.ID, "country")
    def typeCountryName(self):
        return self.driver.find_element(*PurchaseConfirmationPage.countryTextElement)

    usaResult = (By.LINK_TEXT, "United States of America")
    def selectUSA(self):
        return self.driver.find_element(*PurchaseConfirmationPage.usaResult)

    termsCheckbox = (By.CSS_SELECTOR, ".checkbox.checkbox-primary")
    def clickTermsCheckbox(self):
        return self.driver.find_element(*PurchaseConfirmationPage.termsCheckbox)

    purchaseButton = (By.CSS_SELECTOR, ".btn.btn-success.btn-lg")

    def confirmPurchase(self):
        return self.driver.find_element(*PurchaseConfirmationPage.purchaseButton)
