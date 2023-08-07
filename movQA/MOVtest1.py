# [Documentation - Setup] This section lists all dependencies
# that are imported for this test file to work
from appium import webdriver  #webdriver module provides all WebDriver implementations
import warnings
import unittest, time, re       #unittest is the testing framework, provides module for organizing test cases
from selenium.webdriver.common.keys import Keys     #Keys class provide keys in the keyboard like RETURN, F1, ALT, etc.
from selenium.webdriver.common.by import By         #By class provides method for finding the page elements by NAME, ID, XPATH, etc.
from selenium.webdriver.support.ui import Select    #Select class provides ability to select items in dropdown
import var, funct, util, confTest, HtmlTestRunner   #Custom class for mov
from appium.webdriver.common.touch_action import TouchAction
# [Documentation - Summary] Tests user workflow of successful
# registration with valid SSN4 and OTP pass
# For use with Entry Info file version: movCreds.txt

# The test case ex is inherited from unittest.TestCase.
# Inheriting from TestCase class is the way to tell unittest module that this is a test case.
class mov(confTest.movBASE):
        def allowPerms(self):
                driver = self.driver
                try:
                        print("finding allow1")
                        funct.checkElem(driver, var.homePage.allowB2)
                        funct.waitAndClick(driver, var.homePage.allowB2)
                        print("found")     
                except:
                        pass           
                try:
                        print("finding allow2")
                        driver.find_element_by_xpath('//*[@name="Allow"]').click()
                        print("found")   
                except:
                        pass           

# This is the test case method. The test case method should always start with the characters test.
# The first line inside this method creates a local reference to the driver object created in setUp method.
        def test_login1_cancelButton(self):
                driver = self.driver
                mov.allowPerms(self)
        # # Check for existing test user and wipe it from userpool prior to test execution
        #         # try:
        #         #     funct.purge(self, self.phonenum)
        #         #     print('test user purged')
        #         # except:
        #         #     print('no test user found')
        #funct.waitAndClick(driver, var.homePage.allowB)

                funct.waitAndClick(driver, var.homePage.searchB)
                funct.waitAndClick(driver, var.signIn.xB)

                
                try:
                        funct.checkElem(driver, var.signIn.pwF)
                        print("\nE----modal x button does not work!\n")
                except:
                        print("\nLogin Cancel Success!\n")
        
        def test_login2_incorrectPhone(self):
                driver = self.driver
                mov.allowPerms(self)
                print("Checking sign in")
                funct.waitAndClick(driver, var.homePage.searchB)
                funct.waitAndClick(driver, var.signIn.loginB)
                funct.waitAndSend(driver, var.signIn.numF, "516")
                funct.waitAndClick(driver, var.signIn.doneB)
                funct.waitAndClick(driver, var.signIn.continueB)
                try:
                        funct.checkElem(driver, var.signIn.invalidPhoneNumber)
                        print("\nincorrect phone number success!\n")
                except:
                        print("\nE----phone error message not working!\n")
                        funct.checkElem(driver, var.signIn.invalidPhoneNumber)

        def test_login3_noPassword(self):
                driver = self.driver
                mov.allowPerms(self)
                funct.waitAndClick(driver, var.homePage.searchB)
                funct.waitAndClick(driver, var.signIn.loginB)
                # funct.waitAndClick(driver, var.signIn.okB)
                funct.waitAndSend(driver, var.signIn.numF, var.creds.phone)
                funct.waitAndClick(driver, var.signIn.doneB)
                funct.waitAndClick(driver, var.signIn.continueB)
                try:
                        funct.checkElem(driver, var.signIn.noPwError)
                        print("\nno password success\n")
                except:
                        print("\nE----data error message not working!\n")
                        funct.checkElem(driver, var.signIn.noPwError)
                        
                funct.waitAndClick(driver, var.signIn.okB)

        def test_login4_incorrectPassword(self):
                driver = self.driver
                mov.allowPerms(self)
                funct.waitAndClick(driver, var.homePage.searchB)
                funct.waitAndClick(driver, var.signIn.loginB)
                funct.waitAndSend(driver, var.signIn.numF, var.creds.phone)
                funct.waitAndSend(driver, var.signIn.pwF, "867")
                funct.waitAndClick(driver, var.signIn.doneB)
                funct.waitAndClick(driver, var.signIn.continueB)
                try:
                        funct.checkElem(driver, var.signIn.invalidData)
                except:
                        print("\nE----data error message not working!\n")
                        
                funct.waitAndClick(driver, var.signIn.okB)

        def test_login5_successfulTest(self):
                driver = self.driver
                mov.allowPerms(self)
                funct.waitAndClick(driver, var.homePage.searchB)
                funct.waitAndClick(driver, var.signIn.loginB)
                funct.waitAndSend(driver, var.signIn.numF, var.creds.phone)
                funct.waitAndClear(driver, var.signIn.pwF)
                funct.waitAndSend(driver, var.signIn.pwF, var.creds.password)
                funct.waitAndClick(driver, var.signIn.doneB)
                funct.waitAndClick(driver, var.signIn.continueB)
                try:
                        funct.waitUntil(driver, var.homePage.ticketB)
                        funct.checkElem(driver, var.homePage.ticketB)
                        print("\nTest Successful!\n")
                except:
                        print("\nE----Successful Login failure!\n")



if __name__ == "__main__":
    # First runner will enable html logs on your current directory, second runner will keep local console logs
    unittest.main(warnings='ignore', testRunner=HtmlTestRunner.HTMLTestRunner(output='<html_report_dir>'))
    #unittest.main(warnings='ignore')