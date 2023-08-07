import unittest, time, re       #unittest is the testing framework, provides module for organizing test cases
import var, funct, util, confTest, HtmlTestRunner   #Custom class for NYL

class NYlotto(confTest.NYlottoBASE):
    """
    Checks that the login page has expected error messages wtih invalid data submission
    """
    def test_01_loginError(self):
        """Checks main error appears when empty form is submitted and text copy is correct
        :return:
        """
        testenv = self.env
        print("\nTESTING " + testenv + " ENVIRONMENT")
        print("\nChecks main error appears when empty form is submitted and text copy is correct")
        driver = self.driver
        # url is pulled from confTest
        driver.get(self.login_url)
        # triggering error
        funct.waitAndClick(driver, var.loginV.login_button)
        if funct.checkError(driver, var.loginV.login_button_error) == True:
            print('PASS - ' + var.loginV.login_button_error[2] + ' is present')
        elif funct.checkError(driver, var.loginV.login_button_error) == False:
            print('FAIL - ' + var.loginV.login_button_error[2] + ' is missing')
            funct.fullshot(driver)
            raise Exception('Error warning element not found')
        warning = driver.find_element(var.loginV.login_button_error[0], var.loginV.login_button_error[1])
        if funct.checkErrorText(driver, var.loginV.login_button_error, var.loginV.loginErrorStub) == True:
            print('PASS - Warning copy is correct')
        elif funct.checkErrorText(driver, var.loginV.login_button_error, var.loginV.loginErrorStub) == False:
            print('FAIL - Warning should say "' + var.loginV.loginErrorStub + '" , but says "' + warning.get_attribute("innerText") + '"')
            funct.fullshot(driver)
            raise Exception('Error copy is incorrect')
        print('----------')
        funct.closeWindow(driver, 'New York Lottery - Single Sign On')

    def test_02_loginRequiredErrors(self):
        """Checks mandatory field errors are found and text copy is correct
        :return:
        """
        print("\nChecks mandatory field errors are found and text copy is correct")
        driver = self.driver
        # url is pulled from confTest
        driver.get(self.login_url)
        # triggering error
        funct.waitAndClick(driver, var.loginV.email)
        funct.waitAndClick(driver, var.loginV.password)
        funct.waitAndClick(driver, var.loginV.login_button)
        warningList = []
        # These are the CSS selectors for the 2 red text error elements
        warningsExpected = [var.loginV.email_error, var.loginV.password_error]
        for warning in warningsExpected:
            if funct.checkError(driver, warning) == False:
                warningList.append(warning[2])
        if len(warningList) <= 0:
            print('PASS - Error warnings present')
        elif len(warningList) > 0:
            print('FAIL - ')
            print(warningList)
            print(' Error warning(s) missing')
            funct.fullshot(driver)
            raise Exception('Error warning element not found')
        warningsExpected = [var.loginV.email_error, var.loginV.password_error]
        for warning in warningsExpected:
            if funct.checkErrorText(driver, warning, var.loginV.requiredErrorStub) == False:
                warningList.append(warning[2])
        if len(warningList) <= 0:
            print('PASS - Error warnings copy is correct')
        elif len(warningList) > 0:
            print('FAIL - ')
            print(warningList)
            print('Error warning(s) copy is incorrect')
            funct.fullshot(driver)
            raise Exception('Error warning(s) copy is incorrect')
        print('----------')
        funct.closeWindow(driver, 'New York Lottery - Single Sign On')

    def test_03_loginIncompleteEmailError(self):
        """Checks missing email login attempt error and text copy is correct
        :return:
        """
        print("\nChecks missing email login attempt error and text copy is correct")
        driver = self.driver
        # url is pulled from confTest
        driver.get(self.login_url)
        # triggering error
        funct.waitAndSend(driver, var.loginV.password, "valid1234")
        funct.waitAndClick(driver, var.loginV.login_button)
        if funct.checkError(driver, var.loginV.login_button_error) == True:
            print('PASS - ' + var.loginV.login_button_error[2] + ' is present')
        elif funct.checkError(driver, var.loginV.login_button_error) == False:
            print('FAIL - ' + var.loginV.login_button_error[2] + ' is missing')
            funct.fullshot(driver)
            raise Exception('Error warning element not found')

        warning = driver.find_element(var.loginV.login_button_error[0], var.loginV.login_button_error[1])
        if funct.checkErrorText(driver, var.loginV.login_button_error, var.loginV.loginErrorStub) == True:
            print('PASS - Warning copy text is correct')
        elif funct.checkErrorText(driver, var.loginV.login_button_error, var.loginV.loginErrorStub) == False:
            print('FAIL - Warning should say " ' + var.loginV.loginErrorStub + ' , but says "' + warning.get_attribute("innerText") + '"')
            funct.fullshot(driver)
            raise Exception('Error copy is incorrect')
        print('----------')
        funct.closeWindow(driver, 'New York Lottery - Single Sign On')

    def test_04_loginIncompletePswError(self):
        """Checks missing password login attempt error and text copy is correct
        :return:
        """
        print("\nChecks missing password login attempt error and text copy is correct")
        testemail = self.testemail
        driver = self.driver
        # url is pulled from confTest
        driver.get(self.login_url)
        # triggering error
        funct.waitAndSend(driver, var.loginV.email, testemail)
        funct.waitAndClick(driver, var.loginV.login_button)
        if funct.checkError(driver, var.loginV.login_button_error) == True:
            print('PASS - ' + var.loginV.login_button_error[2] + ' is present')
        elif funct.checkError(driver, var.loginV.login_button_error) == False:
            print('FAIL - ' + var.loginV.login_button_error[2] + ' is missing')
            funct.fullshot(driver)
            raise Exception('Error warning element not found')

        warning = driver.find_element(var.loginV.login_button_error[0], var.loginV.login_button_error[1])
        if funct.checkErrorText(driver, var.loginV.login_button_error, var.loginV.loginErrorStub) == True:
            print('PASS - Warning copy is correct')
        elif funct.checkErrorText(driver, var.loginV.login_button_error, var.loginV.loginErrorStub) == False:
            print('FAIL - Warning should say " ' + var.loginV.loginErrorStub + ' , but says "' + warning.get_attribute("innerText") + '"')
            funct.fullshot(driver)
            raise Exception('Error copy is incorrect')
        print('----------')
        funct.closeWindow(driver, 'New York Lottery - Single Sign On')

    def test_05_loginInvalidEmailError(self):
        """Checks invalid email input error and text copy is correct
        :return:
        """
        print("\nChecks that invalid email input displays error and text copy is correct")
        driver = self.driver
        # url is pulled from confTest
        driver.get(self.login_url)
        # triggering error
        funct.waitAndSend(driver, var.loginV.email, "bademail$$$%%%rosedigital")
        funct.waitAndClick(driver, var.loginV.login_button)
        if funct.checkError(driver, var.loginV.email_error) == True:
            print('PASS - ' + var.loginV.email_error[2] + ' is present')
        elif funct.checkError(driver, var.loginV.email_error) == False:
            print('FAIL - "' + var.loginV.email_error[2] + ' is missing')
            funct.fullshot(driver)
            raise Exception('Error warning element not found')
        warning = driver.find_element(var.loginV.email_error[0], var.loginV.email_error[1])
        if funct.checkErrorText(driver, var.loginV.email_error, var.loginV.emailErrorStub) == True:
            print('PASS - Error warnings copy is correct')
        elif funct.checkErrorText(driver, var.loginV.email_error, var.loginV.emailErrorStub) == False:
            print('FAIL - Warning should say "' + var.loginV.emailErrorStub + ' , but says "' + warning.get_attribute("innerText") + '"')
            funct.fullshot(driver)
            raise Exception('Error warning(s) copy is incorrect')
        print('----------')
        funct.closeWindow(driver, 'New York Lottery - Single Sign On')


# use "report" variable in conftest.py to change report style on runner
if __name__ == "__main__":
    if confTest.NYlottoBASE.report == "terminal":
        unittest.main(warnings='ignore')
    elif confTest.NYlottoBASE.report == "html":
        unittest.main(warnings='ignore', testRunner=HtmlTestRunner.HTMLTestRunner(output='<html_report_dir>'))