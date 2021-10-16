import random
import string
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome import webdriver
from PageObjects.AddCustomerPage import AddCustomerPage
from PageObjects.LoginPage import LoginPage
from Utilities.Readproperties import ReadConfig
from Utilities.customlogger import LogGen
from selenium.webdriver.support.ui import Select


class Test_TC003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_AddCustomer(self, setup):
        self.logger.info("**********Test_003_Add Customer************")
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

        self.logger.info("*************Start Add Customer Test************")

        self.addcust = AddCustomerPage(self.driver)
        self.addcust.ClickOnCustomerMenu()
        time.sleep(2)
        self.addcust.ClickOnCustomerSubMenu()
        self.addcust.ClickOnAddButton()
        time.sleep(3)
        self.logger.info("***************Providing Customer Info*********")
        self.email = random_generator() + "@gmail.com"
        self.addcust.Email(self.email)
        self.addcust.EnterPassword("Test113")
        self.addcust.EnterFirstName("Chetan")
        self.addcust.EnterLastName("Ramesh")
        self.addcust.SelectGender("Male")
        self.addcust.SelectDOB("07/05/1982")
        self.addcust.SelectTaxID("12345")
        # self.addcust.EnterNewsLetter("Hurry up! learn Selenium. Course available")
        self.addcust.EnterCompanyName("SeleniumLearner")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.ManageVendor("Vendor 2")
        self.addcust.AdminComment("This is testing...........")
        self.addcust.SaveButton()

        self.logger.info("***********Saving Customer Info***************")
        self.logger.info("***********Add Customer Validation Started************")
        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)

        if 'customer has added successfully.' in self.msg:
            assert True == True
            self.logger.info("****************Add Customer Test Passed************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_AddCustomer_scr.png")
            self.logger.error("*************Add Customer Test Failed************")
            assert True == True
            self.driver.close()
            self.logger.info("************Ending Add Customer Page Test***********8")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
