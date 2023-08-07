import json
import time
import unittest
from urllib.parse import urlparse

import boto3
from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

import util
import var


def purgeSSOemail(self, email):
    """Checks for existing test user email in SSO userpool
    and if found deletes the user through the Admin Dashboard.
    :param self: webdriver instance
    :param email: string of the email that is being removed from SSO User database
    :returns: True if executed without exception
    """
    self.admin_url = 'https://admin-' + self.env + '.nylservices.net/'

    driver = self.driver
    driver.get(self.admin_url)
    testemail = email
    # Instructions for webdriver to read and input user data via the info on the .txt doc.
    # Credentials are localized to one instance via the var file
    try:  #try to login
        waitAndFind(driver, var.adminLoginVar.signin_button)
        waitAndSend(driver, var.adminLoginVar.email, var.CREDSadmin.superadmin_username)
        waitAndSend(driver, var.adminLoginVar.password, var.CREDSadmin.superadmin_psw)
        waitAndClick(driver, var.adminLoginVar.signin_button)
    except Exception:  # if session persists from before, extend session and continue
        time.sleep(2)
        try:
            waitAndFind(driver, var.adminDashVar.extend_button)
            waitAndClick(driver, var.adminDashVar.extend_button)
        except:
            pass    # Search for test user via Email
    time.sleep(2)
    waitAndClick(driver, var.adminDashVar.search_input)
    waitAndSend(driver, var.adminDashVar.search_input, testemail)
    try:
        waitAndClick(driver, var.adminDashVar.search_button)
        time.sleep(1)
        waitAndClick(driver, var.adminDashVar.search_button)
        time.sleep(3)
    except:
        time.sleep(2)
        try:
            waitAndClick(driver, var.adminDashVar.search_button)
        except:
            waitAndClick(driver, var.adminDashVar.search_button)

    time.sleep(3)
    # Checks the returned user is the correct user
    rows = driver.find_elements_by_xpath('//tr[@class="ant-table-row ant-table-row-level-0"]')
    if len(rows) == 1:
        if driver.find_element_by_xpath('//td[@class="ant-table-cell"][4]').text == testemail:  # check that first user returned has the same email address
            # Clicks view/edit button for first user returned, navigates to detail page and clicks delete
            waitAndClick(driver, var.adminDashVar.view_edit_button)
            waitAndClick(driver, var.adminUsersVar.user_status_tab)
            waitAndClick(driver, var.adminUsersVar.delete_button)
            # Submits comment and mandatory text for completion
            ts = timeStamp()
            waitAndSend(driver, var.adminDashVar.comment_textarea, "automated test change at " + ts)
            # attempt to click the modal "OK" buttons to proceed to next step
            # different locator for same button depending on new session or extended session
            try:
                waitAndClick(driver, var.adminDashVar.modal_ok_button)
            except:
                try:
                    waitAndClick(driver, var.adminDashVar.ext2_modal_ok_button)
                except:
                    try:
                        waitAndClick(driver, var.adminDashVar.ext1_modal_ok_button)
                    except:
                        try:
                            waitAndClick(driver, var.adminDashVar.extend_button)
                        except:
                            pass

            waitAndSend(driver, var.adminDashVar.comment_phrase_textarea, "mark for deletion")

            try:
                waitAndClick(driver, var.adminDashVar.modal_ok_button)
            except:
                try:
                    waitAndClick(driver, var.adminDashVar.ext2_modal_ok_button)
                except:
                    try:
                        waitAndClick(driver, var.adminDashVar.ext1_modal_ok_button)
                    except:
                        try:
                            waitAndClick(driver, var.adminDashVar.extend_button)
                        except:
                            pass

            time.sleep(2)
            try:
                waitAndClick(driver, var.adminDashVar.modal_ok_button)
            except:
                try:
                    waitAndClick(driver, var.adminDashVar.ext2_modal_ok_button)
                except:
                    try:
                        waitAndClick(driver, var.adminDashVar.ext1_modal_ok_button)
                    except:
                        try:
                            waitAndClick(driver, var.adminDashVar.extend_button)
                        except:
                            pass

            # # Navigates to Pending Deletion user list to purge user
            waitAndClick(driver, var.adminDashVar.pendingDeletion_link)
            time.sleep(2)
            # Search for test user via Email
            waitAndClick(driver, var.adminDashVar.search_input)
            waitAndSend(driver, var.adminDashVar.search_input, testemail)
            waitAndClick(driver, var.adminDashVar.search_button)
            time.sleep(1)
            waitAndClick(driver, var.adminDashVar.search_button)
            time.sleep(3)

            # Checks the returned user is the correct user
            rows = driver.find_elements_by_xpath('//tr[@class="ant-table-row ant-table-row-level-0"]')
            if len(rows) == 1:
                if driver.find_element_by_xpath('//td[@class="ant-table-cell"][4]').text == testemail:  # check that first user returned is has the same email address
                    # Clicks view/edit button for first user returned, navigates to detail page and clicks delete
                    waitAndClick(driver, var.adminDashVar.view_edit_button)
                    waitAndClick(driver, var.adminPendingDeletionVar.user_status_tab)
                    waitAndClick(driver, var.adminPendingDeletionVar.permanently_delete_button)
                    # Submits comment and mandatory text for completion
                    ts = timeStamp()
                    waitAndSend(driver, var.adminDashVar.comment_textarea, "automated test change at " + ts)
                    try:
                        waitAndClick(driver, var.adminDashVar.modal_ok_button)
                    except:
                        try:
                            waitAndClick(driver, var.adminDashVar.ext2_modal_ok_button)
                        except:
                            try:
                                waitAndClick(driver, var.adminDashVar.ext1_modal_ok_button)
                            except:
                                try:
                                    waitAndClick(driver, var.adminDashVar.extend_button)
                                except:
                                    pass

                    waitAndSend(driver, var.adminDashVar.comment_phrase_textarea, "purge")

                    try:
                        waitAndClick(driver, var.adminDashVar.modal_ok_button)
                    except:
                        try:
                            waitAndClick(driver, var.adminDashVar.ext2_modal_ok_button)
                        except:
                            try:
                                waitAndClick(driver, var.adminDashVar.ext1_modal_ok_button)
                            except:
                                try:
                                    waitAndClick(driver, var.adminDashVar.extend_button)
                                except:
                                    pass

                    time.sleep(2)
                    try:
                        waitAndClick(driver, var.adminDashVar.modal_ok_button)
                    except:
                        try:
                            waitAndClick(driver, var.adminDashVar.ext2_modal_ok_button)
                        except:
                            try:
                                waitAndClick(driver, var.adminDashVar.ext1_modal_ok_button)
                            except:
                                try:
                                    waitAndClick(driver, var.adminDashVar.extend_button)
                                except:
                                    pass

                    time.sleep(3)
                    # Search for test user via Email again to confirm user is gone from system
                    waitAndClick(driver, var.adminDashVar.users_link)
                    waitAndClick(driver, var.adminDashVar.search_input)
                    waitAndSend(driver, var.adminDashVar.search_input, testemail)
                    try:
                        waitAndClick(driver, var.adminDashVar.search_button)
                        time.sleep(1)
                        waitAndClick(driver, var.adminDashVar.search_button)
                        time.sleep(3)
                    except:
                        time.sleep(2)
                        try:
                            waitAndClick(driver, var.adminDashVar.search_button)
                        except:
                            waitAndClick(driver, var.adminDashVar.search_button)

                    time.sleep(3)
                    rows = driver.find_elements_by_xpath('//tr[@class="ant-table-row ant-table-row-level-0"]')
                    if driver.find_elements_by_xpath(var.adminDashVar.no_data_msg[1]) != []:  # search returns no data
                        print(f'\ntest user {testemail} found and purged')
                    elif len(rows) >= 1:  # search returns list of users
                        fullshot(driver)
                        print(f'\nuser still in Pending Deletion list with {testemail}, check user pool')
                        raise Exception
                    else:
                        print(f'\nunexpected behavior: please check screenshot')
                        fullshot(driver)
                        raise Exception
                else:
                    print(f'unexpected behavior: please check screenshot')
                    fullshot(driver)
                    raise Exception
            elif len(rows) >= 2:  # more than 1 user was returned in table
                fullshot(driver)
                print(f'More than 1 user found in Pending Deletion list, check screenshot')
                raise Exception
            elif driver.find_elements_by_xpath(var.adminDashVar.no_data_msg[1]) != []:  # no user returned in table
                print(f'no test user {testemail} found')
                # open new window with execute_script()
                driver.execute_script("window.open('');")
                closeWindow(driver, 'New York Lottery - Admin Dashboard')
                exit()
            else:
                print(f'unexpected behavior: please check screenshot')
                fullshot(driver)
        else:
            print(f'\nunexpected behavior: please check screenshot')
            fullshot(driver)
    elif len(rows) >= 2:  # more than 1 user was returned in table
        fullshot(driver)
        print(f'\nMore than 1 user found in table, check screenshot')
        raise Exception
    elif driver.find_elements_by_xpath(var.adminDashVar.no_data_msg[1]) != []:  # no user returned in table
        print(f'\nno test user {testemail} found')
        # open new window with execute_script()
        driver.execute_script("window.open('');")
        closeWindow(driver, 'New York Lottery - Admin Dashboard')
    else:
        print(f'\nunexpected behavior: please check screenshot')
        fullshot(driver)

def purgeSSOphone(self, phone):
    """Checks for existing test user phone in SSO userpool
    and if found deletes the user through the Admin Dashboard.
    :param self: webdriver instance
    :param phone: 10 digit phone number that is being removed from SSO User database
    type phone: str
    :returns: True if executed without exception
    """
    self.admin_url = 'https://admin-' + self.env + '.nylservices.net/'

    driver = self.driver
    driver.get(self.admin_url)
    testphone = phone
    # match the formatiing in the returned users table: +1 (407) 348-7541
    formatted_phone = '+1 (' + testphone[:3] + ') ' + testphone[3:6] + '-' + testphone[6:]
    # Instructions for webdriver to read and input user data via the info on the .txt doc.
    # Credentials are localized to one instance via the var file
    try:  #try to login
        waitAndFind(driver, var.adminLoginVar.signin_button)
        waitAndSend(driver, var.adminLoginVar.email, var.CREDSadmin.superadmin_username)
        waitAndSend(driver, var.adminLoginVar.password, var.CREDSadmin.superadmin_psw)
        waitAndClick(driver, var.adminLoginVar.signin_button)
    except Exception:  # if session persists from before, extend session and continue
        time.sleep(2)
        try:
            waitAndFind(driver, var.adminDashVar.extend_button)
            waitAndClick(driver, var.adminDashVar.extend_button)
        except:
            pass
    # Search for test user via phone
    time.sleep(2)
    waitAndClick(driver, var.adminDashVar.search_input)
    waitAndSend(driver, var.adminDashVar.search_input, testphone)
    try:
        waitAndClick(driver, var.adminDashVar.search_button)
        time.sleep(1)
        waitAndClick(driver, var.adminDashVar.search_button)
        time.sleep(3)
    except:
        time.sleep(2)
        try:
            waitAndClick(driver, var.adminDashVar.search_button)
        except:
            waitAndClick(driver, var.adminDashVar.search_button)

    time.sleep(3)
    # Checks the returned user is the correct user
    rows = driver.find_elements_by_xpath('//tr[@class="ant-table-row ant-table-row-level-0"]')
    if len(rows) == 1:
        if driver.find_element_by_xpath('//td[@class="ant-table-cell"][6]').text == formatted_phone:  # check that first user returned has the same phone
            # Clicks view/edit button for first user returned
            # TODO remove bulk action button deletion
            # waitAndClick(driver, var.adminDashVar.searchedUser_checkbox)
            # waitAndClick(driver, var.adminDashVar.bulkAction_button)
            # waitAndClick(driver, var.adminDashVar.li_delete)
            waitAndClick(driver, var.adminDashVar.view_edit_button)
            waitAndClick(driver, var.adminUsersVar.user_status_tab)
            waitAndClick(driver, var.adminUsersVar.delete_button)
            # Submits comment and mandatory text for completion
            ts = timeStamp()
            waitAndSend(driver, var.adminDashVar.comment_textarea, "automated test change at " + ts)
            # attempt to click the modal "OK" buttons to proceed to next step
            # different locator for same button depending on new session or extended session
            try:
                waitAndClick(driver, var.adminDashVar.modal_ok_button)
            except:
                try:
                    waitAndClick(driver, var.adminDashVar.ext2_modal_ok_button)
                except:
                    try:
                        waitAndClick(driver, var.adminDashVar.ext1_modal_ok_button)
                    except:
                        try:
                            waitAndClick(driver, var.adminDashVar.extend_button)
                        except:
                            pass

            waitAndSend(driver, var.adminDashVar.comment_phrase_textarea, "mark for deletion")

            try:
                waitAndClick(driver, var.adminDashVar.modal_ok_button)
            except:
                try:
                    waitAndClick(driver, var.adminDashVar.ext2_modal_ok_button)
                except:
                    try:
                        waitAndClick(driver, var.adminDashVar.ext1_modal_ok_button)
                    except:
                        try:
                            waitAndClick(driver, var.adminDashVar.extend_button)
                        except:
                            pass

            time.sleep(2)
            try:
                waitAndClick(driver, var.adminDashVar.modal_ok_button)
            except:
                try:
                    waitAndClick(driver, var.adminDashVar.ext2_modal_ok_button)
                except:
                    try:
                        waitAndClick(driver, var.adminDashVar.ext1_modal_ok_button)
                    except:
                        try:
                            waitAndClick(driver, var.adminDashVar.extend_button)
                        except:
                            pass

            # # Navigates to Pending Deletion user list to purge user
            waitAndClick(driver, var.adminDashVar.pendingDeletion_link)
            time.sleep(2)
            # Search for test user via Phone number
            waitAndClick(driver, var.adminDashVar.search_input)
            waitAndSend(driver, var.adminDashVar.search_input, testphone)
            waitAndClick(driver, var.adminDashVar.search_button)
            time.sleep(1)
            waitAndClick(driver, var.adminDashVar.search_button)
            time.sleep(3)

            # Checks the returned user is the correct user
            rows = driver.find_elements_by_xpath('//tr[@class="ant-table-row ant-table-row-level-0"]')
            if len(rows) == 1:
                if driver.find_element_by_xpath('//td[@class="ant-table-cell"][6]').text == formatted_phone:  # check that first user returned has the same phone
                    # Clicks view/edit button for first user returned
                    # TODO remove bulk action button deletion
                    # waitAndClick(driver, var.adminDashVar.pendingDeleteUser_checkbox)
                    # waitAndClick(driver, var.adminDashVar.bulkAction_button)
                    # waitAndClick(driver, var.adminDashVar.li_permDelete)
                    waitAndClick(driver, var.adminDashVar.view_edit_button)
                    waitAndClick(driver, var.adminPendingDeletionVar.user_status_tab)
                    waitAndClick(driver, var.adminPendingDeletionVar.permanently_delete_button)
                    # Submits comment and mandatory text for completion
                    ts = timeStamp()
                    waitAndSend(driver, var.adminDashVar.comment_textarea, "automated test change at " + ts)
                    try:
                        waitAndClick(driver, var.adminDashVar.modal_ok_button)
                    except:
                        try:
                            waitAndClick(driver, var.adminDashVar.ext2_modal_ok_button)
                        except:
                            try:
                                waitAndClick(driver, var.adminDashVar.ext1_modal_ok_button)
                            except:
                                try:
                                    waitAndClick(driver, var.adminDashVar.extend_button)
                                except:
                                    pass

                    waitAndSend(driver, var.adminDashVar.comment_phrase_textarea, "purge")

                    try:
                        waitAndClick(driver, var.adminDashVar.modal_ok_button)
                    except:
                        try:
                            waitAndClick(driver, var.adminDashVar.ext2_modal_ok_button)
                        except:
                            try:
                                waitAndClick(driver, var.adminDashVar.ext1_modal_ok_button)
                            except:
                                try:
                                    waitAndClick(driver, var.adminDashVar.extend_button)
                                except:
                                    pass

                    time.sleep(2)
                    try:
                        waitAndClick(driver, var.adminDashVar.modal_ok_button)
                    except:
                        try:
                            waitAndClick(driver, var.adminDashVar.ext2_modal_ok_button)
                        except:
                            try:
                                waitAndClick(driver, var.adminDashVar.ext1_modal_ok_button)
                            except:
                                try:
                                    waitAndClick(driver, var.adminDashVar.extend_button)
                                except:
                                    pass

                    time.sleep(3)
                    # Search for test user via Phone again to confirm user is gone from system
                    waitAndClick(driver, var.adminDashVar.users_link)
                    waitAndClick(driver, var.adminDashVar.search_input)
                    waitAndSend(driver, var.adminDashVar.search_input, testphone)
                    try:
                        waitAndClick(driver, var.adminDashVar.search_button)
                        time.sleep(1)
                        waitAndClick(driver, var.adminDashVar.search_button)
                        time.sleep(3)
                    except:
                        time.sleep(2)
                        try:
                            waitAndClick(driver, var.adminDashVar.search_button)
                        except:
                            waitAndClick(driver, var.adminDashVar.search_button)

                    time.sleep(3)
                    rows = driver.find_elements_by_xpath('//tr[@class="ant-table-row ant-table-row-level-0"]')
                    if driver.find_elements_by_xpath(var.adminDashVar.no_data_msg[1]) != []:  # search returns no data
                        print(f'\ntest user {formatted_phone} found and purged')
                    elif len(rows) >= 1:  # search returns list of users
                        fullshot(driver)
                        print(f'\nuser still in Pending Deletion list with {formatted_phone}, check user pool')
                        raise Exception
                    else:
                        print(f'\nunexpected behavior: please check screenshot')
                        fullshot(driver)
                        raise Exception
                else:
                    print(f'unexpected behavior: please check screenshot')
                    fullshot(driver)
                    raise Exception
            elif len(rows) >= 2:  # more than 1 user was returned in table
                fullshot(driver)
                print(f'More than 1 user found in Pending Deletion list, check screenshot')
                raise Exception
            elif driver.find_elements_by_xpath(var.adminDashVar.no_data_msg[1]) != []:  # no user returned in table
                print(f'test user {formatted_phone} NOT found on Pending Deletion list')
                # open new window with execute_script()
                driver.execute_script("window.open('');")
                closeWindow(driver, 'New York Lottery - Admin Dashboard')
                exit()
            else:
                print(f'unexpected behavior: please check screenshot')
                fullshot(driver)
        else:
            print(f'\nunexpected behavior: please check screenshot')
            fullshot(driver)
    elif len(rows) >= 2:  # more than 1 user was returned in table
        fullshot(driver)
        print(f'\nMore than 1 user returned in table, check screenshot')
        raise Exception
    elif driver.find_elements_by_xpath(var.adminDashVar.no_data_msg[1]) != []:  # no user returned in table
        print(f'\nno test user {formatted_phone} found')
        # open new window with execute_script()
        driver.execute_script("window.open('');")
        closeWindow(driver, 'New York Lottery - Admin Dashboard')
    else:
        print(f'\nunexpected behavior: please check screenshot')
        fullshot(driver)
    return True

# [Documentation - Function] Checks for existing test user in Mobile App userpool and deletes the user if found.
def purgeMobile(self, email):
    """Checks for existing test user email in Mobile App userpool
    and if found deletes the user through the AWS tool.
    :param self: webdriver instance
    :param email: email that is being removed from SSO User database
    type email: str
    :returns: True if executed without exception
    """
    if self.env == 'dev':
        userpool = 'us-east-1_OSdCjCmwo'
    elif self.env == 'qa':
        userpool = 'us-east-1_Fwp84k69u'
    elif self.env == 'stage':
        userpool = 'us-east-1_hG2UobNyZ'
    client = boto3.client('cognito-idp')
    # print(userpool)
    testemail = 'email ="' + str(email) + '"'
    response = client.list_users(
        UserPoolId=userpool,
        AttributesToGet=[
            'email',
        ],
        Limit=30,
        Filter=testemail
    )
    # print(response)
    testUser = response['Users'][0]['Username']
    response2 = client.admin_delete_user(
        UserPoolId=userpool,
        Username=testUser
    )
    # print(response2)
    return True

def getCredential(list, target):
    """Uses a filtering method to more easily get and maintain credentials from the credential page
    (which is now localized to one instance via the var page). The target should be given plainly, without colons.
    :param list: list of the lines of text in the credentials file
    :param target: credential that is being pulled from the txt file
    :returns: string of the target credential
    """
    targ = str(target + ': ')
    credential = [item for item in list if item.startswith(targ)][0]
    cred = credential.replace(targ, '')
    return cred

def generateHAR(server, driver):
    """starts a browsermob proxy and generates a har file of current page
    :param server: proxy server
    :param driver: webdriver instance
    :returns: har file of network activity
    """
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

def waitUntil(browser, elem):
    """Webdriver uses actionchains to  wait for a specified page element
    :param browser: Webdriver instance
    :param elem: the element that is being searched,
    a list with the following index elem[0] = search method, elem[1] = locator, elem[2] = name of element
    """
    a = ActionChains(browser)
    try:
        a.move_to_element(browser.find_element(elem[0], elem[1])).perform()
        assert(browser.find_element(elem[0], elem[1]))
        return True
    except:
        time.sleep(5)
        try:
            a.move_to_element(browser.find_element(elem[0], elem[1])).perform()
            assert(browser.find_element(elem[0], elem[1]))
            return True
        except:
            print("E--" + elem[2] + " elem not found")
            return False

def waitUntilNot(browser, elem):
    """Webdriver uses actionchains to  wait for a specified page element
    :param browser: Webdriver instance
    :param elem: the element that is being searched,
    a list with the following index elem[0] = search method, elem[1] = locator, elem[2] = name of element
    """
    a = ActionChains(browser)
    x = 0
    elem = browser.find_element(elem[0], elem[1])
    while elem == True:
        if x < 10:
            time.sleep(1)
            x = x + 1

def waitAndGetText(browser, elem):
    """Function that is used to get text
    :returns: string the text of the element
    """
    waitUntil(browser, elem)
    return browser.find_element(elem[0], elem[1]).text

def waitAndFind(browser, elem):
    """Webdriver uses actionchains to  wait for a specified page element without throwing an error message
    :param browser: Webdriver instance
    :param elem: the element that is being searched,
    a list with the following index elem[0] = search method, elem[1] = locator, elem[2] = name of element
    """
    a = ActionChains(browser)
    try:
        a.move_to_element(browser.find_element(elem[0], elem[1])).perform()
        assert(browser.find_element(elem[0], elem[1]))
    except:
        time.sleep(2)
        a.move_to_element(browser.find_element(elem[0], elem[1])).perform()
        assert(browser.find_element(elem[0], elem[1]))

def waitAndClick(browser, elem):
    """Webdriver uses actionchains to  wait for a specified page element to appear and then proceeds to click on it
    :param browser: Webdriver instance
    :param elem: the element that is being searched,
    a list with the following index elem[0] = search method, elem[1] = locator, elem[2] = name of element
    """
    waitUntil(browser, elem)
    browser.find_element(elem[0], elem[1]).click()

# [Documentation - Function] Webdriver waits for a specified page element
# to appear and then proceeds to send keys to it
def waitAndSend(browser, elem, keys):
    """Webdriver uses actionchains to  wait for a specified page element to appear and then proceeds to click on it
    :param browser: Webdriver instance
    :param elem: the element that is being searched,
    a list with the following index elem[0] = search method, elem[1] = locator, elem[2] = name of element
    :param keys: keys or combination of keys that would be entered via keyboard
    """
    waitUntil(browser, elem)
    browser.find_element(elem[0], elem[1]).send_keys(keys)

def clearTextField(browser, elem):
    """Searches for the elem and clears all the field
    :param browser: Webdriver instance
    :param elem: the element that is being searched,
    a list with the following index elem[0] = search method, elem[1] = locator, elem[2] = name of element
    """
    waitUntil(browser, elem)
    browser.find_element(elem[0], elem[1]).clear()

def timeStamp():
    """Function that grabs UTC time and converts to human readable format
    :returns: string of the timestamp
    """
    ts = time.gmtime()
    times = time.strftime("%Y-%m-%d_%H-%M-%S", ts)
    return times

def checkText(browser, elem, stub):
    """Checks the text of a given element against a given stub
    :param browser: Webdriver instance
    :param elem: the element that is being searched,
    a list with the following index elem[0] = search method, elem[1] = locator, elem[2] = name of element
    :param stub: the spec text that is verified against
    """
    waitUntil(browser, elem)
    el = browser.find_element(elem[0], elem[1])
    if el.text == stub:
        assert el.text == stub
    else:
        print('E---Text Incorrect!\n\nExpected text: "' + stub + '"\n\n but text was: "' + el.text + '"')
        assert el.text == stub

# [Documentation - Function] Function that calls the script to grab full page UTC timestamped screenshot
def fullshot(browser):
    """Calls the script to grab full page UTC timestamped screenshot
    :param browser: Webdriver instance
    """
    browser.set_window_position(0, 0)
    browser.maximize_window()
    timestamp = timeStamp() + '.png'
    util.fullpage_screenshot(browser, timestamp)


def checkError(browser, elemWarning):
    """"Checks that an error exists
    :param browser: Webdriver instance
    :param elemWarning: the element that is being searched,
    a list with the following index elem[0] = search method, elem[1] = locator, elem[2] = name of element
    """
    try:
        browser.find_element(elemWarning[0], elemWarning[1])
        return True
    except:
        return False

def checkErrorText(browser, elemWarning, elemWarningStub):
    """Checks the actual warning text against the reported warning copy and returns a True/False
    :param browser: Webdriver instance
    :param elemWarning: the element that is being searched,
    a list with the following index elem[0] = search method, elem[1] = locator, elem[2] = name of element
    :param elemWarningStub: the spec text that is verified against
    :returns: True when error message matches and False when not
    """
    warning = browser.find_element(elemWarning[0], elemWarning[1])
    if warning.get_attribute("innerText") == elemWarningStub:
        return True
    else:
        return False

def verifyErrorText(browser, elemWarning, elemWarningStub):
    """Checks the actual warning text against the reported warning copy and raises an exception if it does not match
    :param browser: Webdriver instance
    :param elemWarning: the element that is being searched,
    a list with the following index elem[0] = search method, elem[1] = locator, elem[2] = name of element
    :param elemWarningStub: the spec text that is verified against
    """
    warning = browser.find_element(elemWarning[0], elemWarning[1])
    if warning.get_attribute("innerText") == elemWarningStub:
        pass
    else:
        print('FAIL - Warning should say "' + elemWarningStub + '" , but says "' + warning.get_attribute("innerText") + '"!')
        raise Exception('Error warning(s) copy is incorrect')

def checkValue(browser, elem, valueExpected):
    """Checks the actual value in the field against the expected value
    :param browser: Webdriver instance
    :param elemWarning: the element that is being searched,
    a list with the following index elem[0] = search method, elem[1] = locator, elem[2] = name of element
    :param valueExpected: the value attribute of the element
    """
    warning = browser.find_element(elem[0], elem[1])
    if warning.get_attribute("value") == valueExpected:
        return True
    else:
        return False

def createVerifiedUser(self, email):
    """
    Creates a verified user via submission of SSN4 and OTP. User has the following flags:
    custom:ssn_verification	"Y"
    custom:phone_verification	"Y"
    custom:gov_id_verification	"X"
    custom:verified	"Y"
    :param self: Webdriver instance
    :param email: email address of the new user
    """
    # Check for existing test user and wipe it from userpool prior to test execution
    try:
        purgeSSOemail(self, email)
        if self.env != 'dev':
            try:
                purgeSSOphone(self, var.credsSSOWEB.phone)
            except:
                pass
    except:
        if self.env != 'dev':
            try:
                purgeSSOphone(self, var.credsSSOWEB.phone)
            except:
                pass
    driver = self.driver
    driver.get(self.reg_url)
    # Instructions for webdriver to read and input user data via the info on the .txt doc.
    # Credentials are localized to one instance via the var file
    waitAndSend(driver, var.regV.fname, var.credsSSOWEB.fname)
    waitAndSend(driver, var.regV.lname, var.credsSSOWEB.lname)
    waitAndSend(driver, var.regV.housenum, var.credsSSOWEB.housenum)
    waitAndSend(driver, var.regV.street, var.credsSSOWEB.street)
    waitAndSend(driver, var.regV.city, var.credsSSOWEB.city)
    # Find and select the state according to the info in the .txt doc
    # Uses a for loop to iterate through the list of states until element
    # matches the entry info in the text file. Then clicks the element found.
    select_box = driver.find_element_by_name("state")
    waitAndClick(driver, var.regV.state_dropdown)
    options = [x for x in select_box.find_elements_by_tag_name("option")]
    for element in options:
        if element.text in var.credsSSOWEB.state:
            element.click()
            break
    waitAndSend(driver, var.regV.zip, var.credsSSOWEB.zip)
    waitAndSend(driver, var.regV.phone, var.credsSSOWEB.phone)
    waitAndSend(driver, var.regV.ssn4, var.credsSSOWEB.ssn4)
    waitAndSend(driver, var.regV.dob, (
            var.credsSSOWEB.dob_month + var.credsSSOWEB.dob_date + var.credsSSOWEB.dob_year))
    waitAndClick(driver, var.regV.dob_check)
    waitAndSend(driver, var.regV.email, email)
    waitAndSend(driver, var.regV.password, var.credsSSOWEB.password)
    waitAndSend(driver, var.regV.confirmPsw, var.credsSSOWEB.password)
    waitAndClick(driver, var.regV.tos_check)
    waitAndClick(driver, var.regV.submit_button)
    # 2nd screen. OTP selection screen
    waitAndClick(driver, var.otpV.text_button)
    # 3rd screen. OTP code entry screen
    time.sleep(5)
    waitAndSend(driver, var.otpV.otp_input, "111111")
    waitAndClick(driver, var.otpV.otp_continue_button)
    # 4th screen. Successful registration should redirect to Google.com.
    # Checking that the search field on google.com is present on page.
    if driver.find_elements_by_name("q") != []:
        print('Verified user registration is successful.')
        # open new window with execute_script()
        driver.execute_script("window.open('');")
        closeWindow(driver, 'New York Lottery - Single Sign On')
    else:
        fullshot(driver)
        print('FAIL - User registration redirect screen not reached. Test can not proceed')
        raise Exception('Registration redirected incorrectly')

def createUnverifiedUser(self, email):
    """
    Creates a UNverified user via selecting govid verification process, failing OTP and skippiing image upload.
    User has the following flags:
    custom:ssn_verification	"N"
    custom:phone_verification	"N"
    custom:gov_id_verification	"-"
    custom:verified	"N"
    :param self: Webdriver instance
    :param email: email address of the new user
    """
    # Check for existing test user and wipe it from userpool prior to test execution
    try:
        purgeSSOemail(self, email)
        if self.env != 'dev':
            try:
                purgeSSOphone(self, var.credsSSOWEB.phone)
            except:
                pass
    except:
        if self.env != 'dev':
            try:
                purgeSSOphone(self, var.credsSSOWEB.phone)
            except:
                pass
    driver = self.driver
    driver.get(self.reg_url)
    # Instructions for webdriver to read and input user data via the info on the .txt doc.
    # Credentials are localized to one instance via the var file
    waitAndSend(driver, var.regV.fname, var.credsSSOWEB.fname)
    waitAndSend(driver, var.regV.lname, var.credsSSOWEB.lname)
    waitAndSend(driver, var.regV.housenum, var.credsSSOWEB.housenum)
    waitAndSend(driver, var.regV.street, var.credsSSOWEB.street)
    waitAndSend(driver, var.regV.city, var.credsSSOWEB.city)
    # Find and select the state according to the info in the .txt doc
    # Uses a for loop to iterate through the list of states until element
    # matches the entry info in the text file. Then clicks the element found.
    select_box = driver.find_element_by_name("state")
    waitAndClick(driver, var.regV.state_dropdown)
    options = [x for x in select_box.find_elements_by_tag_name("option")]
    for element in options:
        if element.text in var.credsSSOWEB.state:
            element.click()
            break
    waitAndSend(driver, var.regV.zip, var.credsSSOWEB.zip)
    waitAndSend(driver, var.regV.phone, var.credsSSOWEB.phone)
    waitAndClick(driver, var.regV.ss_check)         # selects Gov id check box
    waitAndSend(driver, var.regV.dob, (
            var.credsSSOWEB.dob_month + var.credsSSOWEB.dob_date + var.credsSSOWEB.dob_year))
    waitAndClick(driver, var.regV.dob_check)
    waitAndSend(driver, var.regV.email, email)
    waitAndSend(driver, var.regV.password, var.credsSSOWEB.password)
    waitAndSend(driver, var.regV.confirmPsw, var.credsSSOWEB.password)
    waitAndClick(driver, var.regV.tos_check)
    waitAndClick(driver, var.regV.submit_button)
    # 2nd screen. OTP selection screen
    waitAndClick(driver, var.otpV.text_button)
    # 3rd screen. OTP code entry screen. Submits bad OTP code to fail phone verification
    time.sleep(7)
    waitAndSend(driver, var.otpV.otp_input, "987654")
    waitAndClick(driver, var.otpV.otp_continue_button)
    # 4th screen. Unsuccessful registration should redirect to "Sorry, identity cannot be verified" screen.
    time.sleep(5)
    if driver.find_elements_by_class_name("migration-failed-body") != []:
        print(f"Unverified user account {email} successfully created.")
        return True
    elif driver.find_elements_by_name("q") != []:
        print("Reached successful registration. Attempting to create unverified user again")
        return False
    elif "Confirm your details" in driver.find_element_by_tag_name('body').text:
        print("Neither Identity verification failed screen nor Registration successful screen reached.")
        return False
    else:
        print("Unexpected screen reached when attempting to create unverified user. See screenshot.")
        fullshot(driver)
        return False

def closeWindow(driver, title):
    """ Checks all open tabs in the window and closes the tab with the passed in title
    :param driver: Webdriver instance
    :param title: the title of the webpage that is meant to be closed
    """
    # return all handles value of open browser window
    handles = driver.window_handles

    for i in handles:
        driver.switch_to.window(i)

        # close specified web page
        if driver.title == title:
            time.sleep(2)
            driver.close()

def verifyRedirect(self, browser, email, elem):
    """ Asserts whether an expected elem on a redirected screen is found.
    :param self: Selenium instance
    :param browser: Webdriver instance
    :param email: email of the user that is under test, passed to purge function to clean up test
    :param elem: an element found on the redirected page,
    a list with the following index elem[0] = search method, elem[1] = locator, elem[2] = name of element
    """
    verification = waitUntil(browser, elem)
    if verification == True:
        print(f"\nPASS - Redirected successfully.\n")
    elif verification == False:
            print(f"\nFAIL - Redirect screen not reached.\n")
            fullshot(browser)
            purgeSSOemail(self, email)
            raise Exception('Redirected incorrectly. Check screenshot.')
    else:
        fullshot(browser)
        purgeSSOemail(self, email)
        raise Exception('Unexpected behavior. Check screenshot.')

def aws_login(self):
    print("\nLogin attempt into AWS")
    driver = self.driver
    print('----------')
    # switch to AWS login page
    driver.get(self.aws_login_url)
    # Login AWS attempt
    clearTextField(driver, var.loginAWS.aws_acctId)
    waitAndSend(driver, var.loginAWS.aws_acctId, var.CREDSaws.aws_acctId)
    waitAndSend(driver, var.loginAWS.aws_email, var.CREDSaws.aws_email)
    waitAndSend(driver, var.loginAWS.aws_password, var.CREDSaws.aws_password)
    waitAndClick(driver, var.loginAWS.aws_signin_button)
    time.sleep(2)

def sso_register_customEmail(self):
    """
        Register the user with timestamp in the email address in %Y-%m-%d_%H%M_%S format
        ex: qa+sso2022-12-01_140433@rosedigital.co
    """

    # Get the local time and convert into timestamp
    driver = self.driver
    testenv = self.env
    ts = time.localtime()
    timeUserCreated = time.strftime("%Y-%m-%d %H:%M:%S", ts)
    temp_time = timeUserCreated.replace(":","")
    temp_time = temp_time.replace(" ","_")
    # Register the user with the email format: qa+sso+timeUserCreated+@rosedigital.co
    email = 'qa+sso' + str(temp_time) + '@rosedigital.co'
    # creates a verified user with valid SSN4
    print('Registering a SSO user with the email...' + email)
    createVerifiedUser(self, email)
    return email, testenv