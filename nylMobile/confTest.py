# [Documentation - Setup] This section lists all dependencies
# that are imported for this test file to work
from selenium import webdriver  #webdriver module provides all WebDriver implementations
import warnings
from browsermobproxy import Server
import unittest, time, re       #unittest is the testing framework, provides module for organizing test cases
from selenium.webdriver.common.keys import Keys     #Keys class provide keys in the keyboard like RETURN, F1, ALT, etc.
from selenium.webdriver.common.by import By         #By class provides method for finding the page elements by NAME, ID, XPATH, etc.
from selenium.webdriver.support.ui import Select    #Select class provides ability to select items in dropdown
import var, funct, HtmlTestRunner                    #Custom class for NYL

class NYLmobileBASE(unittest.TestCase):

# The setUp is part of initialization, this method will get called before every test function which you
# are going to write in this test case class. Here you are creating the instance of Chrome WebDriver.

    def setUp(self):
        desired_caps = {
            "deviceName": "Galaxy S7",
            "udid": "emulator-5554",
            "platformName": "Android",
            "version" : "8.0",
            "app": "/Users/Shared/testing/app-qa.apk",
            "realDevice": False
        }
        self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_caps)
        self.verificationErrors = []
        self.driver.implicitly_wait(12)
 


# The tearDown method will get called after every test method. This is a place to do all cleanup actions.
    def tearDown(self):
        # NOTE: this code for checking for exceptions does NOT work for Safari
        # Python 3.8+ may have this built in. Need to revisit at future date.
        # checking for exceptions or assertion errors, if there are take screenshot
        ### If methods can be ported to mobile, this code will be re-used
        # for method, error in self._outcome.errors:
        #     if error:
        #         funct.fullshot(self)
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)