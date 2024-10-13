import pytest
import time
from selenium import webdriver
from Utilities import ReadConfiguration


@pytest.fixture()
def setup_and_teardown(request):
    browser = ReadConfiguration.read_configuration("basic info", "browser")
    driver = None
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("Provide valid browser from the list chrome/firefox,edge")
    driver.maximize_window()
    app_url = ReadConfiguration.read_configuration("basic info", "url")
    driver.get(app_url)
    request.cls.driver = driver
    time.sleep(2)
    yield
    driver.quit()
