# [Documentation - Setup] This section lists all dependencies
# that are imported for this test file to work
from selenium import webdriver  #webdriver module provides all WebDriver implementations
import warnings
import unittest, time, re       #unittest is the testing framework, provides module for organizing test cases
from selenium.webdriver.common.keys import Keys     #Keys class provide keys in the keyboard like RETURN, F1, ALT, etc.
from selenium.webdriver.common.by import By         #By class provides method for finding the page elements by NAME, ID, XPATH, etc.
from selenium.webdriver.support.ui import Select    #Select class provides ability to select items in dropdown
import var, funct, util, confTest, HtmlTestRunner                            #Custom class for NYL

# The test case class is inherited from unittest.TestCase.
# Inheriting from TestCase class is the way to tell unittest module that this is a test case.
class MOBILEnyl(confTest.NYLmobileBASE):

#tests the text on the dashboard page
        def test_dashboardCheckText(self):
                driver = self.driver
                funct.checkText(driver, var.NYLdashboard.guestCopy, var.NYLdashboard.guestStub)
                funct.checkText(driver, var.NYLdashboard.loginCopy, var.NYLdashboard.loginStub)
#checks that a successful registrations works correctly              
        def test_regSuccess(self):
                driver = self.driver
                timeStamp = funct.timeStamp()
                funct.waitAndClick(driver, var.NYLdashboard.register_b)
                funct.waitAndSend(driver, var.NYLregistration.email_f,  'FAKE_' + timeStamp + "@fakerose.co")
                funct.waitAndSend(driver, var.NYLregistration.password_f, "Foleyfoley1")
                funct.waitAndSend(driver, var.NYLregistration.confirmPW_f , "Foleyfoley1")
                funct.waitAndSend(driver, var.NYLregistration.firstName_f, "Foley")
                funct.waitAndClick(driver, var.NYLregistration.firstName_f)
                funct.actionSend(driver, Keys.TAB)
                funct.actionSend(driver, 'foley')
                funct.actionSend(driver, Keys.TAB)
                funct.actionSend(driver, Keys.TAB)
                funct.actionSend(driver, "5168675309")
                funct.actionSend(driver, Keys.TAB)
                funct.actionSend(driver, Keys.TAB)
                funct.actionSend(driver, Keys.TAB)
                funct.actionSend(driver, Keys.TAB)
                funct.actionSend(driver, Keys.TAB)
                funct.waitAndSend(driver, var.NYLregistration.zip_f, "11111")
                funct.waitAndClick(driver, var.NYLregistration.yes_b)
                funct.waitAndClick(driver, var.NYLregistration.reg_b)
                funct.waitUntil(driver, var.NYLregistration.pip1)


# Boiler plate code to run the test suite
if __name__ == "__main__":
        #First runner will enable html logs on your current directory, second runner will keep local console logs
        unittest.main(warnings='ignore', testRunner=HtmlTestRunner.HTMLTestRunner(output='html_report_dir'))
        # unittest.main(warnings='ignore')