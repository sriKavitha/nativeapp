# [Documentation - Setup] This section lists all dependencies
# that are imported for function file to work
from browsermobproxy import Server
from selenium import webdriver
import unittest, time, re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import os, json, boto3, var
from urllib.parse import urlparse


# [Documentation - Summary] This file creates the functions for
# use in all test cases within the automation test suite of MOV




# [Documentation - Function] uses a filtering method to more easily get and maintain credentials from the credential page (which is now localized to one instance via the var page)
# target should be given plainly, without colons
def getCredential(list, target):
    targ = str(target + ': ')
    credential = [item for item in list if item.startswith(targ)][0]
    cred = credential.replace(targ, '')
    return cred


# [Documentation - logs in using the phone and password variables from the creds variable class]
def login(self):
    driver = self.driver
    waitAndClick(driver, var.homePage.searchB)
    waitAndClick(driver, var.signIn.loginB)
    waitAndSend(driver, var.signIn.numF, var.creds.phone)
    waitAndClear(driver, var.signIn.pwF)
    waitAndSend(driver, var.signIn.pwF, var.creds.password)
    waitAndClick(driver, var.signIn.doneB)
    waitAndClick(driver, var.signIn.continueB)
    waitUntil(driver, var.homePage.ticketB)
    checkElem(driver, var.homePage.ticketB)

# [Documentation - Function] Webdriver waits for a specified page element
def waitUntil(browser, elem):
    try:
        browser.find_element(elem[0], elem[1])
        assert(browser.find_element(elem[0], elem[1]))
    except:
        time.sleep(2)
        try:
            # [Documentation - option] allows for automatic scrolling if element not found (unstable)
            #browser.execute_script("arguments[0].scrollIntoView();", browser.find_element(elem[0], elem[1]))
            browser.find_element(elem[0], elem[1])
        except:
            print("E--" + elem[2] + " elem not found")
            browser.find_element(elem[0], elem[1])

# [Documentation - Function] Webdriver waits for a specified page element
# to appear and then proceeds to verify it exists
def checkElem(browser, elem):
        browser.find_element(elem[0], elem[1])
        assert(browser.find_element(elem[0], elem[1]))

# [Documentation - Function] Preset function for clicking the "allow" buttons that appear upon opening of MOV, if they exist
def Allow(self):
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
# [Documentation - Function] Webdriver waits for a specified page element
# to appear and then proceeds to click on it
def waitAndClick(browser, elem):
    waitUntil(browser, elem)
    #a.move_to_element(browser.find_element(elem[0], elem[1])).click()  
    browser.find_element(elem[0], elem[1]).click()

# [Documentation - Function] Webdriver waits for a specified page element
# to appear and then proceeds to send keys to it
def waitAndSend(browser, elem, keys):
    waitUntil(browser, elem)
    browser.find_element(elem[0], elem[1]).click()
    browser.find_element(elem[0], elem[1]).send_keys(keys)
    try:
        waitAndClick(driver, var.signIn.doneB)
    except:
        pass
# [Documentation - Function] Webdriver waits for a specified field page element
# to appear and then proceeds to clear it
def waitAndClear(browser, elem):
    waitUntil(browser, elem)
    browser.find_element(elem[0], elem[1]).clear()

# [Documentation - Function] Function that grabs UTC time and converts to human readable format
def timeStamp():
    ts = time.gmtime()
    times = time.strftime("%Y-%m-%d_%H-%M-%S", ts)
    return times

# [Documentation - Function] Function that checks the text of a given element against a given stub
def checkText(browser, elem, stub):
    waitUntil(browser, elem)
    el = browser.find_element(elem[0], elem[1])
    if el.text == stub:
        assert el.text == stub
    else:
        print('E---Text Incorrect!\n\nExpected text: "' + stub + '"\n\n but text was: "' + el.text + '"')
        assert el.text == stub

