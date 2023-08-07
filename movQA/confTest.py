# [Documentation - Setup] This section lists all dependencies
# that are imported for this test file to work
from selenium import webdriver  #webdriver module provides all WebDriver implementations
import warnings
from browsermobproxy import Server
import unittest, time, re       #unittest is the testing framework, provides module for organizing test cases
from selenium.webdriver.common.keys import Keys     #Keys class provide keys in the keyboard like RETURN, F1, ALT, etc.
from selenium.webdriver.common.by import By         #By class provides method for finding the page elements by NAME, ID, XPATH, etc.
from selenium.webdriver.support.ui import Select    #Select class provides ability to select items in dropdown
import var, funct, util                         #Custom class for NYL
import pytest

class movBASE(unittest.TestCase):

# The setUp is part of initialization, this method will get called before every test function which you
# are going to write in this test case class. Here you are creating the instance of Chrome WebDriver.

    def setUp(self):

        app = ('/Users/foley/Downloads/MOVf2.ipa')
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                "app": app,
                "platformName": "iOS",
                "platformVersion": "13.3",
                "deviceName": "iPhone 8 Plus",
                "automationName": "XCUITest",
            }
        )

# The tearDown method will get called after every test method. This is a place to do all cleanup actions.
    def tearDown(self):
        # NOTE: this code for checking for exceptions does NOT work for Safari
        # Python 3.8+ may have this built in. Need to revisit at future date.
        # checking for exceptions or assertion errors, if there are take screenshot
        # for method, error in self._outcome.errors:
        #     if error:
        #         funct.fullshot(self.driver)
        # # self.driver.quit()
        # self.assertEqual([], self.verificationErrors)
        self.driver.quit()

# loader = unittest.TestLoader()
# start_dir = './'
# suite = loader.discover(start_dir)
#
# runner = unittest.TextTestRunner()
# runner.run(suite)