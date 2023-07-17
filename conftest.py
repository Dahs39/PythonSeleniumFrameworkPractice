import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Passing different values through command line, from https://docs.pytest.org/en/7.1.x/example/simple.html
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Specify browser to run test in: chrome, firefox, or safari"
    )
@pytest.fixture(scope="class") # Executes at the beginning of the class once, instead of for each test
def setup(request):
    browserName = request.config.getoption("browser")
    if browserName == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        service_obj = Service("C:\Python\chromedriver_win32\chromedriver.exe");
        driver = webdriver.Chrome(options=options, service=service_obj)
    elif browserName == "firefox":
        service_obj = Service("C:\Python\geckodriver-v0.33.0-win32\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.implicitly_wait(2)
    driver.maximize_window()
    request.cls.driver = driver  # assigning local fixture to class driver
    yield
    driver.close()