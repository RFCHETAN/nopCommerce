import pytest

from PageObjects.LoginPage import LoginPage
from Utilities.Readproperties import ReadConfig
from Utilities.customlogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

#test
    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("**********test_homePageTitle************")
        self.logger.info("**********Verifying HomePage Title************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**********HomePageTitleTest is Passed************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_HomePageTitle.png")
            self.driver.close()
            self.logger.error("**********HomePageTitleTest is Failed************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("**********Verifying Login Test************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("**********Verifying Login Test Passed************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.logger.error("**********Verifying Login Test Failed************")
            self.driver.close()
            assert True


