# [Documentation - Setup] This section lists all dependencies
# that are imported for this test file to work
from selenium import webdriver  #webdriver module provides all WebDriver implementations
import warnings
import unittest, time, re       #unittest is the testing framework, provides module for organizing test cases
from selenium.webdriver.common.keys import Keys     #Keys class provide keys in the keyboard like RETURN, F1, ALT, etc.
from selenium.webdriver.common.by import By         #By class provides method for finding the page elements by NAME, ID, XPATH, etc.
from selenium.webdriver.support.ui import Select    #Select class provides ability to select items in dropdown
import var, funct, confTest   #Custom class for NYL

# [Documentation - Summary] Marks user for deletion, then purges user from userpool via email search

class NYLadmin(confTest.NYLadminBASE):
    # replace method arg 'self.testemail' to the email of the user destined for deletion
    def test_purgeUser(self, testemail='self.testemail'):
        if testemail == 'self.testemail':
            testemail = self.testemail

        driver = self.driver
        # url is pulled from confTest
        driver.get(self.admin_url)

        # Instructions for webdriver to read and input user data via the info on the .txt doc.
        # Credentials are localized to one instance via the var file
        funct.waitAndSend(driver, var.adminLoginVar.email, var.CREDSadmin.superadmin_username)
        funct.waitAndSend(driver, var.adminLoginVar.password, var.CREDSadmin.superadmin_psw)
        funct.waitAndClick(driver, var.adminLoginVar.signin_button)
        time.sleep(5)
        # Search for test user via Email
        # TODO due to ongoing Admin Dash work in dev env, this if else is in place, will need to update once AD work is complete
        if self.env == 'dev':
            funct.waitAndClick(driver, var.adminDashVar.search_input)
            funct.waitAndSend(driver, var.adminDashVar.search_input, testemail)
        else:
            funct.waitAndClick(driver, var.adminDashVar.search_input)
            funct.waitAndClick(driver, var.adminDashVar.category_email)
            funct.waitAndClick(driver, var.adminDashVar.operator_contains)
            funct.waitAndSend(driver, var.adminDashVar.search_input, testemail)
            driver.find_element_by_xpath(var.adminDashVar.search_input[1]).send_keys(Keys.ENTER)
        time.sleep(2)
        funct.waitAndClick(driver, var.adminDashVar.search_button)
        time.sleep(3)
        # Checks the returned user is the correct user
        source = driver.page_source
        num_returned = source.count(testemail)
        if driver.find_elements_by_xpath(var.adminDashVar.no_data_msg[1]) != []:
            raise Exception("No user found, check user data")
        elif num_returned != 2:
            raise Exception("User not found, check user data")
        else:
            pass
        # Clicks checkbox for first user returned
        funct.waitAndClick(driver, var.adminDashVar.searchedUser_checkbox)
        funct.waitAndClick(driver, var.adminDashVar.bulkAction_button)
        funct.waitAndClick(driver, var.adminDashVar.li_delete)
        # Submits comment and mandatory text for completion
        ts = funct.timeStamp()
        funct.waitAndSend(driver, var.adminDashVar.comment_textarea, "automated test change at " + ts)
        funct.waitAndClick(driver, var.adminDashVar.modal_ok_button)
        funct.waitAndSend(driver, var.adminDashVar.comment_phrase_textarea, "mark for deletion")
        funct.waitAndClick(driver, var.adminDashVar.modal_ok_button)
        time.sleep(5)
        funct.waitAndClick(driver, var.adminDashVar.modal_ok_button)
        # # Navigates to Pending Deletion user list to purge user
        funct.waitAndClick(driver, var.adminDashVar.pendingDeletion_link)
        # Search for test user via Email
        # TODO due to ongoing Admin Dash work in dev env, this if else is in place, will need to update once AD work is complete
        if self.env == 'dev':
            funct.waitAndClick(driver, var.adminDashVar.search_input)
            funct.waitAndSend(driver, var.adminDashVar.search_input, testemail)
        else:
            funct.waitAndClick(driver, var.adminDashVar.search_input)
            funct.waitAndClick(driver, var.adminDashVar.category_email)
            funct.waitAndClick(driver, var.adminDashVar.operator_contains)
            funct.waitAndSend(driver, var.adminDashVar.search_input, testemail)
            driver.find_element_by_xpath(var.adminDashVar.search_input[1]).send_keys(Keys.ENTER)
        time.sleep(2)
        funct.waitAndClick(driver, var.adminDashVar.search_button)
        time.sleep(3)
        # Checks the returned user is the correct user
        source = driver.page_source
        num_returned = source.count(testemail)
        if driver.find_elements_by_xpath(var.adminDashVar.no_data_msg[1]) != []:
            raise Exception("No user found, check user data")
        elif num_returned != 2:
            raise Exception("User not found, check user data")
        else:
            pass
        # Clicks checkbox for first user returned
        funct.waitAndClick(driver, var.adminDashVar.pendingDeleteUser_checkbox)
        funct.waitAndClick(driver, var.adminDashVar.bulkAction_button)
        funct.waitAndClick(driver, var.adminDashVar.li_permDelete)
        # Submits comment and mandatory text for completion
        ts = funct.timeStamp()
        funct.waitAndSend(driver, var.adminDashVar.comment_textarea, "automated test change at " + ts)
        funct.waitAndClick(driver, var.adminDashVar.modal_ok_button)
        funct.waitAndSend(driver, var.adminDashVar.comment_phrase_textarea, "purge")
        funct.waitAndClick(driver, var.adminDashVar.modal_ok_button)
        time.sleep(2)
        funct.waitAndClick(driver, var.adminDashVar.modal_ok_button)
        time.sleep(3)
        # Search for test user via Email again to confirm user is gone from system
        funct.waitAndClick(driver, var.adminDashVar.search_button)
        time.sleep(3)
        if driver.find_elements_by_xpath(var.adminDashVar.no_data_msg[1]) != []:
            print(f"Test user {testemail} found and purged")
        else:
            raise Exception(f"User {testemail} not purged, try again.")

# This file is a helper tool for manual testing, no HTML reporting is necessary
# Boiler plate code to run the test suite
if __name__ == "__main__":
    unittest.main(warnings='ignore')