# [Documentation - Setup] This section lists all dependencies
# that are imported for function file to work
from browsermobproxy import Server
from selenium import webdriver
import unittest, time, re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import os, json, util, boto3, var
from urllib.parse import urlparse


# [Documentation - Summary] This file creates the functions for
# use in the automation test suite of Rewild

# [Documentation - Function] uses a filtering method to more easily get and maintain credentials from the credential page (which is now localized to one instance via the var page)
# target should be given plainly, without colons
def getCredential(list, target):
    targ = str(target + ': ')
    credential = [item for item in list if item.startswith(targ)][0]
    cred = credential.replace(targ, '')
    return cred

# [Documentation - Function] Mobile Webdriver uses actionchains to swipe upwards once (at 1/4 of the screen's length) from the element given

def swipeUp(browser, elem1, amount=-.25):
    size=browser.get_window_size()
    height = int(size['height'])
    a = ActionChains(browser)
    el1 = browser.find_element(elem1[0], elem1[1])
    a.drag_and_drop_by_offset(el1, 0, amount*height).perform()
    time.sleep(1)

# [Documentation - Function] Mobile Webdriver uses actionchains to swipe upwards from the first element given, until the second element is found
def swipeUpUntil(browser, elem1, elem2, amount=-.15):
    browser.implicitly_wait(3)
    size=browser.get_window_size()
    height = int(size['height'])
    whilebool = False
    while whilebool == False:
        a = ActionChains(browser)
        el1 = browser.find_element(elem1[0], elem1[1])
        a.drag_and_drop_by_offset(el1, 0, amount*height).perform()
        try:
            browser.find_element(elem2[0], elem2[1])
            whilebool = True
        except:
            pass
    time.sleep(1)
    browser.implicitly_wait(12)

# [Documentation - Function] Mobile Webdriver uses actionchains to swipe leftwards from the first element given, until the second element is found

def swipeLeftUntil(browser, elem1, elem2):
    browser.implicitly_wait(3)
    size=browser.get_window_size()
    #print(size)
    width = int(size['width'])
    whilebool = False
    while whilebool == False:
        a = ActionChains(browser)
        el1 = browser.find_element(elem1[0], elem1[1])
        a.drag_and_drop_by_offset(el1, -1*width, 0).perform()
        try:
            browser.find_element(elem2[0], elem2[1])
            whilebool = True
        except:
            pass
    time.sleep(1)
    browser.implicitly_wait(12)

# [Documentation - Function] starts a browsermob proxy and generates a har file of current page
def generateHAR(server, driver):
    hurl = str(driver.current_url)
    server = Server("/Users/browsermob-proxy-2.1.4/bin/browsermob-proxy",  options={'port': 8090})
    server.start()
    proxy = server.create_proxy()
    chromedriver = "/usr/local/bin/chromedriver"
    url = urlparse(proxy.proxy).path
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--proxy-server={0}".format(url))
    driver = webdriver.Chrome(chromedriver, options=chrome_options)
    proxy.new_har("test", options={'captureHeaders': True})
    driver.get(hurl)
    result = json.dumps(proxy.har, ensure_ascii=False)
    print(result)
    harname = str('HAR_' + timeStamp())
    with open(harname, 'w') as har_file:
        json.dump(proxy.har, har_file)
    proxy.close()

# [Documentation - Function] Webdriver uses actionchains to  wait for a specified page element
def waitUntil(browser, elem):
    a = ActionChains(browser)
    try:
        a.move_to_element(browser.find_element(elem[0], elem[1])).perform()
        assert(browser.find_element(elem[0], elem[1]))
    except:
        time.sleep(2)
        try:
            a.move_to_element(browser.find_element(elem[0], elem[1])).perform()
            assert(browser.find_element(elem[0], elem[1]))
        except:
            print("E--" + elem[1] + " elem not found")

# [Documentation - Function] Webdriver waits for a specified page element
# to appear and then proceeds to click on it
def waitAndClick(browser, elem):
    waitUntil(browser, elem)
    browser.find_element(elem[0], elem[1]).click()

# [Documentation - Function] Webdriver waits for a specified page element
# to appear and then proceeds to send keys to it
def waitAndSend(browser, elem, keys):
    waitUntil(browser, elem)
    browser.find_element(elem[0], elem[1]).send_keys(keys)

def clearTextField(browser, elem):
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

# [Documentation - Function] Function that calls the script to grab full page UTC timestamped screenshot
def fullshot(browser):
    browser.set_window_position(0, 0)
    browser.maximize_window()
    timestamp = timeStamp() + '.png'
    util.fullpage_screenshot(browser, timestamp)

# [Documentation - Function] Checks that an error exists
def checkError(browser, elemWarning):
    try:
        browser.find_element(elemWarning[0], elemWarning[1])
        return True
    except:
        return False

# [Documentation - Function] Checks the actual warning text against the reported warning copy
def checkErrorText(browser, elemWarning, elemWarningStub):
    warning = browser.find_element(elemWarning[0], elemWarning[1])
    if warning.get_attribute("innerText") == elemWarningStub:
        return True
    else:
        return False


# [Documentation - Function] Checks the actual value in the field against the expected value
def checkValue(browser, elem, valueExpected):
    warning = browser.find_element(elem[0], elem[1])
    if warning.get_attribute("value") == valueExpected:
        return True
    else:
        return False

