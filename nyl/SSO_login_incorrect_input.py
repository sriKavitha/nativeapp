# [Documentation - Setup] This section lists all dependencies
# that are imported for this test file to work
from selenium import webdriver  #webdriver module provides all WebDriver implementations
import warnings
import unittest, time, re       #unittest is the testing framework, provides module for organizing test cases
from selenium.webdriver.common.keys import Keys     #Keys class provide keys in the keyboard like RETURN, F1, ALT, etc.
from selenium.webdriver.common.by import By         #By class provides method for finding the page elements by NAME, ID, XPATH, etc.
from selenium.webdriver.support.ui import Select    #Select class provides ability to select items in dropdown
import var, funct, util, confTest, HtmlTestRunner   #Custom class for NYL

class NYlotto(confTest.NYlottoBASE):

    def test_01_loginIncorrectEmailError(self):
        """Tests error messages are present for incorrect email when logging in.

        Jira test ticket - https://rosedigital.atlassian.net/browse/NYL-2930

        :return:
        """

        testenv = self.env
        print("\nTESTING " + testenv + " ENVIRONMENT")
        print("\nChecks that incorrect email login attempt displays error")
        driver = self.driver
        # url is pulled from confTest
        driver.get(self.login_url)
        # triggering error
        funct.waitAndSend(driver, var.loginV.email, "notarealemail@rosedigital.co")
        funct.waitAndSend(driver, var.loginV.password, "Test1234")
        funct.waitAndClick(driver, var.loginV.login_button)
        time.sleep(10)
        # checks if error message is present
        if funct.checkError(driver, var.loginV.login_button_error) == True:
            print('PASS - ' + var.loginV.login_button_error[2] + ' is present.')
        elif funct.checkError(driver, var.loginV.login_button_error) == False:
            print('FAIL - ' + var.loginV.login_button_error[2] + ' is missing')
            funct.fullshot(driver)
            raise Exception('Error warning element not found')
        # Checks correct error message
        warning = driver.find_element(var.loginV.login_button_error[0], var.loginV.login_button_error[1])
        if funct.checkErrorText(driver, var.loginV.login_button_error, var.loginV.badEmailErrorStub) == True:
            print('PASS - Error warnings found and warning copy is correct')
            # print('Warning text displayed is "' + warning.get_attribute("innerText") + '"')
        elif funct.checkErrorText(driver, var.loginV.login_button_error, var.loginV.badEmailErrorStub) == False:
            print('FAIL - Warning should say "' + var.loginV.badEmailErrorStub + '" , but says "' + warning.get_attribute("innerText") + '"!')
            funct.fullshot(driver)
            raise Exception('Error warning(s) copy is incorrect')
        funct.closeWindow(driver, 'New York Lottery - Admin Dashboard')


    def test_02_loginIncorrectPswError(self):
        """Tests error messages are present for incorrect password when logging in.

        Jira test ticket - https://rosedigital.atlassian.net/browse/NYL-2549

        Creates a verified user, navigates to login page and submits incorrect password.
        :return:
        """

        print("\nChecks that incorrect password login attempt displays error")
        testemail = self.testemail
        driver = self.driver
        print('\n----------\n' + 'Test setup')
        # creates a verified user with valid SSN4
        funct.createVerifiedUser(self, testemail)
        print('----------')
        # switch to login page
        driver.get(self.login_url)
        # triggering error
        funct.waitAndSend(driver, var.loginV.email, testemail)
        funct.waitAndSend(driver, var.loginV.password, "badpassword")
        funct.waitAndClick(driver, var.loginV.login_button)
        time.sleep(7)
        # checks if error message is present
        if funct.checkError(driver, var.loginV.login_button_error) == True:
            print('PASS - ' + var.loginV.login_button_error[2] + ' is present')
        elif funct.checkError(driver, var.loginV.login_button_error) == False:
            print('FAIL - ' + var.loginV.login_button_error[2] + ' is missing')
            funct.fullshot(driver)
            raise Exception('Error warning element not found')
        # checks if error text matches recorded copy
        warning = driver.find_element(var.loginV.login_button_error[0], var.loginV.login_button_error[1])
        if funct.checkErrorText(driver, var.loginV.login_button_error, var.loginV.badPasswordErrorStub) == True:
            print('PASS - Error warnings found and warning copy is correct')
        elif funct.checkErrorText(driver, var.loginV.login_button_error, var.loginV.badPasswordErrorStub) == False:
            print('FAIL - Warning should say "' + var.loginV.badPasswordErrorStub + '" , but says "' + warning.get_attribute("innerText") + '"!')
            funct.fullshot(driver)
            raise Exception('Error warning(s) copy is incorrect')
        # Deleting test data
        print('\n----------\n' + 'Test complete!\n\nTest clean up commencing')
        try:
            funct.purgeSSOemail(self, testemail)
        except:
            pass
        funct.closeWindow(driver, 'New York Lottery - Admin Dashboard')
        print('----------')

# use "report" variable in conftest.py to change report style on runner
if __name__ == "__main__":
    if confTest.NYlottoBASE.report == "terminal":
        unittest.main(warnings='ignore')
    elif confTest.NYlottoBASE.report == "html":
        unittest.main(warnings='ignore', testRunner=HtmlTestRunner.HTMLTestRunner(output='<html_report_dir>'))