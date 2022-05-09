from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")
        return driver
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        return driver
    else:
        driver = webdriver.Chrome()
        return driver

def pytest_addoption(parser): # This will get the value from the CLI hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #This will returnn the Browser value to setup method
    return request.config.getoption("--browser")

