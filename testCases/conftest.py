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

################### Pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Pavan'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)