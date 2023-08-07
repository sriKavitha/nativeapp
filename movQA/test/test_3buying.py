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


# [Documentation - Summary] Tests user workflow 

# The test case ex is inherited from unittest.TestCase.
# Inheriting from TestCase class is the way to tell unittest module that this is a test case.
class mov3(confTest.movBASE):
        # [Documentation - local Function] Checks for "allow permissions" buttons, and clicks if found.
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
# [Documentation - Function] Checks for existing test user in userpool and deletes the user if found.
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



# [Documentation - local Function] registers user with un and pw provided
        def register(self, un, pw):
                driver = self.driver
                funct.waitAndClick(driver, var.homePage.searchB)
                funct.waitAndClick(driver, var.register.registerB)
                funct.waitAndClear(driver, var.register.unField)
                funct.waitAndSend(driver, var.register.unField, un)
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

                funct.waitAndSend(driver, var.register.pwField, pw)
                funct.waitAndClick(driver, var.signIn.doneB)
                funct.waitAndClick(driver, var.register.continueB)

                funct.waitAndClick(driver, var.homePage.searchB)


# [Documentation - Function] buys tickets and checks that the total is correct
        def buytickets(self, ticket, number):
                driver = self.driver
                funct.login(self)
                funct.waitAndClick(driver, var.homePage.ticketB)
                funct.waitAndClick(driver, var.tickets.buyMoreB)
                funct.waitAndClick(driver, ticket)
                funct.waitAndClick(driver, var.tickets.nextB)
                time.sleep(1)
                funct.waitAndClick(driver, var.tickets.ccF)
                #workaround for keyboard error on safari screen
#4                TouchAction(driver).tap(x=50, y=599).perform()
#2                TouchAction(driver).tap(x=190, y=539).perform()
#1              TouchAction(driver).tap(x=54, y=536).perform()
                TouchAction(driver).tap(x=50, y=599).perform()
                TouchAction(driver).tap(x=190, y=539).perform()
                TouchAction(driver).tap(x=50, y=599).perform()
                TouchAction(driver).tap(x=190, y=539).perform()
                TouchAction(driver).tap(x=50, y=599).perform()
                TouchAction(driver).tap(x=190, y=539).perform()
                TouchAction(driver).tap(x=50, y=599).perform()
                TouchAction(driver).tap(x=190, y=539).perform()
                TouchAction(driver).tap(x=50, y=599).perform()
                TouchAction(driver).tap(x=190, y=539).perform()
                TouchAction(driver).tap(x=50, y=599).perform()
                TouchAction(driver).tap(x=190, y=539).perform()
                TouchAction(driver).tap(x=50, y=599).perform()
                TouchAction(driver).tap(x=190, y=539).perform()
                TouchAction(driver).tap(x=50, y=599).perform()
                TouchAction(driver).tap(x=190, y=539).perform()
                TouchAction(driver).tap(x=54, y=536).perform()
                TouchAction(driver).tap(x=54, y=536).perform()
                TouchAction(driver).tap(x=190, y=539).perform()
                TouchAction(driver).tap(x=190, y=539).perform()
                TouchAction(driver).tap(x=54, y=536).perform()
                TouchAction(driver).tap(x=54, y=536).perform()
                TouchAction(driver).tap(x=54, y=536).perform()
                TouchAction(driver).tap(x=54, y=536).perform()
                TouchAction(driver).tap(x=54, y=536).perform()
                TouchAction(driver).tap(x=54, y=536).perform()
                TouchAction(driver).tap(x=54, y=536).perform()
                TouchAction(driver).tap(x=54, y=536).perform()

#                funct.waitAndSend(driver, var.tickets.ccF, '4242424242424242112512311385')
                funct.waitAndClick(driver, var.tickets.payB)
                funct.waitAndClick(driver, var.tickets.doneB)
                funct.waitAndClick(driver, var.tickets.okB)
                time.sleep(1)
                funct.waitAndClick(driver, var.tickets.ticketCount)
                tix = driver.find_element_by_xpath('(//*[@type="XCUIElementTypeStaticText"])[2]').get_attribute("value")
                print(tix)
                if tix == str(number):
                        print("ticket buying Success!")
                else:
                        print("expected " + str(number) + " tickets, but got " + str(tix))
                        raise(Exception)


# This is the test case method. The test case method should always start with the characters test.
        def test_0setup(self):
                mov3.removeUser(self, var.register.username)
                mov3.allowPerms(self)
                mov3.register(self, var.register.username, "Test1234")

        def test_buy1(self):
                mov3.allowPerms(self)
                mov3.buytickets(self, var.tickets.tix1, 1)


        def test_buy2(self):
                mov3.allowPerms(self)
                mov3.buytickets(self, var.tickets.tix5, 6)

        def test_buy3(self):
                mov3.allowPerms(self)
                mov3.buytickets(self, var.tickets.tix10, 16)

        def test_buy4(self):
                mov3.allowPerms(self)
                mov3.buytickets(self, var.tickets.tix15, 31)

        def test_buy5(self):
                mov3.allowPerms(self)
                mov3.buytickets(self, var.tickets.tix25, 61)

        def test_buy6(self):
                mov3.allowPerms(self)
                mov3.buytickets(self, var.tickets.tix50, 121)
        def test_buy7(self):
                ticketcount = 222
                mov3.allowPerms(self)
                driver = self.driver
                #mov2.removeUser(self, var.register.username)
                funct.login(self)
                funct.waitAndClick(driver, var.homePage.ticketB)
                funct.waitAndClick(driver, var.tickets.buyMoreB)
                TouchAction(driver).press(x=217, y=552).move_to(x=217, y=239).perform()

                driver.scroll(driver.find_element_by_xpath(var.tickets.tix25[1]), driver.find_element_by_xpath(var.tickets.tix1[1]))
                funct.waitAndClick(driver, var.tickets.tixPlus)
                funct.waitAndClick(driver, var.tickets.nextB)
                funct.waitAndSend(driver, var.tickets.buyTixF, 1)
                funct.waitAndClick(driver, var.tickets.buyB)
                time.sleep(1)
                funct.waitAndClick(driver, var.tickets.buyTixError1)
                funct.waitAndClick(driver, var.tickets.okB)
                funct.waitAndClick(driver, var.tickets.nextB)
                funct.waitAndSend(driver, var.tickets.buyTixF, 101)
                funct.waitAndClick(driver, var.tickets.buyB)
                time.sleep(1)
                funct.waitAndClick(driver, var.tickets.ccF)
                #workaround for keyboard error on safari screen
#4                TouchAction(driver).tap(x=50, y=599).perform()
#2                TouchAction(driver).tap(x=190, y=539).perform()
#1              TouchAction(driver).tap(x=54, y=536).perform()
                TouchAction(driver).tap(x=50, y=599).perform()
                TouchAction(driver).tap(x=190, y=539).perform()
                TouchAction(driver).tap(x=50, y=599).perform()
                TouchAction(driver).tap(x=190, y=539).perform()
                TouchAction(driver).tap(x=50, y=599).perform()
                TouchAction(driver).tap(x=190, y=539).perform()
                TouchAction(driver).tap(x=50, y=599).perform()
                TouchAction(driver).tap(x=190, y=539).perform()
                TouchAction(driver).tap(x=50, y=599).perform()
                TouchAction(driver).tap(x=190, y=539).perform()
                TouchAction(driver).tap(x=50, y=599).perform()
                TouchAction(driver).tap(x=190, y=539).perform()
                TouchAction(driver).tap(x=50, y=599).perform()
                TouchAction(driver).tap(x=190, y=539).perform()
                TouchAction(driver).tap(x=50, y=599).perform()
                TouchAction(driver).tap(x=190, y=539).perform()
                TouchAction(driver).tap(x=54, y=536).perform()
                TouchAction(driver).tap(x=54, y=536).perform()
                TouchAction(driver).tap(x=190, y=539).perform()
                TouchAction(driver).tap(x=190, y=539).perform()
                TouchAction(driver).tap(x=54, y=536).perform()
                TouchAction(driver).tap(x=54, y=536).perform()
                TouchAction(driver).tap(x=54, y=536).perform()
                TouchAction(driver).tap(x=54, y=536).perform()
                TouchAction(driver).tap(x=54, y=536).perform()
                TouchAction(driver).tap(x=54, y=536).perform()
                TouchAction(driver).tap(x=54, y=536).perform()
                TouchAction(driver).tap(x=54, y=536).perform()

#                funct.waitAndSend(driver, var.tickets.ccF, '4242424242424242112512311385')
                funct.waitAndClick(driver, var.tickets.payB)
                funct.waitAndClick(driver, var.tickets.doneB)
                funct.waitAndClick(driver, var.tickets.okB)
                time.sleep(1)
                funct.waitAndClick(driver, var.tickets.ticketCount)
                tix = driver.find_element_by_xpath('(//*[@type="XCUIElementTypeStaticText"])[2]').get_attribute("value")
                print(tix)
                if tix == str(ticketcount):
                        print("ticket buying Success!")
                else:
                        print("expected " + str(ticketcount) + " tickets, but got " + str(tix))
                        raise(Exception)
                



        # Boiler plate code to run the test suite
if __name__ == "__main__":
    # First runner will enable html logs on your current directory, second runner will keep local console logs
    #unittest.main(warnings='ignore', testRunner=HtmlTestRunner.HTMLTestRunner(output='<html_report_dir>'))
    unittest.main(warnings='ignore')