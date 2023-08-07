import unittest, time, re       #unittest is the testing framework, provides module for organizing test cases
from selenium.webdriver.common.keys import Keys     #Keys class provide keys in the keyboard like RETURN, F1, ALT, etc.
import var, funct, util, confTest, HtmlTestRunner   #Custom class for NYL

class NYlotto(confTest.NYlottoBASE):
    """
    Checks that the registration page has expected error messages wtih invalid data submission
    """

    def test_01_regSubmitError(self):
        """Checks main error is present when empty form is submitted
        :return:
        """
        testenv = self.env
        print("TESTING " + testenv + " ENVIRONMENT")
        print("\nChecks main error appears when empty form is submitted")
        driver = self.driver
        # url is pulled from confTest
        driver.get(self.reg_url)
        # triggering error
        funct.waitAndClick(driver, var.regV.submit_button)
        if funct.checkError(driver, var.regV.submit_button_error) == True:
            print("PASS - " + var.regV.submit_button_error[2] + " is present.")
        elif funct.checkError(driver, var.regV.submit_button_error) == False:
            print("FAIL - " + var.regV.submit_button_error[2] + " is missing")
            funct.fullshot(driver)
            raise Exception('Error warning element not found.')
        funct.closeWindow(driver, 'New York Lottery - Single Sign On')
        print('----------')

    def test_02_regSubmitErrorCopy(self):
        """Checks main error copy is correct when empty form is submitted
        :return:
        """
        print("\nChecks main error copy")
        driver = self.driver
        # url is pulled from confTest
        driver.get(self.reg_url)
        # triggering error
        funct.waitAndClick(driver, var.regV.submit_button)
        warning = driver.find_element(var.regV.submit_button_error[0], var.regV.submit_button_error[1])
        if funct.checkErrorText(driver, var.regV.submit_button_error, var.regV.submitErrorStub) == True:
            print("PASS - Warning copy text is correct.")
        elif funct.checkErrorText(driver, var.regV.submit_button_error, var.regV.submitErrorStub) == False:
            print("FAIL - Warning should say " + var.regV.submitErrorStub + " , but says " + warning.get_attribute("innerText") + "!")
            funct.fullshot(driver)
            raise Exception('Error copy is incorrect.')
        funct.closeWindow(driver, 'New York Lottery - Single Sign On')
        print('----------')

    def test_03_regRequiredErrors(self):
        """Checks error when mandatory fields are left empty
        :return:
        """
        print("\nChecks mandatory field errors are found")
        driver = self.driver
        # url is pulled from confTest
        driver.get(self.reg_url)
        # triggering error
        funct.waitAndClick(driver, var.regV.submit_button)
        warningList = []
        # These are the CSS selectors for the 12 red text error elements
        warningsExpected = [
             var.regV.fname_error, var.regV.lname_error, var.regV.housenum_error,
             var.regV.street_error, var.regV.city_error, var.regV.state_dropdown_error,
             var.regV.zip_error, var.regV.phone_error, var.regV.dob_error,
             var.regV.email_error, var.regV.password_error, var.regV.confirmPsw_error]
        for warning in warningsExpected:
            if funct.checkError(driver, warning) == False:
                warningList.append(warning[2])
        if len(warningList) <= 0:
            print("PASS - Error warnings found and present.")
        elif len(warningList) > 0:
            print("FAIL - ")
            print(warningList)
            print("Error warning(s) missing")
            funct.fullshot(driver)
            raise Exception("Error warning element not found.")
        funct.closeWindow(driver, 'New York Lottery - Single Sign On')
        print('----------')

    def test_04_regRequiredErrorsCopy(self):
        """Checks text copy is correct when mandatory fields are left empty
        :return:
        """
        print("\nChecks mandatory field error copy")
        driver = self.driver
        # url is pulled from confTest
        driver.get(self.reg_url)
        # triggering error
        funct.waitAndClick(driver, var.regV.submit_button)
        warningList = []
        # These are the CSS selectors for the 12 red text error elements
        warningsExpected = [
             var.regV.fname_error, var.regV.lname_error, var.regV.housenum_error,
             var.regV.street_error, var.regV.city_error, var.regV.state_dropdown_error,
             var.regV.zip_error, var.regV.phone_error, var.regV.dob_error,
             var.regV.email_error, var.regV.password_error, var.regV.confirmPsw_error]
        for warning in warningsExpected:
            if funct.checkErrorText(driver, warning, var.regV.requiredErrorStub) == False:
                warningList.append(warning[2])
        if len(warningList) <= 0:
            print("PASS - Error warnings found and copy is correct.")
        elif len(warningList) > 0:
            print("FAIL - ")
            print(warningList)
            print("Error warning(s) copy is incorrect.")
            funct.fullshot(driver)
            raise Exception("Error warning(s) copy is incorrect.")
        funct.closeWindow(driver, 'New York Lottery - Single Sign On')
        print('----------')

    def test_05_regUnacceptedLetterErrors(self):
        """Checks invalid letter input error and text copy is correct
        :return:
        """
        print("\nChecks that certain fields do not take letters")
        driver = self.driver
        # url is pulled from confTest
        driver.get(self.reg_url)
        # grabbing every text field and inputting letters into it, triggering error
        textFields = driver.find_elements_by_class_name("form-control")
        valueInputted = "asd"
        valueExpected = ""
        for field in textFields:
            field.send_keys(valueInputted)
        warningList = []
        # These are the fields that do not take letters and will have error elements
        warningsExpected = [
            var.regV.zip, var.regV.phone, var.regV.ssn4, var.regV.dob]
        for warning in warningsExpected:
            if funct.checkValue(driver, warning, valueExpected) == False:
                warningList.append(warning[2])
        if len(warningList) <= 0:
            print("PASS - invalid values '" + valueInputted + "' not accepted in appropriate fields")
        elif len(warningList) > 0:
            print("FAIL - invalid values '" + valueInputted + "' are allowed in")
            print(warningList)
            print(" fields.")
            funct.fullshot(driver)
            raise Exception("Invalid values allowed in fields.")
        funct.closeWindow(driver, 'New York Lottery - Single Sign On')
        print('----------')

    def test_06_regUnacceptedSymbolsErrors(self):
        """Checks invalid symbols input error and text copy is correct
        :return:
        """
        print("\nChecks that certain fields do not take symbols")
        driver = self.driver
        # url is pulled from confTest
        driver.get(self.reg_url)
        # grabbing every text field and inputting symbols into it, triggering error
        textFields = driver.find_elements_by_class_name("form-control")
        valueInputted = "!@#"
        valueExpected = ""
        for field in textFields:
            field.send_keys(Keys.SHIFT + "1" + "2" + "3")
        warningList = []
        # These are the fields that do not take letters and will have error elements
        warningsExpected = [
            var.regV.fname, var.regV.mname, var.regV.lname,
            var.regV.zip, var.regV.phone, var.regV.ssn4, var.regV.dob]
        for warning in warningsExpected:
            if funct.checkValue(driver, warning, valueExpected) == False:
                warningList.append(warning[2])
        if len(warningList) <= 0:
            print("PASS - invalid values '" + valueInputted + "' not accepted in appropriate fields")
        elif len(warningList) > 0:
            print("FAIL - invalid values '" + valueInputted + "' are allowed in")
            print(warningList)
            print(" fields.")
            funct.fullshot(driver)
            raise Exception("Invalid values allowed in fields.")
        funct.closeWindow(driver, 'New York Lottery - Single Sign On')
        print('----------')

    def test_07_regUnacceptedNumbersErrors(self):
        """Checks invalid number input error and text copy is correct
        :return:
        """
        print("\nChecks that certain fields do not take numbers")
        driver = self.driver
        # url is pulled from confTest
        driver.get(self.reg_url)
        # grabbing every text field and inputting numbers into it, triggering error
        textFields = driver.find_elements_by_class_name("form-control")
        valueInputted = "123"
        valueExpected = ""
        for field in textFields:
            field.send_keys("123")
        warningList = []
        # These are the fields that do not take letters and will have error elements
        warningsExpected = [
            var.regV.fname, var.regV.mname, var.regV.lname]
        for warning in warningsExpected:
            if funct.checkValue(driver, warning, valueExpected) == False:
                warningList.append(warning[2])
        if len(warningList) <= 0:
            print("PASS - invalid values '" + valueInputted + "' not accepted in appropriate fields")
        elif len(warningList) > 0:
            print("FAIL - invalid values '" + valueInputted + "' are allowed in")
            print(warningList)
            print(" fields.")
            funct.fullshot(driver)
            raise Exception("Invalid values allowed in fields.")
        funct.closeWindow(driver, 'New York Lottery - Single Sign On')
        print('----------')

    def test_08_regInvalidFormatZipcode(self):
        """Checks invalid zipcode input error and text copy is correct
        :return:
        """
        print("\nChecks for appearance of error messages when inputting invalid data in zip code field")
        driver = self.driver
        # url is pulled from confTest
        driver.get(self.reg_url)
        # triggering error
        funct.waitAndSend(driver, var.regV.zip, "123")
        funct.waitAndSend(driver, var.regV.zip, Keys.TAB)
        if funct.checkErrorText(driver, var.regV.zip_error, var.regV.zipErrorStub) == True:
            print("PASS - " + var.regV.zip_error[2] + " is present and copy correctly reads as '" + var.regV.zipErrorStub + "'")
        elif funct.checkErrorText(driver, var.regV.zip_error, var.regV.zipErrorStub) == False:
            print("FAIL - Error warning copy is incorrect and does not read '" + var.regV.zipErrorStub + "'")
            funct.fullshot(driver)
            raise Exception('Error warning copy is incorrect.')
        funct.closeWindow(driver, 'New York Lottery - Single Sign On')
        print('----------')

    def test_09_regInvalidFormatPhone(self):
        """Checks invalid phone input error and text copy is correct
        :return:
        """
        print("\nChecks for appearance of error messages when inputting invalid data in phone field")
        driver = self.driver
        # url is pulled from confTest
        driver.get(self.reg_url)
        # triggering error
        funct.waitAndSend(driver, var.regV.phone, "123")
        funct.waitAndSend(driver, var.regV.phone, Keys.TAB)
        if funct.checkErrorText(driver, var.regV.phone_error, var.regV.phoneErrorStub) == True:
            print("PASS - " + var.regV.phone_error[2] + " is present and copy correctly reads as '" + var.regV.phoneErrorStub + "'")
        elif funct.checkErrorText(driver, var.regV.phone, var.regV.phoneErrorStub) == False:
            print("FAIL - Error warning copy is incorrect and does not read '" + var.regV.phoneErrorStub + "'")
            funct.fullshot(driver)
            raise Exception('Error warning copy is incorrect.')
        funct.closeWindow(driver, 'New York Lottery - Single Sign On')
        print('----------')

    def test_10_regInvalidFormatDOB(self):
        """Checks invalid date of birth input error and text copy is correct
        :return:
        """
        print("\nChecks for appearance of error messages when inputting invalid data in DOB field")
        driver = self.driver
        # url is pulled from confTest
        driver.get(self.reg_url)
        # triggering error
        funct.waitAndSend(driver, var.regV.dob, "123")
        funct.waitAndSend(driver, var.regV.dob, Keys.TAB)
        if funct.checkErrorText(driver, var.regV.dob_error, var.regV.dobErrorStub) == True:
            print("PASS - " + var.regV.dob_error[2] + " is present and copy correctly reads as '" + var.regV.dobErrorStub + "'")
        elif funct.checkErrorText(driver, var.regV.dob_error, var.regV.dobErrorStub) == False:
            print("FAIL - Error warning copy is incorrect and does not read '" + var.regV.dobErrorStub + "'")
            funct.fullshot(driver)
            raise Exception('Error warning copy is incorrect.')
        funct.closeWindow(driver, 'New York Lottery - Single Sign On')
        print('----------')

    def test_11_regInvalidFormatEmail(self):
        """Checks invalid email input error and text copy is correct
        :return:
        """
        print("\nChecks for appearance of error messages when inputting invalid data in email field")
        driver = self.driver
        # url is pulled from confTest
        driver.get(self.reg_url)
        # triggering error
        funct.waitAndSend(driver, var.regV.email, "123")
        funct.waitAndSend(driver, var.regV.email, Keys.TAB)
        if funct.checkErrorText(driver, var.regV.email_error, var.regV.emailErrorStub) == True:
            print("PASS - " + var.regV.email_error[2] + " is present and copy correctly reads as '" + var.regV.emailErrorStub + "'")
        elif funct.checkErrorText(driver, var.regV.email_error, var.regV.emailErrorStub) == False:
            print("FAIL - Error warning copy is incorrect and does not read '" + var.regV.emailErrorStub + "'")
            funct.fullshot(driver)
            raise Exception('Error warning copy is incorrect.')
        funct.closeWindow(driver, 'New York Lottery - Single Sign On')
        print('----------')

    def test_12_regInvalidFormatPswNumbers(self):
        """Checks for error is when password format does not follow rules
        :return:
        """
        print("\nChecks for appearance of error messages when inputting only numbers in password field")
        driver = self.driver
        # url is pulled from confTest
        driver.get(self.reg_url)
        # triggering error
        funct.waitAndSend(driver, var.regV.password, "123456789")
        funct.waitAndSend(driver, var.regV.password, Keys.TAB)
        if funct.checkErrorText(driver, var.regV.password_error, var.regV.passwordErrorStub) == True:
            print("PASS - " + var.regV.password_error[2] + " is present and copy correctly reads as '" + var.regV.passwordErrorStub + "'")
        elif funct.checkErrorText(driver, var.regV.password_error, var.regV.passwordErrorStub) == False:
            print("FAIL - Error warning copy is incorrect and does not read '" + var.regV.passwordErrorStub + "'")
            funct.fullshot(driver)
            raise Exception('Error warning copy is incorrect.')
        funct.closeWindow(driver, 'New York Lottery - Single Sign On')
        print('----------')

    def test_13_regInvalidFormatPswLetters(self):
        """Checks for error is when password format does not follow rules
        :return:
        """
        print("\nChecks for appearance of error messages when inputting only letters in password field")
        driver = self.driver
        # url is pulled from confTest
        driver.get(self.reg_url)
        # triggering error
        funct.waitAndSend(driver, var.regV.password, "asdftest")
        funct.waitAndSend(driver, var.regV.password, Keys.TAB)
        if funct.checkErrorText(driver, var.regV.password_error, var.regV.passwordErrorStub) == True:
            print("PASS - " + var.regV.password_error[2] + " is present and copy correctly reads as '" + var.regV.passwordErrorStub + "'")
        elif funct.checkErrorText(driver, var.regV.password_error, var.regV.passwordErrorStub) == False:
            print("FAIL - Error warning copy is incorrect and does not read '" + var.regV.passwordErrorStub + "'")
            funct.fullshot(driver)
            raise Exception('Error warning copy is incorrect.')
        funct.closeWindow(driver, 'New York Lottery - Single Sign On')
        print('----------')

    def test_14_regInvalidFormatPswSymbols(self):
        """Checks for error is when password format does not follow rules
        :return:
        """
        print("\nChecks for appearance of error messages when inputting special characters in password field")
        driver = self.driver
        # url is pulled from confTest
        driver.get(self.reg_url)
        # triggering error
        funct.waitAndSend(driver, var.regV.password, "test")
        funct.waitAndSend(driver, var.regV.password, Keys.SHIFT + "1")
        funct.waitAndSend(driver, var.regV.password, "test")
        funct.waitAndSend(driver, var.regV.password, Keys.TAB)
        # print(driver.find_element(var.regV.password[0],var.regV.password[1]).get_attribute("value"))
        if funct.checkErrorText(driver, var.regV.password_error, var.regV.passwordErrorStub) == True:
            print("PASS - " + var.regV.password_error[2] + " is present and copy correctly reads as '" + var.regV.passwordErrorStub + "'")
        elif funct.checkErrorText(driver, var.regV.password_error, var.regV.passwordErrorStub) == False:
            print("FAIL - Error warning copy is incorrect and does not read '" + var.regV.passwordErrorStub + "'")
            funct.fullshot(driver)
            raise Exception('Error warning copy is incorrect.')
        funct.closeWindow(driver, 'New York Lottery - Single Sign On')
        print('----------')

    def test_15_regMismatchedPsw(self):
        """Checks for error is when passwords do not match
        :return:
        """
        print("\nChecks for appearance of error messages when inputting mismatched passwords")
        driver = self.driver
        # url is pulled from confTest
        driver.get(self.reg_url)
        # triggering error
        funct.waitAndSend(driver, var.regV.password, "test")
        funct.waitAndSend(driver, var.regV.confirmPsw, Keys.SHIFT + "1")
        funct.waitAndSend(driver, var.regV.confirmPsw, Keys.TAB)
        # checking updated error message text
        if funct.checkErrorText(driver, var.regV.confirmPsw_error, var.regV.confirmPswErrorStub) == True:
            print("PASS - " + var.regV.confirmPsw_error[2] + " is present and copy correctly reads as '" + var.regV.confirmPswErrorStub + "'")
        elif funct.checkErrorText(driver, var.regV.confirmPsw_error, var.regV.confirmPswErrorStub) == False:
            print("FAIL - Error warning copy is incorrect and does not read '" + var.regV.confirmPswErrorStub + "'")
            funct.fullshot(driver)
            raise Exception('Error warning copy is incorrect.')
        funct.closeWindow(driver, 'New York Lottery - Single Sign On')
        print('----------')

    def test_16_regUnderage(self):
        """Checks for error is when underage birthdate is entered
        :return:
        """
        print("\nChecks for appearance of error messages when underage Date of Birth is inputted")
        driver = self.driver
        # url is pulled from confTest
        driver.get(self.reg_url)
        # triggering error
        funct.waitAndSend(driver, var.regV.dob, "01/01/2018")
        funct.waitAndSend(driver, var.regV.dob, Keys.TAB)
        # checking updated error message text
        if funct.checkErrorText(driver, var.regV.dob_error, var.regV.dobErrorUnderageStub) == True:
            print("PASS - " + var.regV.dob_error[2] + " is present and copy correctly reads as '" + var.regV.dobErrorUnderageStub + "'")
        elif funct.checkErrorText(driver, var.regV.dob_error, var.regV.dobErrorStub) == False:
            print("FAIL - Error warning copy is incorrect and does not read '" + var.regV.dobErrorUnderageStub + "'")
            funct.fullshot(driver)
            raise Exception('Error warning copy is incorrect.')
        funct.closeWindow(driver, 'New York Lottery - Single Sign On')
        print('----------')

    def test_17_regChkbxErrors(self):
        """Checks error when mandatory checkboxes are not checked
        :return:
        """
        print("\nChecks for appearance of error messages when mandatory checkboxes are not checked")
        driver = self.driver
        # url is pulled from confTest
        driver.get(self.reg_url)
        # triggering error
        funct.waitAndClick(driver, var.regV.submit_button)
        # checking for error messages
        formChecks = driver.find_elements_by_class_name("form-check-label")
        # print(len(formChecks))
        checkCounter = 0
        checkCounterExpected = 2
        for elem in formChecks:
            if "form-check-label error" in elem.get_attribute("class"):
                checkCounter = checkCounter+1
        if checkCounter == checkCounterExpected:
            print("PASS - All checkbox text color change errors are present.")
        else:
            print("FAIL - expected " + str(checkCounterExpected) + " red text changes, but found " + str(checkCounter) + ".")
            funct.fullshot(driver)
            raise Exception('Error warning(s) missing.')
        funct.closeWindow(driver, 'New York Lottery - Single Sign On')
        print('----------')

# use "report" variable in conftest.py to change report style on runner
if __name__ == "__main__":
    if confTest.NYlottoBASE.report == "terminal":
        unittest.main(warnings='ignore')
    elif confTest.NYlottoBASE.report == "html":
        unittest.main(warnings='ignore', testRunner=HtmlTestRunner.HTMLTestRunner(output='<html_report_dir>'))