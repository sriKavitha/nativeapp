import unittest, time, re       #unittest is the testing framework, provides module for organizing test cases
from selenium.webdriver.common.keys import Keys     #Keys class provide keys in the keyboard like RETURN, F1, ALT, etc.
import var, funct, util, confTest, HtmlTestRunner   #Custom class for NYL

class NYlotto(confTest.NYlottoBASE):

    def test_01_regDupeEmail(self):
        """Tests that a User cannot register with a duplicate Phone.

        Jira test ticket - https://rosedigital.atlassian.net/browse/NYL-1923
        Creates a new verified user with testemail. Opens a new page and attempts to register again
        with the same email and a different phone number(tempphone).
        :return:
        """

        testenv = self.env
        print("TESTING " + testenv + " ENVIRONMENT")
        print("\nChecks for failed registration with duplicate email in userpool")
        testemail = self.testemail
        tempphone = self.tempphone
        formatted_tempphone = '(' + tempphone[:3] + ') ' + tempphone[3:6] + '-' + tempphone[6:]

        driver = self.driver
        print('\n----------\n' + 'Test setup')
        # find and purge temp phone if in userpool
        funct.purgeSSOphone(self, tempphone)
        # creates a verified user with valid SSN4
        funct.createVerifiedUser(self, testemail)
        # edits the created user to a different phone number. so the system will only check the dupe email response
        self.admin_url = f'https://admin-{self.env}.nylservices.net/'
        driver.get(self.admin_url)
        try:  # try to login
            funct.waitAndFind(driver, var.adminLoginVar.signin_button)
            funct.waitAndSend(driver, var.adminLoginVar.email, var.CREDSadmin.superadmin_username)
            funct.waitAndSend(driver, var.adminLoginVar.password, var.CREDSadmin.superadmin_psw)
            funct.waitAndClick(driver, var.adminLoginVar.signin_button)
        except Exception:  # if session persists from before, extend session and continue
            time.sleep(2)
            try:
                funct.waitAndFind(driver, var.adminDashVar.extend_button)
                funct.waitAndClick(driver, var.adminDashVar.extend_button)
            except:
                pass  # Search for test user via Email
        time.sleep(2)
        funct.waitAndClick(driver, var.adminDashVar.search_input)
        funct.waitAndSend(driver, var.adminDashVar.search_input, testemail)
        try:
            funct.waitAndClick(driver, var.adminDashVar.search_button)
            time.sleep(1)
            funct.waitAndClick(driver, var.adminDashVar.search_button)
            time.sleep(3)
        except:
            time.sleep(2)
            try:
                funct.waitAndClick(driver, var.adminDashVar.search_button)
            except:
                funct.waitAndClick(driver, var.adminDashVar.search_button)

        time.sleep(3)
        # Checks the returned user is the correct user
        rows = driver.find_elements_by_xpath('//tr[@class="ant-table-row ant-table-row-level-0"]')
        if len(rows) == 1:
            if driver.find_element_by_xpath(
                '//td[@class="ant-table-cell"][4]').text == testemail:  # check that first user returned has the same email address
                funct.waitAndClick(driver, var.adminDashVar.view_edit_button)    # Clicks the View/Edit link
                funct.waitAndClick(driver, var.adminUsersVar.edit_button)    # Clicks the Edit info button
                # funct.clearTextField(driver, var.adminDashVar.phone_input)
                driver.find_element_by_xpath('//*[@id="phone"]').send_keys("" + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE)
                funct.waitAndSend(driver, var.adminUsersVar.phone_input, formatted_tempphone)
                funct.waitAndClick(driver, var.adminUsersVar.save_button)
                # attempt to click the modal "OK" buttons to proceed to next step
                # different locator for same button depending on new session or extended session
                try:
                    funct.waitAndClick(driver, var.adminDashVar.modal_ok_button)
                except:
                    try:
                        funct.waitAndClick(driver, var.adminDashVar.ext2_modal_ok_button)
                    except:
                        try:
                            funct.waitAndClick(driver, var.adminDashVar.ext1_modal_ok_button)
                        except:
                            try:
                                funct.waitAndClick(driver, var.adminDashVar.extend_button)
                            except:
                                pass

                funct.waitAndSend(driver, var.adminDashVar.comment_phrase_textarea, "edit user")

                try:
                    funct.waitAndClick(driver, var.adminDashVar.modal_ok_button)
                except:
                    try:
                        funct.waitAndClick(driver, var.adminDashVar.ext2_modal_ok_button)
                    except:
                        try:
                            funct.waitAndClick(driver, var.adminDashVar.ext1_modal_ok_button)
                        except:
                            try:
                                funct.waitAndClick(driver, var.adminDashVar.extend_button)
                            except:
                                pass

                try:
                    funct.waitAndClick(driver, var.adminDashVar.modal_ok_button)
                except:
                    try:
                        funct.waitAndClick(driver, var.adminDashVar.ext2_modal_ok_button)
                    except:
                        try:
                            funct.waitAndClick(driver, var.adminDashVar.ext1_modal_ok_button)
                        except:
                            try:
                                funct.waitAndClick(driver, var.adminDashVar.extend_button)
                            except:
                                pass
        print('----------')


        # Switch to blank registration page
        driver.get(self.reg_url)
        # Assertion that the title has Single Sign On in the title.
        self.assertIn("Single Sign On", driver.title)

        # Instructions for webdriver to read and input user data via the info on the .txt doc.
        # Credentials are localized to one instance via the var file
        funct.waitAndSend(driver, var.regV.fname, var.credsSSOWEB.fname)
        funct.waitAndSend(driver, var.regV.lname, var.credsSSOWEB.lname)
        funct.waitAndSend(driver, var.regV.housenum, var.credsSSOWEB.housenum)
        funct.waitAndSend(driver, var.regV.street, var.credsSSOWEB.street)
        funct.waitAndSend(driver, var.regV.city, var.credsSSOWEB.city)
        # Find and select the state according to the info in the .txt doc
        # Uses a for loop to iterate through the list of states until element
        # matches the entry info in the text file. Then clicks the element found.
        select_box = driver.find_element_by_name("state")
        funct.waitAndClick(driver, var.regV.state_dropdown)
        options = [x for x in select_box.find_elements_by_tag_name("option")]
        for element in options:
            if element.text in var.credsSSOWEB.state:
                element.click()
                break
        funct.waitAndSend(driver, var.regV.zip, var.credsSSOWEB.zip)
        funct.waitAndSend(driver, var.regV.phone, var.credsSSOWEB.phone)
        funct.waitAndSend(driver, var.regV.ssn4, var.credsSSOWEB.ssn4)
        funct.waitAndSend(driver, var.regV.dob,
                          (var.credsSSOWEB.dob_month + var.credsSSOWEB.dob_date + var.credsSSOWEB.dob_year))
        funct.waitAndClick(driver, var.regV.dob_check)
        funct.waitAndSend(driver, var.regV.email, testemail)
        funct.waitAndSend(driver, var.regV.password, var.credsSSOWEB.password)
        funct.waitAndSend(driver, var.regV.confirmPsw, var.credsSSOWEB.password)
        funct.waitAndClick(driver, var.regV.tos_check)
        funct.waitAndClick(driver, var.regV.submit_button)
        # Checking that error message appears and registration does not proceed.
        warning = driver.find_element(var.regV.submit_button_error[0], var.regV.submit_button_error[1])
        if funct.checkErrorText(driver, var.regV.submit_button_error, var.regV.duplicateEmailErrorStub) == True:
            print('PASS - Error warnings found and warning copy is correct')
            print('Warning text displayed is "' + warning.get_attribute("innerText") + '"')
        elif funct.checkErrorText(driver, var.regV.submit_button_error, var.regV.duplicateEmailErrorStub) == False:
            try:
                funct.purgeSSOemail(self, testemail)
                print('test user purged')
            except:
                print('no test user found')
            print(
                'FAIL - Warning should say "' + var.regV.duplicateEmailErrorStub + '" , but says "' + warning.get_attribute(
                    "innerText") + '"!')
            funct.fullshot(driver)
            raise Exception('Error warning(s) copy is incorrect')
        else:
            try:
                funct.purgeSSOemail(self, testemail)
                print('test user purged')
            except:
                print('no test user found')
            print("E---Error message did not appear or other unexpected behavior. Test Failed.")
            funct.fullshot(driver)
            raise Exception('Unexpected message or behavior.')
        # Deleting test data
        print('\n----------\n' + 'Test complete!\n\nTest clean up commencing')
        try:
            funct.purgeSSOemail(self, testemail)
        except:
            pass
        funct.closeWindow(driver, 'New York Lottery - Admin Dashboard')
        print('----------')

# use "report" variable in conftest.py to change report style on runner
if __name__ == "__main__":
    if confTest.NYlottoBASE.report == "terminal":
        unittest.main(warnings='ignore')
    elif confTest.NYlottoBASE.report == "html":
        unittest.main(warnings='ignore', testRunner=HtmlTestRunner.HTMLTestRunner(output='<html_report_dir>'))