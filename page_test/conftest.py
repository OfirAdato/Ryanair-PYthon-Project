import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture(scope="class")
def driverd(request):
    options = Options()
    options.add_argument(
        "user-data-dir=C:\\Users\\linoy\\AppData\\Local\\Google\\Chrome\\User Data\\profile-directory=Profile 5")
    service = ChromeService(executable_path="D:\\Python\\Python311\\Scripts\\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_page_load_timeout(30)  # Set page load timeout
    driver.set_script_timeout(30)  # Set script timeout
    request.cls.driver = driver
    driver.maximize_window()
    yield driver
    driver.quit()
