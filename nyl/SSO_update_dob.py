# [Documentation - Setup] This section lists all dependencies
# that are imported for this test file to work
from selenium import webdriver  #webdriver module provides all WebDriver implementations
import warnings
import unittest, time, re       #unittest is the testing framework, provides module for organizing test cases
from selenium.webdriver.common.keys import Keys     #Keys class provide keys in the keyboard like RETURN, F1, ALT, etc.
from selenium.webdriver.common.by import By         #By class provides method for finding the page elements by NAME, ID, XPATH, etc.
from selenium.webdriver.support.ui import Select    #Select class provides ability to select items in dropdown
import var, funct, util, confTest                   #Custom class for NYL
import HtmlTestRunner                               #Report runner

class NYlotto(confTest.NYlottoBASE):

    def test_updateDOB(self, testemail='self.testemail'):
        """Tests updating user Date of Birth via Update Profile page

        Jira test ticket - https://rosedigital.atlassian.net/browse/NYL-2041

        Creates a verified SSO user via SSN4 submission, navigates to the Update Profile page,
        submits update and checks for correct frontend updates and redirects
        :param self: Webdriver instance
        :param testemail: email of the user being updated, default is the email in conftest.py
        :return: None
        """
        if testemail == 'self.testemail':
            testemail = self.testemail
        testenv = self.env
        print("TESTING " + testenv + " ENVIRONMENT")
        print("\nChecks date of birth change in update profile saves and redirects to OTP")

        print('\n----------\n' + 'Test setup')
        # creates a verified user with valid SSN4
        funct.createVerifiedUser(self, testemail)
        print('----------')

        driver = self.driver
        # url is pulled from confTest
        driver.get(self.update_url)
        time.sleep(2)
        # Makes change in field and submits
        dobChange = '01011990'
        formattedChange = dobChange[:2] + "/" + dobChange[2:4] + "/" + dobChange[4:]
        funct.clearTextField(driver, var.updateProfV.dob)
        funct.waitAndSend(driver, var.updateProfV.dob, dobChange)
        funct.waitAndClick(driver, var.updateProfV.update_button)
        time.sleep(2)
        # 2nd screen. OTP selection screen
        funct.waitAndClick(driver, var.otpV.text_button)
        # 3rd screen. OTP code entry screen
        funct.waitAndSend(driver, var.otpV.otp_input, "111111")
        funct.waitAndClick(driver, var.otpV.otp_continue_button)
        time.sleep(5)
        # check for proper redirect to Google.com
        if driver.find_elements_by_name("q") != []:
            print('Update profile successfully redirected to Google.')
        else:
            funct.fullshot(driver)
            print('FAIL - Update profile redirect screen not reached. Test can not proceed.')
            try:
                funct.purgeSSOemail(self, testemail)
            except:
                pass
            raise Exception('Update profile redirected incorrectly')
        # Checks the change has been saved to the profile
        driver.get(self.update_url)
        time.sleep(5)
        change = driver.find_element(var.updateProfV.dob[0], var.updateProfV.dob[1])
        if funct.checkValue(driver, var.updateProfV.dob, formattedChange) == True:
            print('PASS - Profile update change for ' + var.updateProfV.dob[2] + ' successfully saved to user.')
            print('Updated text is "' + change.get_attribute("value") + '"')
        elif funct.checkValue(driver, var.updateProfV.dob, formattedChange) == False:
            print(
                'FAIL - Updated ' + var.updateProfV.dob[2] + ' field should say "' + dobChange + '" , but says "' + change.get_attribute(
                    "value") + '"!')
            funct.fullshot(driver)
            try:
                funct.purgeSSOemail(self, testemail)
            except:
                pass
            raise Exception('Update profile changes failed to save.')

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