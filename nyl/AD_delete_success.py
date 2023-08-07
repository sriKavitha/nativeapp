import unittest, time, re       #unittest is the testing framework, provides module for organizing test cases
from selenium.webdriver.common.keys import Keys     #Keys class provide keys in the keyboard like RETURN, F1, ALT, etc.
import var, funct, confTest, HtmlTestRunner   #Custom class for NYL

class NYLadmin(confTest.NYLadminBASE):

    def test_deleteEmailSuccess(self):
        """Verifies that an Admin Dash super user can purge an SSO user via Admin Dash with the SSO user email

        Creates a verified SSO user in the userpool. Logs in the Admin Dashboard with an Admin superuser.
        Searches for the SSO user with email address, selects the user detail tab, chooses to delete user
        and enters appropriate comment. Proceeds to find SSO user in purged user list, selects user detail tab and
        purges the SSO user from the user database.
        :return:
        """
        testenv = self.env
        print("TESTING " + testenv + " ENVIRONMENT")
        testemail = self.testemail
        print("\nChecks deletion and purge of user with email search is successful")
        print('\n----------\n' + 'Test setup')
        # creates a verified user with valid SSN4
        funct.createVerifiedUser(self, testemail)
        print('----------')
        driver = self.driver

        driver.get(self.admin_url)

        try:  # try to login
            funct.waitAndSend(driver, var.adminLoginVar.email, var.CREDSadmin.superadmin_username)
            funct.waitAndSend(driver, var.adminLoginVar.password, var.CREDSadmin.superadmin_psw)
            funct.waitAndClick(driver, var.adminLoginVar.signin_button)
        except Exception:  # if session persists from before, extend session and continue
            try:
                time.sleep(2)
                funct.waitAndClick(driver, var.adminDashVar.extend_button)
                print('Admin Dash Session persisted, login bypassed')
            except:
                pass
        # Search for test user via Email
        # TODO due to ongoing Admin Dash work in dev env, this if else is in place,
        #  will need to update once AD work is complete
        if self.env == 'dev':
            funct.waitAndClick(driver, var.adminDashVar.search_input)
            funct.waitAndSend(driver, var.adminDashVar.search_input, testemail)
        else:
            funct.waitAndClick(driver, var.adminDashVar.search_input)
            funct.waitAndClick(driver, var.adminDashVar.category_email)
            funct.waitAndClick(driver, var.adminDashVar.operator_contains)
            funct.waitAndSend(driver, var.adminDashVar.search_input, testemail)
            driver.find_element_by_xpath(var.adminDashVar.search_input[1]).send_keys(Keys.ENTER)
        try:
            time.sleep(2)
            funct.waitAndClick(driver, var.adminDashVar.search_button)
            time.sleep(2)
            funct.waitAndClick(driver, var.adminDashVar.search_button)
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
                # Clicks view/edit button for first user returned, navigates to detail page and clicks delete
                funct.waitAndClick(driver, var.adminDashVar.view_edit_button)
                funct.waitAndClick(driver, var.adminUsersVar.user_status_tab)
                funct.waitAndClick(driver, var.adminUsersVar.delete_button)
                # Submits comment and mandatory text for completion
                ts = funct.timeStamp
                funct.waitAndSend(driver, var.adminDashVar.comment_textarea, "automated test change at " + ts)
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

                funct.waitAndSend(driver, var.adminDashVar.comment_phrase_textarea, "mark for deletion")

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

                time.sleep(2)
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

                # # Navigates to Pending Deletion user list to purge user
                funct.waitAndClick(driver, var.adminDashVar.pendingDeletion_link)
                time.sleep(2)
                # Search for test user via Email
                funct.waitAndClick(driver, var.adminDashVar.search_input)
                funct.waitAndSend(driver, var.adminDashVar.search_input, testemail)
                funct.waitAndClick(driver, var.adminDashVar.search_button)
                time.sleep(1)
                funct.waitAndClick(driver, var.adminDashVar.search_button)
                time.sleep(3)

                # Checks the returned user is the correct user
                rows = driver.find_elements_by_xpath('//tr[@class="ant-table-row ant-table-row-level-0"]')
                if len(rows) == 1:
                    if driver.find_element_by_xpath(
                            '//td[@class="ant-table-cell"][4]').text == testemail:  # check that first user returned is has the same email address
                        # Clicks view/edit button for first user returned, navigates to detail page and clicks delete
                        funct.waitAndClick(driver, var.adminDashVar.view_edit_button)
                        funct.waitAndClick(driver, var.adminPendingDeletionVar.user_status_tab)
                        funct.waitAndClick(driver, var.adminPendingDeletionVar.permanently_delete_button)
                        # Submits comment and mandatory text for completion
                        ts = funct.timeStamp()
                        funct.waitAndSend(driver, var.adminDashVar.comment_textarea, "automated test change at " + ts)
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

                        funct.waitAndSend(driver, var.adminDashVar.comment_phrase_textarea, "purge")

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

                        time.sleep(2)
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

                        time.sleep(3)
                        # Search for test user via Email again to confirm user is gone from system
                        funct.waitAndClick(driver, var.adminDashVar.users_link)
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
                        rows = driver.find_elements_by_xpath('//tr[@class="ant-table-row ant-table-row-level-0"]')
                        if driver.find_elements_by_xpath(
                                var.adminDashVar.no_data_msg[1]) != []:  # search returns no data
                            print(f'\ntest user {testemail} found and purged')
                        elif len(rows) >= 1:  # search returns list of users
                            funct.fullshot(driver)
                            print(f'\nuser still in Pending Deletion list with {testemail}, check user pool')
                            raise Exception
                        else:
                            print(f'\nunexpected behavior: please check screenshot')
                            funct.fullshot(driver)
                            raise Exception
                    else:
                        print(f'unexpected behavior: please check screenshot')
                        funct.fullshot(driver)
                        raise Exception
                elif len(rows) >= 2:  # more than 1 user was returned in table
                    funct.fullshot(driver)
                    print(f'More than 1 user found in Pending Deletion list, check screenshot')
                    raise Exception
                elif driver.find_elements_by_xpath(var.adminDashVar.no_data_msg[1]) != []:  # no user returned in table
                    print(f'no test user {testemail} found')
                    # open new window with execute_script()
                    driver.execute_script("window.open('');")
                    funct.closeWindow(driver, 'New York Lottery - Admin Dashboard')
                    exit()
                else:
                    print(f'unexpected behavior: please check screenshot')
                    funct.fullshot(driver)
            else:
                print(f'\nunexpected behavior: please check screenshot')
                funct.fullshot(driver)
        elif len(rows) >= 2:  # more than 1 user was returned in table
            funct.fullshot(driver)
            print(f'\nMore than 1 user found in table, check screenshot')
            raise Exception
        elif driver.find_elements_by_xpath(var.adminDashVar.no_data_msg[1]) != []:  # no user returned in table
            print(f'\nno test user {testemail} found')
            # open new window with execute_script()
            driver.execute_script("window.open('');")
            funct.closeWindow(driver, 'New York Lottery - Admin Dashboard')
        else:
            print(f'\nunexpected behavior: please check screenshot')
            funct.fullshot(driver)
            
            
# use "report" variable in conftest.py to change report style on runner
if __name__ == "__main__":
    if confTest.NYlottoBASE.report == "terminal":
        unittest.main(warnings='ignore')
    elif confTest.NYlottoBASE.report == "html":
        unittest.main(warnings='ignore', testRunner=HtmlTestRunner.HTMLTestRunner(output='<html_report_dir>'))