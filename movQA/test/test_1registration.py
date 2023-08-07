# [Documentation - Setup] This section lists all dependencies
# that are imported for this test file to work
from appium import webdriver  #webdriver module provides all WebDriver implementations
import warnings
import unittest, time, re       #unittest is the testing framework, provides module for organizing test cases
from selenium.webdriver.common.keys import Keys     #Keys class provide keys in the keyboard like RETURN, F1, ALT, etc.
from selenium.webdriver.common.by import By         #By class provides method for finding the page elements by NAME, ID, XPATH, etc.
from selenium.webdriver.support.ui import Select    #Select class provides ability to select items in dropdown
import var, funct, confTest, HtmlTestRunner   #Custom class for MOV
from appium.webdriver.common.touch_action import TouchAction
import requests


# [Documentation - Summary] Tests user workflow of successful


# The test case ex is inherited from unittest.TestCase.
# Inheriting from TestCase class is the way to tell unittest module that this is a test case.
class mov2(confTest.movBASE):
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

        def removeUser(self, user):
                auth_token=var.creds.authToken
                hed = {'Authorization': 'Bearer ' + auth_token}
                data = {
                "password": var.creds.authPW,
                "username": user
                }

                url = 'https://api-dev.mymov.com/api/v1/automation/users/delete'
                response = requests.post(url, json=data, headers=hed)
                print(response)
                print(response.json())          

# This is the test case method. The test case method should always start with the characters test.
# The first line inside this method creates a local reference to the driver object created in setUp method.
        def test_reg1_deleteOlderRegistration(self):
                mov2.removeUser(self, var.register.username)
        
        def test_reg2_usernameField(self):
                driver = self.driver
                mov2.allowPerms(self)
                funct.waitAndClick(driver, var.homePage.searchB)
                funct.waitAndClick(driver, var.register.registerB)
                funct.waitAndClick(driver, var.register.backArrow)
                funct.waitAndClick(driver, var.homePage.searchB)
                funct.waitAndClick(driver, var.register.registerB)

                funct.waitAndClick(driver, var.register.continueB)
                funct.waitAndClick(driver, var.register.unError1)
                funct.waitAndClick(driver, var.register.okB)

                funct.waitAndSend(driver, var.register.unField, "1")
                funct.waitAndClick(driver, var.signIn.doneB)
                funct.waitAndClick(driver, var.register.continueB)
                funct.waitAndClick(driver, var.register.unError2)
                funct.waitAndClick(driver, var.register.okB)

                funct.waitAndClear(driver, var.register.unField)
                funct.waitAndSend(driver, var.register.unField, var.register.username)
                funct.waitAndClick(driver, var.signIn.doneB)                
                funct.waitAndClick(driver, var.register.continueB)              

                time.sleep(1)
               
                funct.waitAndClick(driver, var.register.backArrow)
                funct.waitAndClear(driver, var.register.unField)
                funct.waitAndSend(driver, var.register.unField, var.register.username)
                funct.waitAndClick(driver, var.signIn.doneB)
                funct.waitAndClick(driver, var.register.continueB)              

        def test_reg3_phoneField(self):
                driver = self.driver
                mov2.allowPerms(self)
                funct.waitAndClick(driver, var.homePage.searchB)
                funct.waitAndClick(driver, var.register.registerB)
                funct.waitAndClear(driver, var.register.unField)
                funct.waitAndSend(driver, var.register.unField, var.register.username)
                funct.waitAndClick(driver, var.signIn.doneB)                
                funct.waitAndClick(driver, var.register.continueB)              

                time.sleep(1)
                funct.waitAndClick(driver, var.register.continueB)
                funct.waitAndClick(driver, var.register.phoneError1)
                funct.waitAndClick(driver, var.register.okB)

                funct.waitAndSend(driver, var.register.phoneF, var.register.usedNumber)
                funct.waitAndClick(driver, var.signIn.doneB)
                funct.waitAndClick(driver, var.register.continueB)
                funct.waitAndClick(driver, var.register.phoneError2)
                funct.waitAndClick(driver, var.register.okB)

                funct.waitAndClear(driver, var.register.phoneF)
                funct.waitAndSend(driver, var.register.phoneF, var.creds.phone)
                funct.waitAndClick(driver, var.signIn.doneB)
                funct.waitAndClick(driver, var.register.continueB)

                funct.waitAndClick(driver, var.register.backArrow)
                funct.waitAndClear(driver, var.register.phoneF)
                funct.waitAndSend(driver, var.register.phoneF, var.creds.phone)
                funct.waitAndClick(driver, var.signIn.doneB)
                funct.waitAndClick(driver, var.register.continueB)

        def test_reg4_pinField(self):
                driver = self.driver
                mov2.allowPerms(self)
                funct.waitAndClick(driver, var.homePage.searchB)
                funct.waitAndClick(driver, var.register.registerB)
                funct.waitAndClear(driver, var.register.unField)
                funct.waitAndSend(driver, var.register.unField, var.register.username)
                funct.waitAndClick(driver, var.signIn.doneB)                
                funct.waitAndClick(driver, var.register.continueB)              
                funct.waitAndClear(driver, var.register.phoneF)
                funct.waitAndSend(driver, var.register.phoneF, var.creds.phone)
                funct.waitAndClick(driver, var.signIn.doneB)
                funct.waitAndClick(driver, var.register.continueB)
                #
                time.sleep(1)
                funct.waitAndClick(driver, var.register.continueB)
                funct.waitAndClick(driver, var.register.pinError1)
                funct.waitAndClick(driver, var.register.okB)

                funct.waitAndSend(driver, var.register.pinF, "1")
                funct.waitAndClick(driver, var.signIn.doneB)
                funct.waitAndClick(driver, var.register.continueB)
                funct.waitAndClick(driver, var.register.pinError2)
                funct.waitAndClick(driver, var.register.okB)

                funct.waitAndClear(driver, var.register.pinF)
                funct.waitAndSend(driver, var.register.pinF, "0000")
                funct.waitAndClick(driver, var.signIn.doneB)
                funct.waitAndClick(driver, var.register.continueB)
                funct.waitAndClick(driver, var.register.pinError3)
                funct.waitAndClick(driver, var.register.okB)

                funct.waitAndClear(driver, var.register.pinF)



        def test_reg5_pwField(self):
                driver = self.driver
                mov2.allowPerms(self)

                funct.waitAndClick(driver, var.homePage.searchB)
                funct.waitAndClick(driver, var.register.registerB)
                funct.waitAndClear(driver, var.register.unField)
                funct.waitAndSend(driver, var.register.unField, var.register.username)
                funct.waitAndClick(driver, var.signIn.doneB)                
                funct.waitAndClick(driver, var.register.continueB)              
                funct.waitAndClear(driver, var.register.phoneF)
                funct.waitAndSend(driver, var.register.phoneF, var.creds.phone)
                funct.waitAndClick(driver, var.signIn.doneB)
                funct.waitAndClick(driver, var.register.continueB)
                funct.waitAndClear(driver, var.register.pinF)
                funct.waitAndSend(driver, var.register.pinF, "1234")
                funct.waitAndClick(driver, var.signIn.doneB)
                funct.waitAndClick(driver, var.register.continueB)
                time.sleep(1)

                funct.waitAndClick(driver, var.register.continueB)
                funct.waitAndClick(driver, var.register.pwError1)
                funct.waitAndClick(driver, var.register.okB)

                funct.waitAndSend(driver, var.register.pwField, "0")
                funct.waitAndClick(driver, var.signIn.doneB)
                funct.waitAndClick(driver, var.register.continueB)
                funct.waitAndClick(driver, var.register.pwError2)
                funct.waitAndClick(driver, var.register.okB)
                funct.waitAndClear(driver, var.register.pwField)
                funct.waitAndSend(driver, var.register.pwField, "Test1234")
                funct.waitAndClick(driver, var.signIn.doneB)
                funct.waitAndClick(driver, var.register.continueB)

                funct.waitAndClick(driver, var.homePage.searchB)
                print("\n\nTest completed successfully!")
                




        # Boiler plate code to run the test suite
if __name__ == "__main__":
    # First runner will enable html logs on your current directory, second runner will keep local console logs
    #unittest.main(warnings='ignore', testRunner=HtmlTestRunner.HTMLTestRunner(output='<html_report_dir>'))
    unittest.main(warnings='ignore')