# [Documentation - Setup] This section lists all dependencies
# that are imported for this test file to work
from selenium import webdriver  #webdriver module provides all WebDriver implementations
import warnings
import unittest, time, re       #unittest is the testing framework, provides module for organizing test cases
from selenium.webdriver.common.keys import Keys     #Keys class provide keys in the keyboard like RETURN, F1, ALT, etc.
from selenium.webdriver.common.by import By         #By class provides method for finding the page elements by NAME, ID, XPATH, etc.
from selenium.webdriver.support.ui import Select    #Select class provides ability to select items in dropdown
import var, funct, util, confTest, HtmlTestRunner   #Custom class for NYL

# [Documentation - Summary] Creates an unverified user that has the following flags:
# custom:ssn_verification	"N"
# custom:phone_verification	"N"
# custom:gov_id_verification	"-"
# custom:verified	"N"

class NYlotto(confTest.NYlottoBASE):
    # replace method arg 'self.testemail' to the email of the user email you want to use
    def test_newUnverified(self, testemail='self.testemail'):
        if testemail == 'self.testemail':
            testemail = self.testemail
        print(testemail)
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
        # Clicks the checkbox for not supplying SSN4 info. Will send user thru ID Verification flow.
        funct.waitAndClick(driver, var.regV.ss_check)
        funct.waitAndSend(driver, var.regV.dob, (var.credsSSOWEB.dob_month + var.credsSSOWEB.dob_date + var.credsSSOWEB.dob_year))
        funct.waitAndClick(driver, var.regV.dob_check)
        funct.waitAndSend(driver, var.regV.email, testemail)
        funct.waitAndSend(driver, var.regV.password, var.credsSSOWEB.password)
        funct.waitAndSend(driver, var.regV.confirmPsw, var.credsSSOWEB.password)
        funct.waitAndClick(driver, var.regV.tos_check)
        funct.waitAndClick(driver, var.regV.submit_button)
        # 2nd screen. OTP selection screen
        funct.waitAndClick(driver, var.otpV.text_button)
        print("Test complete, user created")


# This file is a helper tool for manual testing, no HTML reporting is necessary
# Boiler plate code to run the test suite
if __name__ == "__main__":
    unittest.main(warnings='ignore')