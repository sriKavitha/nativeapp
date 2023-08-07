# [Documentation - Setup] This section lists all dependencies
# that are imported for function file to work
import time, var
from selenium.webdriver import ActionChains

# [Documentation - Summary] This file creates the functions for
# use in the automation test suite of NYL APP

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

 # [Documentation - Function] Webdriver uses actionchains to  wait for a specified page element
# to appear prior to the next interaction on the page   

def waitUntil(browser, elem):
    a = ActionChains(browser)
    try:
        a.move_to_element(browser.find_element(elem[0], elem[1])).perform()
        assert(browser.find_element(elem[0], elem[1]))
    except:
        time.sleep(1)
        try:
            swipeUp(browser, var.NYLregistration.base) 
            assert(browser.find_element(elem[0], elem[1]))
        except:
            swipeUp(browser, var.NYLregistration.base) 
            try:
                a.move_to_element(browser.find_element(elem[0], elem[1])).perform()
                assert(browser.find_element(elem[0], elem[1]))
            except:    
                print("E--" + elem[1] + " elem not found")
                #assert(browser.find_element(elem[0], elem[1]))

# [Documentation - Function] Webdriver waits for a specified page element
# to appear and then proceeds to click on it
def waitAndClick(browser, elem):
    waitUntil(browser, elem)
    browser.find_element(elem[0], elem[1]).click()

def coordinateClick(browser, x, y):
    a = ActionChains(browser)
    base = browser.find_element(var.NYLregistration.base[0], var.NYLregistration.base[1])
    a.move_to_element_with_offset(base, x, y).click().perform()

# [Documentation - Function] Webdriver waits for a specified page element
# to appear and then proceeds to send keys to it
def waitAndSend(browser, elem, keys):
    waitUntil(browser, elem)
    browser.find_element(elem[0], elem[1]).send_keys(keys)

def actionSend(browser, keys):
    a = ActionChains(browser)
    a.send_keys(keys)
    a.perform()

def getList(browser, elem):
    waitUntil(browser, elem)
    ret = browser.find_elements(elem[0], elem[1])
    return(ret)

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

# # [Documentation - Function] Function that calls the script to grab full page UTC timestamped screenshot
# def fullshot(self):
#     self.driver.set_window_position(0, 0)
#     self.driver.maximize_window()
#     timestamp = timeStamp() + '.png'
#     util.fullpage_screenshot(self.driver, timestamp)