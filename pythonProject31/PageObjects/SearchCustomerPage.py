class SearchCustomer:
    txtEmailID = "SearchEmail"
    txtFirstName = "SearchFirstName"
    txtLastName = "SearchLastName"
    btnSearchID = "search-customers"

    # SearchResults_xpath = /html/body/div[3]/div[1]/form[1]/section/div/div/div/div[2]/div
    SearchResults_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element_by_id(self.txtEmailID).clear()
        self.driver.find_element_by_id(self.txtEmailID).send_keys(email)

    def setFirstName(self, fname):
        self.driver.find_element_by_id(self.txtFirstName).clear()
        self.driver.find_element_by_id(self.txtFirstName).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element_by_id(self.txtLastName).clear()
        self.driver.find_element_by_id(self.txtLastName).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element_by_id(self.btnSearchID).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements_by_xpath(self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements_by_xpath(self.tableColumns_xpath))

    def getSearchCustomerByEmail(self, email):
        flag = False

        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            emailid = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[2]").text
            if emailid == email:
                flag = True
            break
        return flag

    def searchcustomerByName(self, Name):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            name = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[3]").text
            if name == Name:
                flag = True
            break
        return flag


