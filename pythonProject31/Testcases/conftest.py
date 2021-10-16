from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome(executable_path="C:\\Users\\Chetan Ramesh\\Desktop\\Selenium2021\\chromedriver_win32\\chromedriver.exe")
        print("Launching Chrome Browser")
    elif browser=='firefox':
        driver=webdriver.Firefox(executable_path="C:\\Users\\Chetan Ramesh\\Desktop\\Selenium2021\\geckodriver-v0.30.0-win64\\geckodriver.exe")
        print("Launching Firefox Browser")
    else:
        driver = webdriver.Ie(
            executable_path="C:\\Users\\Chetan Ramesh\\Desktop\\Selenium2021\\IEDriverServer_x64_3.150.2\\IEDriverServer.exe")

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")





def pytest_configure(config):
    config._metadata['Project Name'] = 'nop commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Project Name'] = 'nop commerce project'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

