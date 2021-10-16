import pytest
import time
from PageObjects.LoginPage import LoginPage
from PageObjects.AddCustomerPage import AddCustomerPage
from PageObjects.SearchCustomerPage import SearchCustomer
from Utilities.Readproperties import ReadConfig
from Utilities.customlogger import LogGen


class Test_SearchCustomerByEmail_TC004:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_SearchCustomerByEmail(self, setup):
        self.logger.info("**********Test_004_Search Customer By Email************")
        self.driver = setup
        # self.driver = webdriver.Chrome(executable_path="C:\\Users\\Chetan Ramesh\\Desktop\\Selenium2021"
        # "\\chromedriver_win32\\chromedriver.exe")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(2)

        self.logger.info("*************Login is Successful****************")

        self.logger.info("*************Start Search Customer By Email Test************")

        self.addcust = AddCustomerPage(self.driver)
        self.addcust.ClickOnCustomerMenu()
        time.sleep(2)
        self.addcust.ClickOnCustomerSubMenu()

        self.logger.info("*************Searching Customer By Email ID************")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.getSearchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True == status
        self.logger.info("*************Test_004_Search Customer By Email is finished************")
        self.driver.close()
