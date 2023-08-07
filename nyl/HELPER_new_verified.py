# [Documentation - Setup] This section lists all dependencies
# that are imported for this test file to work
from selenium import webdriver  #webdriver module provides all WebDriver implementations
import warnings
import unittest, time, re       #unittest is the testing framework, provides module for organizing test cases
from selenium.webdriver.common.keys import Keys     #Keys class provide keys in the keyboard like RETURN, F1, ALT, etc.
from selenium.webdriver.common.by import By         #By class provides method for finding the page elements by NAME, ID, XPATH, etc.
from selenium.webdriver.support.ui import Select    #Select class provides ability to select items in dropdown
import var, funct, util, confTest, HtmlTestRunner   #Custom class for NYL

# [Documentation - Summary] Creates a verified user that has the following flags:
# custom:ssn_verification	"Y"
# custom:phone_verification	"Y"
# custom:gov_id_verification	"X"
# custom:verified	"Y"

class NYlotto(confTest.NYlottoBASE):
    # replace method arg 'self.testemail' to the email of the user email you want to use
    def test_newVerified(self, testemail='self.testemail'):
        if testemail == 'self.testemail':
            testemail = self.testemail
        # Check for existing test user and wipe it from userpool prior to test execution
        try:
            funct.purgeSSOemail(self, testemail)
            if self.env != 'dev':
                try:
                    funct.purgeSSOphone(self, var.credsSSOWEB.phone)
                except:
                    pass
        except:
            if self.env != 'dev':
                try:
                    funct.purgeSSOphone(self, var.credsSSOWEB.phone)
                except:
                    pass
        driver = self.driver
        # The driver.get method will navigate to a page given by the URL.
        # WebDriver will wait until the page has fully loaded (that is, the “onload” event has fired)
        # before returning control to your test or script.
        # url is pulled from confTest
        driver.get(self.reg_url)
        # Assertion that the title has Single Sign On in the title.
        self.assertIn("Single Sign On", driver.title)

        # Instructions for webdriver to read and input user data via the info on the .txt doc.
        # Credentials are localized to one instance via the var file
        funct.waitAndSend(driver, var.regV.fname, var.credsSSOWEB.fname)
        funct.waitAndSend(driver, var.regV.lname, var.credsSSOWEB.lname)
        funct.waitAndSend(driver, var.regV.housenum, var.credsSSOWEB.housenum)
        funct.waitAndSend(driver, var.regV.street, var.credsSSOWEB.street)
        funct.waitAndSend(driver, var.regV.city, var.credsSSOWEB.city)
        # Find and select the state according to the info in the .txt doc
        # Uses a for loop to iterate through the list of states until element
        # matches the entry info in the text file. Then clicks the element found.
        select_box = driver.find_element_by_name("state")
        funct.waitAndClick(driver, var.regV.state_dropdown)
        options = [x for x in select_box.find_elements_by_tag_name("option")]
        for element in options:
            if element.text in var.credsSSOWEB.state:
                element.click()
                break
        funct.waitAndSend(driver, var.regV.zip, var.credsSSOWEB.zip)
        funct.waitAndSend(driver, var.regV.phone, var.credsSSOWEB.phone)
        funct.waitAndSend(driver, var.regV.ssn4, var.credsSSOWEB.ssn4)
        funct.waitAndSend(driver, var.regV.dob, (var.credsSSOWEB.dob_month + var.credsSSOWEB.dob_date + var.credsSSOWEB.dob_year))
        funct.waitAndClick(driver, var.regV.dob_check)
        funct.waitAndSend(driver, var.regV.email, testemail)
        funct.waitAndSend(driver, var.regV.password, var.credsSSOWEB.password)
        funct.waitAndSend(driver, var.regV.confirmPsw, var.credsSSOWEB.password)
        funct.waitAndClick(driver, var.regV.tos_check)
        funct.waitAndClick(driver, var.regV.submit_button)
        # 2nd screen. OTP selection screen
        funct.waitAndClick(driver, var.otpV.text_button)
        # 3rd screen. OTP code entry screen
        time.sleep(5)
        funct.waitAndSend(driver, var.otpV.otp_input, "111111")
        funct.waitAndClick(driver, var.otpV.otp_continue_button)
        # 4th screen. Successful registration should redirect to Google.com.
        # Checking that the search field on google.com is present on page.
        if driver.find_elements_by_name("q") != []:
             print("PASS - registration successful and redirected to callback uri, user created")
        else:
            funct.fullshot(driver)
            print("FAIL - Redirect screen not reached, but user created")

# This file is a helper tool for manual testing, no HTML reporting is necessary
# Boiler plate code to run the test suite
if __name__ == "__main__":
    unittest.main(warnings='ignore')