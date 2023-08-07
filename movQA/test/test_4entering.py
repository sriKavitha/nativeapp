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


# The test case ex is inherited from unittest.TestCase.
# Inheriting from TestCase class is the way to tell unittest module that this is a test case.
class mov4(confTest.movBASE):
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
        
        
        def buy101tix(self):
                driver = self.driver
                funct.waitAndClick(driver, var.homePage.homeB)
                funct.waitAndClick(driver, var.homePage.ticketB)
                funct.waitAndClick(driver, var.tickets.buyMoreB)
                TouchAction(driver).press(x=217, y=552).move_to(x=217, y=239).perform()

                driver.scroll(driver.find_element_by_xpath(var.tickets.tix25[1]), driver.find_element_by_xpath(var.tickets.tix1[1]))
                funct.waitAndClick(driver, var.tickets.tixPlus)
                funct.waitAndClick(driver, var.tickets.nextB)
                funct.waitAndSend(driver, var.tickets.buyTixF, 101)
                funct.waitAndClick(driver, var.tickets.buyB)
                time.sleep(1)
                funct.waitAndClick(driver, var.tickets.ccF)
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
                funct.waitAndClick(driver, var.tickets.payB)
                funct.waitAndClick(driver, var.tickets.doneB)
                funct.waitAndClick(driver, var.tickets.okB)
                time.sleep(1)
                funct.waitAndClick(driver, var.tickets.ticketCount)


        def test_0setup(self):
                mov4.removeUser(self, var.register.username)
                mov4.allowPerms(self)
                mov4.register(self, var.register.username, "Test1234")
                mov4.buy101tix(self)

        def test_raffle1(self):
                number = 99
                driver = self.driver
                mov4.allowPerms(self)
                funct.login(self)
                funct.waitAndClick(driver, var.homePage.raffleB)
                time.sleep(1)
                TouchAction(driver).tap(x=211, y=371).perform()
                time.sleep(1)
                funct.waitAndClick(driver, var.raffle.selectB)
                funct.waitAndClick(driver, var.raffle.dontAllowB)
                funct.waitAndClick(driver, var.raffle.selectB)
                funct.waitAndClick(driver, var.raffle.okB)
                time.sleep(3)
                try:
                        funct.waitAndClick(driver, var.homePage.ticketB)
                        funct.checkElem(driver, var.homePage.ticketB)
                except:

                        time.sleep(4)
                        funct.waitAndClick(driver, var.homePage.ticketB)
                time.sleep(4)
                try:
                        funct.waitAndClick(driver, var.tickets.ticketCount)
                except:
                        time.sleep(2)
                        pass
                tix = driver.find_element_by_xpath('(//*[@type="XCUIElementTypeStaticText"])[2]').get_attribute("value")
                print(tix)
                if tix == str(number):
                        print("ticket buying Success!")
                else:
                        print("expected " + str(number) + " tickets, but got " + str(tix))
                        raise(Exception)
        
        def test_raffle2(self):
                number = 99
                driver = self.driver
                mov4.allowPerms(self)
                funct.login(self)
                funct.waitAndClick(driver, var.homePage.raffleB)
                funct.waitAndClick(driver, var.raffle.customB)
                funct.waitAndClick(driver, var.raffle.customF)
                funct.waitAndSend(driver, var.raffle.customF, "12")
                funct.waitAndClick(driver, var.signIn.doneB)
                funct.waitAndClick(driver, var.raffle.customE1)
                funct.waitAndClick(driver, var.raffle.okB2)
                funct.waitAndSend(driver, var.raffle.customF, "120")
                funct.waitAndClick(driver, var.signIn.doneB)
                funct.waitAndClick(driver, var.raffle.customE2)
                funct.waitAndClick(driver, var.raffle.reloadB)
                time.sleep(4)
                try:
                        funct.waitAndClick(driver, var.tickets.ticketCount)
                except:
                        time.sleep(2)
                        pass
                tix = driver.find_element_by_xpath('(//*[@type="XCUIElementTypeStaticText"])[2]').get_attribute("value")
                print(tix)
                if tix == str(number):
                        print("ticket buying Success!")
                else:
                        print("expected " + str(number) + " tickets, but got " + str(tix))
                        raise(Exception)

        def test_raffle3(self):
                number = 0
                driver = self.driver
                mov4.allowPerms(self)
                funct.login(self)
                funct.waitAndClick(driver, var.homePage.raffleB)
                funct.waitAndClick(driver, var.raffle.customB)
                funct.waitAndSend(driver, var.raffle.customF, "99")
                funct.waitAndClick(driver, var.signIn.doneB)
                funct.waitAndClick(driver, var.raffle.okB)
                time.sleep(3)
                try:
                        funct.waitAndClick(driver, var.homePage.ticketB)
                        funct.checkElem(driver, var.homePage.ticketB)
                except:

                        time.sleep(4)
                        funct.waitAndClick(driver, var.homePage.ticketB)
                
                time.sleep(1)
                try:
                        funct.waitAndClick(driver, var.tickets.ticketCount)
                        funct.checkElem(driver, var.tickets.ticketCount)
                except:

                        time.sleep(4)
                        pass
                tix = driver.find_element_by_xpath(var.tickets.ticketCount[1]).get_attribute("value")
                print(tix)
                if tix == str(number):
                        print("ticket buying Success!")
                else:
                        print("expected " + str(number) + " tickets, but got " + str(tix))
                        raise(Exception)           
     




        

                



        # Boiler plate code to run the test suite
if __name__ == "__main__":
    # First runner will enable html logs on your current directory, second runner will keep local console logs
    #unittest.main(warnings='ignore', testRunner=HtmlTestRunner.HTMLTestRunner(output='<html_report_dir>'))
    unittest.main(warnings='ignore')