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

    def test_01_AWS_loginIncorrectAccountIDError(self):
        """Tests error messages are present for incorrect Account ID when logging in.
        """

        print("\nChecks that incorrect Account ID for AWS login attempt displays error")
        driver = self.driver
        # url is pulled from confTest
        driver.get(self.aws_login_url)
        # triggering error
        funct.clearTextField(driver, var.loginAWS.aws_acctId)
        funct.waitAndSend(driver, var.loginAWS.aws_acctId, "TestAccountID")
        funct.waitAndSend(driver, var.loginAWS.aws_email, "notarealemail@rosedigital.co")
        funct.waitAndSend(driver, var.loginAWS.aws_password, "Test1234")
        funct.waitAndClick(driver, var.loginAWS.aws_signin_button)
        time.sleep(2)
        # checks if error message is present
        if funct.checkError(driver, var.loginAWS.aws_login_button_error) == True:
            print('PASS - ' + var.loginAWS.aws_login_button_error[2] + ' is present.')
        elif funct.checkError(driver, var.loginAWS.aws_login_button_error) == False:
            print('FAIL - ' + var.loginAWS.aws_login_button_error[2] + ' is missing')
            funct.fullshot(driver)
            raise Exception('Error warning element not found')
        # Checks correct error message
        warning = driver.find_element(var.loginAWS.aws_login_button_error[0], var.loginAWS.aws_login_button_error[1])
        if funct.checkErrorText(driver, var.loginAWS.aws_login_button_error, var.loginAWS.aws_badCredentials_errorstub) == True:
            print('PASS - Error warnings found and warning copy is correct')
            # print('Warning text displayed is "' + warning.get_attribute("innerText") + '"')
        elif funct.checkErrorText(driver, var.loginV.login_button_error, var.loginAWS.aws_badCredentials_errorstub) == False:
            print('FAIL - Warning should say "' + var.loginAWS.aws_badCredentials_errorstub + '" , but says "' + warning.get_attribute(
                        "innerText") + '"!')
            funct.fullshot(driver)
            raise Exception('Error warning(s) copy is incorrect')
        funct.closeWindow(driver, 'Sign in as IAM user')

    def test_02_AWS_loginIncorrectUserNameError(self):
        """Tests error messages are present for incorrect User Name when logging in.
        """

        print("\nChecks that incorrect User Name for AWS login attempt displays error")
        driver = self.driver
        # url is pulled from confTest
        driver.get(self.aws_login_url)
        # triggering error
        funct.clearTextField(driver, var.loginAWS.aws_acctId)
        funct.waitAndSend(driver, var.loginAWS.aws_acctId, "testsso")
        funct.waitAndSend(driver, var.loginAWS.aws_email, "fakeemail@rosedigital.co")
        funct.waitAndSend(driver, var.loginAWS.aws_password, "Test1234")
        funct.waitAndClick(driver, var.loginAWS.aws_signin_button)
        time.sleep(2)
        # checks if error message is present
        if funct.checkError(driver, var.loginAWS.aws_login_button_error) == True:
            print('PASS - ' + var.loginAWS.aws_login_button_error[2] + ' is present.')
        elif funct.checkError(driver, var.loginAWS.aws_login_button_error) == False:
            print('FAIL - ' + var.loginAWS.aws_login_button_error[2] + ' is missing')
            funct.fullshot(driver)
            raise Exception('Error warning element not found')
        # Checks correct error message
        warning = driver.find_element(var.loginAWS.aws_login_button_error[0], var.loginAWS.aws_login_button_error[1])
        if funct.checkErrorText(driver, var.loginAWS.aws_login_button_error, var.loginAWS.aws_badCredentials_errorstub) == True:
            print('PASS - Error warnings found and warning copy is correct')
        elif funct.checkErrorText(driver, var.loginV.login_button_error, var.loginAWS.aws_badCredentials_errorstub) == False:
            print('FAIL - Warning should say "' + var.loginAWS.aws_badCredentials_errorstub + '" , but says "' + warning.get_attribute(
                        "innerText") + '"!')
            funct.fullshot(driver)
            raise Exception('Error warning(s) copy is incorrect')
        funct.closeWindow(driver, 'Sign in as IAM user')

    def test_03_AWS_loginIncorrectPasswordError(self):
        """Tests error messages are present for incorrect Password when logging in.
        """

        print("\nChecks that incorrect Password for AWS login attempt displays error")
        driver = self.driver
        # url is pulled from confTest
        driver.get(self.aws_login_url)
        # triggering error
        funct.clearTextField(driver, var.loginAWS.aws_acctId)
        funct.waitAndSend(driver, var.loginAWS.aws_acctId, "TestAccountID")
        funct.waitAndSend(driver, var.loginAWS.aws_email, "notarealemail@rosedigital.co")
        funct.waitAndSend(driver, var.loginAWS.aws_password, "pwd$%^&$1234")
        funct.waitAndClick(driver, var.loginAWS.aws_signin_button)
        time.sleep(2)
        # checks if error message is present
        if funct.checkError(driver, var.loginAWS.aws_login_button_error) == True:
            print('PASS - ' + var.loginAWS.aws_login_button_error[2] + ' is present.')
        elif funct.checkError(driver, var.loginAWS.aws_login_button_error) == False:
            print('FAIL - ' + var.loginAWS.aws_login_button_error[2] + ' is missing')
            funct.fullshot(driver)
            raise Exception('Error warning element not found')
        # Checks correct error message
        warning = driver.find_element(var.loginAWS.aws_login_button_error[0], var.loginAWS.aws_login_button_error[1])
        if funct.checkErrorText(driver, var.loginAWS.aws_login_button_error, var.loginAWS.aws_badCredentials_errorstub) == True:
            print('PASS - Error warnings found and warning copy is correct')
        elif funct.checkErrorText(driver, var.loginV.login_button_error, var.loginAWS.aws_badCredentials_errorstub) == False:
            print('FAIL - Warning should say "' + var.loginAWS.aws_badCredentials_errorstub + '" , but says "' + warning.get_attribute(
                        "innerText") + '"!')
            funct.fullshot(driver)
            raise Exception('Error warning(s) copy is incorrect')
        funct.closeWindow(driver, 'Sign in as IAM user')

# use "report" variable in conftest.py to change report style on runner
if __name__ == "__main__":
    if confTest.NYlottoBASE.report == "terminal":
        unittest.main(warnings='ignore')
    elif confTest.NYlottoBASE.report == "html":
        unittest.main(warnings='ignore', testRunner=HtmlTestRunner.HTMLTestRunner(output='<html_report_dir>'))