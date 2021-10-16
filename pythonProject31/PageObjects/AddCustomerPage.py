import time

from selenium.webdriver.support.ui import Select


class AddCustomerPage:
    Customer_Menu_Link_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    # Customer_Menu_Link_xpath = "//a[@href='#']//span[contains(text(),'Customers')]"
    Customer_Sub_Link_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a"
    Add_New_Button = "/html/body/div[3]/div[1]/form[1]/div/div/a"
    Email_id = "Email"
    Pwd_id = "Password"
    FN_id = "FirstName"
    LN_id = "LastName"
    Gender_M_id = "Gender_Male"
    Gender_F_id = "Gender_Female"
    DoB_id = "DateOfBirth"
    Company_Name_id = "Company"
    Is_Tax_Exempt_Checkbox_id = "IsTaxExempt"

    # Newsletter_xpath = "//*[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div/div"
    CustomRoles_listbox_xpath = "//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div"
    CR_lst_Administrator_xpath = "//li[contains(text(), 'Administrators')]"
    CR_lst_Moderators_xpath = "//li[contains(text(), 'Forum Moderators')]"
    CR_lst_guest_xpath = "//li[contains(text(), 'Guests')]"
    CR_lst_Registered_xpath = "//li[contains(text(),'Registered')]"
    CR_lst_Vendors_xpath = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[11]/div[" \
                           "2]/select "
    ManageVendor_dropdown_id = "Vendor2"
    Active_checkbox_id = "Active"
    AdminComment_id = "AdminComment"
    Save_Button_xpath = "/html/body/div[3]/div[1]/form/div[1]/div/button[1]"

    # Create Constructor:
    def __init__(self, driver):
        self.driver = driver

    def ClickOnCustomerMenu(self):
        self.driver.find_element_by_xpath(self.Customer_Menu_Link_xpath).click()

    def ClickOnCustomerSubMenu(self):
        self.driver.find_element_by_xpath(self.Customer_Sub_Link_xpath).click()

    def ClickOnAddButton(self):
        self.driver.find_element_by_xpath(self.Add_New_Button).click()

    def Email(self, email):
        self.driver.find_element_by_id(self.Email_id).send_keys(email)

    def EnterPassword(self, password):
        self.driver.find_element_by_id(self.Pwd_id).send_keys(password)

    def EnterFirstName(self, firstname):
        self.driver.find_element_by_id(self.FN_id).send_keys(firstname)

    def EnterLastName(self, lastname):
        self.driver.find_element_by_id(self.LN_id).send_keys(lastname)

    def SelectGender(self, gender):
        if gender == 'Male':
            self.driver.find_element_by_id(self.Gender_M_id).click()
        elif gender == 'Female':
            self.driver.find_element_by_id(self.Gender_F_id).click()
        else:
            self.driver.find_element_by_id(self.Gender_M_id).click()

    def SelectDOB(self, dob):
        self.driver.find_element_by_id(self.DoB_id).send_keys(dob)

    def EnterCompanyName(self, cn):
        self.driver.find_element_by_id(self.Company_Name_id).send_keys(cn)

    time.sleep(3)

    def AdminComment(self, AC):
        self.driver.find_element_by_id(self.AdminComment_id).send_keys(AC)

    def ActiveCheckbox(self, Active):
        self.driver.find_element_by_id(self.Active_checkbox_id).send_keys(Active)
        time.sleep(3)

    # def EnterNewsLetter(self, news):
    # self.driver.find_element_by_xpath(self.Newsletter_xpath).send_keys(news)

    def SelectTaxID(self, TaxId):
        self.driver.find_element_by_id(self.Is_Tax_Exempt_Checkbox_id).send_keys(TaxId)

    def setCustomerRoles(self, role):
        self.driver.find_element_by_xpath(self.CustomRoles_listbox_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.CR_lst_Registered_xpath)

        elif role == 'Administrators':
            self.listitem = self.driver.find_element_by_xpath(self.CR_lst_Administrator_xpath)

        elif role == 'Guests':
            time.sleep(3)
            self.listitem = self.driver.find_element_by_xpath(self.CR_lst_guest_xpath).click()
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            time.sleep(3)


        # elif role == 'Registered':
        # self.listitem = self.driver.find_element_by_xpath(self.CR_lst_Registered_xpath)

        elif role == 'Moderator':
            self.listitem = self.driver.find_element_by_xpath(self.CR_lst_Moderators_xpath)

        elif role == 'Vendors':
            self.listitem = self.driver.find_element_by_xpath(self.CR_lst_Vendors_xpath)

        else:
            self.listitem = self.driver.find_element_by_xpath(self.CR_lst_guest_xpath)
            time.sleep(3)
            # self.listitem.click()
            self.driver.execute_script("arguments[0].click();", self.listitem)

    def ManageVendor(self, value):

        element = self.driver.find_element_by_xpath(self.CR_lst_Vendors_xpath)
        drp = Select(element)
        drp.select_by_visible_text(value)

    def SaveButton(self):
        self.driver.find_element_by_xpath(self.Save_Button_xpath).click()
