import time

import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.Readproperties import ReadConfig
from Utilities.customlogger import LogGen
from Utilities import XlUtils


class Test_002_Login_ddt:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/DDT.xlsx"

    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.logger.info("**********Test_002_Login_ddt************")
        self.logger.info("**********Verifying Login ddt Test************")
        self.driver = setup

        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)

        self.rows = XlUtils.getRowCount(self.path, 'Sheet1')
        print("No of rows in an xl:", self.rows)

        lst_status = []

        for r in range(2, self.rows + 1):

            self.username = XlUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XlUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XlUtils.readData(self.path, 'Sheet1', r, 3)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            # act_title = self.driver.title

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("****Passed****")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                    self.driver.close()

                elif self.exp == "Fail":
                    self.logger.info("****Failed****")
                    self.lp.clickLogout()
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("****Failed****")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("****Pass****")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("**********Login DDT test Passed************")
            self.driver.close()
            assert True
        else:
            self.logger.info("**********Login DDT test is failed************")
            self.driver.close()
            assert False
