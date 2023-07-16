import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="class") # Executes at the beginning of the class once, instead of for each test
def setup(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    service_obj = Service("C:\Python\chromedriver_win32\chromedriver.exe");
    driver = webdriver.Chrome(options=options, service=service_obj)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.implicitly_wait(2)
    driver.maximize_window()
    request.cls.driver = driver  # assigning local fixture to class driver
    yield
    driver.close()