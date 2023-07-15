import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service_obj = Service("C:\Python\chromedriver_win32\chromedriver.exe");
driver = webdriver.Chrome(options=options, service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.implicitly_wait(2)
driver.maximize_window()

# Check title of page?
shopItem = driver.find_element(By.LINK_TEXT, "Shop")
shopItem.click()

# Assert that the right phones have been returned?
phoneOptions = driver.find_elements(By.CSS_SELECTOR, ".card-title")
for phone in phoneOptions:
    print(phone.text)
    if phone.text == "Nokia Edge":
        addToCartBtn = driver.find_element(By.XPATH, "//body[1]/app-root[1]/app-shop[1]/div[1]/div[1]/div[2]/app-card-list[1]/app-card[3]/div[1]/div[2]/button[1]")
        addToCartBtn.click()

checkoutBtn = driver.find_element(By.CSS_SELECTOR, ".nav-link.btn.btn-primary")
checkoutBtn.click()


wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-default")))\

continueShoppingBtn = driver.find_element(By.CSS_SELECTOR, ".btn.btn-default")
continueShoppingBtn.click()

# Issue where the Continue Shopping doesn't save your cart so this just adds Samsung Note 8 to cart now
phoneOptions = driver.find_elements(By.CSS_SELECTOR, ".card-title")
for phone in phoneOptions:
    print(phone.text)
    if phone.text == "Samsung Note 8":
        addToCartBtn = driver.find_element(By.XPATH, "//body[1]/app-root[1]/app-shop[1]/div[1]/div[1]/div[2]/app-card-list[1]/app-card[2]/div[1]/div[2]/button[1]")
        addToCartBtn.click()

checkoutBtn = driver.find_element(By.CSS_SELECTOR, ".nav-link.btn.btn-primary")
checkoutBtn.click()

# Check cart has the right item, right quantity, right price, right total?

cartCheckoutBtn = driver.find_element(By.CSS_SELECTOR, ".btn.btn-success")
cartCheckoutBtn.click()

countryLocation = driver.find_element(By.ID, "country")
countryLocation.send_keys("United States")

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "United States of America")))

usaLink = driver.find_element(By.LINK_TEXT, "United States of America")
usaLink.click()

termsCheckbox = driver.find_element(By.ID, "checkbox2")
termsCheckbox.click()

purchaseBtn = driver.find_element(By.CSS_SELECTOR, ".btn.btn-success.btn-lg")
purchaseBtn.click()
