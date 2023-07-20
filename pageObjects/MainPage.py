# https://rahulshettyacademy.com/angularpractice/
from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    shopBtn = (By.LINK_TEXT, "Shop")
    def shopLink(self):
        return self.driver.find_element(*MainPage.shopBtn)
        # driver.find_element(By.LINK_TEXT, "Shop")

    enterNameBoxElement = (By.CSS_SELECTOR, ".form-control")
    def enterNameBox(self):
        return self.driver.find_element(*MainPage.enterNameBoxElement)

    emailBoxElement = (By.NAME, "email")
    def enterEmailBox(self):
        return self.driver.find_element(*MainPage.emailBoxElement)

    passwordBoxElement = (By.ID, "exampleInputPassword1")
    def enterPasswordBox(self):
        return self.driver.find_element(*MainPage.passwordBoxElement)

    iceCreamCheckBoxElement = (By.ID, "exampleCheck1")
    def iceCreamCheckBox(self):
        return self.driver.find_element(*MainPage.iceCreamCheckBoxElement)

    employmentStatus = (By.ID, "exampleFormControlSelect1")
    def chooseEmploymentStatus(self):
        return self.driver.find_element(*MainPage.employmentStatus)

    bdayElement = (By.NAME, "bday")
    def chooseBday(self):
        return self.driver.find_element(*MainPage.bdayElement)

    submitBtnElement = (By.CLASS_NAME, "btn-success")
    def submitForm(self):
        return self.driver.find_element(*MainPage.submitBtnElement)