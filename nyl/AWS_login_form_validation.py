import unittest, time, re       #unittest is the testing framework, provides module for organizing test cases
import var, funct, util, confTest, HtmlTestRunner   #Custom class for NYL

class NYlotto(confTest.NYlottoBASE):
    """
    Checks that the AWS login page has expected error messages with invalid data submission
    """
    def test_01_aws_loginError(self):
        """Checks main error appears when empty AWS form is submitted and text copy is correct
        :return:
        """
        print("\nChecks main error appears when empty AWS form is submitted and text copy is correct")
        driver = self.driver
        # url is pulled from confTest
        driver.get(self.aws_login_url)
        # triggering error
        # clear the account ID before Sign In button is clicked... The account ID is auto-filled with "nyl-sso"
        funct.clearTextField(driver, var.loginAWS.aws_acctId)
        funct.waitAndClick(driver, var.loginAWS.aws_signin_button)
        if funct.checkError(driver, var.loginAWS.aws_signin_button) == True:
            print('PASS - ' + var.loginAWS.aws_acctId[2] + ' is present')
            print('PASS - ' + var.loginAWS.aws_email[2] + ' is present')
            print('PASS - ' + var.loginAWS.aws_password[2] + ' is present')
        elif funct.checkError(driver, var.loginV.login_button_error) == False:
            print('FAIL - ' + var.loginAWS.aws_login_button_error[2] + ' is missing')
            funct.fullshot(driver)
            raise Exception('Error warning element not found')
        warning = driver.find_element(var.loginAWS.aws_login_button_error[0], var.loginAWS.aws_login_button_error[1])
        if funct.checkErrorText(driver, var.loginAWS.aws_account_Id_error, var.loginAWS.aws_account_Id_errorstub) == True:
            print('PASS - Warning copy is correct')
        elif funct.checkErrorText(driver, var.loginAWS.aws_account_Id_error, var.loginAWS.aws_account_Id_errorstub) == False:
            print('FAIL - Warning should say "' + var.loginAWS.aws_account_Id_error + '" , but says "' + warning.get_attribute("innerText") + '"')
        if funct.checkErrorText(driver, var.loginAWS.aws_email_error, var.loginAWS.aws_email_errorstub) == True:
                print('PASS - Warning copy is correct')
        elif funct.checkErrorText(driver, var.loginAWS.aws_email_error, var.loginAWS.aws_email_errorstub) == False:
                print('FAIL - Warning should say "' + var.loginAWS.aws_email_error + '" , but says "' + warning.get_attribute("innerText") + '"')
        if funct.checkErrorText(driver, var.loginAWS.aws_password_error, var.loginAWS.aws_password_errorstub) == True:
                print('PASS - Warning copy is correct')
        elif funct.checkErrorText(driver, var.loginAWS.aws_password_error, var.loginAWS.aws_password_errorstub) == False:
                print('FAIL - Warning should say "' + var.loginAWS.aws_password_error + '" , but says "' + warning.get_attribute("innerText") + '"')
                funct.fullshot(driver)
                raise Exception('Error copy is incorrect')
        print('----------')
        funct.closeWindow(driver, 'Sign in as IAM user')
    def test_02_aws_loginRequiredErrors(self):
        """Checks mandatory field errors are found and text copy is correct
        :return:
        """
        print("\nChecks mandatory field errors are found and text copy is correct")
        driver = self.driver
        # url is pulled from confTest
        driver.get(self.aws_login_url)
        # triggering error
        funct.clearTextField(driver, var.loginAWS.aws_acctId)
        funct.waitAndClick(driver, var.loginAWS.aws_acctId)
        funct.waitAndClick(driver, var.loginAWS.aws_email)
        funct.waitAndClick(driver, var.loginAWS.aws_password)
        funct.waitAndClick(driver, var.loginAWS.aws_signin_button)
        warningList = []
        # These are the CSS selectors for the 3 red text error elements
        warningsExpected = driver.find_elements_by_xpath('//div[@class="textinput error"]')
        for warning in warningsExpected:
            if warning.get_attribute("innertext"):
                warningList.append(warning[2])
        if len(warningList) <= 0:
            print('PASS - Error warnings present')
        elif len(warningList) > 0:
            print('FAIL - ')
            print(warningList)
            print(' Error warning(s) missing')
            funct.fullshot(driver)
            raise Exception('Error warning element not found')
        if len(warningList) <= 0:
            print('PASS - Error warnings copy is correct')
        elif len(warningList) > 0:
            print('E -- ')
            print(warningList)
            print('Error warning(s) copy is incorrect')
            funct.fullshot(driver)
            raise Exception('Error warning(s) copy is incorrect')
        print('----------')
        funct.closeWindow(driver, 'Sign in as IAM user')

    def test_03_aws_loginIncompleteAccountIDError(self):
        """Checks missing account ID for AWS login attempt error and text copy is correct
        :return:
        """
        print("\nChecks missing account ID login attempt error and text copy is correct")
        driver = self.driver
        # url is pulled from confTest
        driver.get(self.aws_login_url)
        # triggering error
        funct.clearTextField(driver, var.loginAWS.aws_acctId)
        funct.waitAndSend(driver, var.loginAWS.aws_email, "testemail@rose.com")
        funct.waitAndSend(driver, var.loginAWS.aws_password, "test1234")
        funct.waitAndClick(driver, var.loginAWS.aws_signin_button)
        if funct.checkError(driver, var.loginAWS.aws_login_button_error) == True:
            print('PASS - ' + var.loginAWS.aws_email[2] + ' is present')
            print('PASS - ' + var.loginAWS.aws_password[2] + ' is present')
            print('PASS - ' + var.loginAWS.aws_signin_button[2] + ' is present')
        elif funct.checkError(driver, var.loginAWS.aws_login_button_error) == False:
            print('FAIL - ' + var.loginAWS.aws_login_button_error[2] + ' is missing')
            funct.fullshot(driver)
            raise Exception('Error warning element not found')

        warning = driver.find_element(var.loginAWS.aws_account_Id_error[0], var.loginAWS.aws_account_Id_error[1])
        if funct.checkErrorText(driver, var.loginAWS.aws_account_Id_error, var.loginAWS.aws_account_Id_errorstub) == True:
            print('PASS - Warning copy text is correct')
        elif funct.checkErrorText(driver, var.loginAWS.aws_account_Id_error, var.loginAWS.aws_account_Id_errorstub) == False:
            print('FAIL - Warning should say " ' + var.loginAWS.aws_account_Id_errorstub + ' , but says "' + warning.get_attribute("innerText") + '"')
            funct.fullshot(driver)
            raise Exception('Error copy is incorrect')
        print('----------')
        funct.closeWindow(driver, 'Sign in as IAM user')

    def test_04_aws_loginIncompleteUserNameError(self):
        """Checks missing User Name/Email for AWS login attempt error and text copy is correct
        :return:
        """
        print("\nChecks missing User Name/Email login attempt error and text copy is correct")
        driver = self.driver
        # url is pulled from confTest
        driver.get(self.aws_login_url)
        # triggering error
        funct.clearTextField(driver, var.loginAWS.aws_acctId)
        funct.waitAndSend(driver, var.loginAWS.aws_acctId, "sso")
        funct.waitAndSend(driver, var.loginAWS.aws_password, "test1234")
        funct.waitAndClick(driver, var.loginAWS.aws_signin_button)
        if funct.checkError(driver, var.loginAWS.aws_login_button_error) == True:
            print('PASS - ' + var.loginAWS.aws_acctId[2] + ' is present')
            print('PASS - ' + var.loginAWS.aws_password[2] + ' is present')
            print('PASS - ' + var.loginAWS.aws_signin_button[2] + ' is present')
        elif funct.checkError(driver, var.loginAWS.aws_login_button_error) == False:
            print('FAIL - ' + var.loginAWS.aws_login_button_error[2] + ' is missing')
            funct.fullshot(driver)
            raise Exception('Error warning element not found')

        warning = driver.find_element(var.loginAWS.aws_email_error[0], var.loginAWS.aws_email_error[1])
        if funct.checkErrorText(driver, var.loginAWS.aws_email_error, var.loginAWS.aws_email_errorstub) == True:
            print('PASS - Warning copy text is correct')
        elif funct.checkErrorText(driver, var.loginAWS.aws_email_error, var.loginAWS.aws_email_errorstub) == False:
            print('FAIL - Warning should say " ' + var.loginAWS.aws_email_errorstub + ' , but says "' + warning.get_attribute("innerText") + '"')
            funct.fullshot(driver)
            raise Exception('Error copy is incorrect')
        print('----------')
        funct.closeWindow(driver, 'Sign in as IAM user')

    def test_05_aws_loginIncompletePasswordError(self):
        """Checks missing Password for AWS login attempt error and text copy is correct
        :return:
        """
        print("\nChecks missing Password login attempt error and text copy is correct")
        driver = self.driver
        # url is pulled from confTest
        driver.get(self.aws_login_url)
        # triggering error
        funct.clearTextField(driver, var.loginAWS.aws_acctId)
        funct.waitAndSend(driver, var.loginAWS.aws_acctId, "sso")
        funct.waitAndSend(driver, var.loginAWS.aws_email, "test1234")
        funct.waitAndClick(driver, var.loginAWS.aws_signin_button)
        if funct.checkError(driver, var.loginAWS.aws_login_button_error) == True:
            print('PASS - ' + var.loginAWS.aws_acctId[2] + ' is present')
            print('PASS - ' + var.loginAWS.aws_email[2] + ' is present')
            print('PASS - ' + var.loginAWS.aws_signin_button[2] + ' is present')
        elif funct.checkError(driver, var.loginAWS.aws_login_button_error) == False:
            print('FAIL - ' + var.loginAWS.aws_login_button_error[2] + ' is missing')
            funct.fullshot(driver)
            raise Exception('Error warning element not found')

        warning = driver.find_element(var.loginAWS.aws_password_error[0], var.loginAWS.aws_password_error[1])
        if funct.checkErrorText(driver, var.loginAWS.aws_password_error, var.loginAWS.aws_password_errorstub) == True:
            print('PASS - Warning copy text is correct')
        elif funct.checkErrorText(driver, var.loginAWS.aws_password_error, var.loginAWS.aws_password_errorstub) == False:
            print('FAIL - Warning should say " ' + var.loginAWS.aws_password_errorstub + ' , but says "' + warning.get_attribute("innerText") + '"')
            funct.fullshot(driver)
            raise Exception('Error copy is incorrect')
        print('----------')
        funct.closeWindow(driver, 'Sign in as IAM user')

# use "report" variable in conftest.py to change report style on runner
if __name__ == "__main__":
    if confTest.NYlottoBASE.report == "terminal":
        unittest.main(warnings='ignore')
    elif confTest.NYlottoBASE.report == "html":
        unittest.main(warnings='ignore', testRunner=HtmlTestRunner.HTMLTestRunner(output='<html_report_dir>'))