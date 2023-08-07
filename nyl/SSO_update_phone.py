import unittest, time
import var, funct, confTest                   #Custom class for NYL
import HtmlTestRunner                               #Report runner

class NYlotto(confTest.NYlottoBASE):

    def test_updatePhone(self, testemail='self.testemail'):
        """ Tests updating user phone number via Update Profile page

        Jira test ticket - https://rosedigital.atlassian.net/browse/NYL-2040

        Creates a verified SSO user via SSN4 submission, navigates to the Update Profile page,
        submits new phone # and checks for correct frontend updates and redirects
        :param self: Webdriver instance
        :return: None
        """
        if testemail == 'self.testemail':
            testemail = self.testemail
        testenv = self.env
        print("TESTING " + testenv + " ENVIRONMENT")
        print("\nChecks phone change in update profile redirects per IDW pii check")

        print('\n----------\n' + 'Test setup')
        # creates a verified user with valid SSN4
        funct.createVerifiedUser(self, testemail)
        print('----------')

        driver = self.driver

        driver.get(self.update_url)
        time.sleep(2)
        # Makes change in field and submits
        phoneChange = self.tempphone
        formattedChange = "(" + phoneChange[:3] + ") " + phoneChange[3:6] + "-" + phoneChange[6:]
        # print(formattedChange)
        funct.clearTextField(driver, var.updateProfV.phone)
        funct.waitAndSend(driver, var.updateProfV.phone, phoneChange)
        funct.waitAndClick(driver, var.updateProfV.update_button)
        time.sleep(5)

        if funct.waitUntil(driver, var.identityVerFailedV.failed_body) == True:  # IDW returned a fail on PII check
            print("PASS - ID Verification Failed message is expected and received!")
            print('\n----------\n' + 'Test complete!\n\nTest clean up commencing')
            funct.purgeSSOemail(self, testemail)
            driver.quit()
        else:
            # 2nd screen. OTP selection screen
            funct.waitAndClick(driver, var.otpV.text_button)
            # 3rd screen. OTP code entry screen
            funct.waitAndSend(driver, var.otpV.otp_input, "111111")
            funct.waitAndClick(driver, var.otpV.otp_continue_button)
            time.sleep(5)
            # check for proper redirects
            if funct.waitUntil(driver, var.resetPswV.gSearchButton) == True:  #IDW returned a pass on PII check
                print('PASS - Update profile successfully redirected to Google.')
                # Checks the change has been saved to the profile
                driver.get(self.update_url)
                time.sleep(5)
                change = driver.find_element(var.updateProfV.phone[0], var.updateProfV.phone[1])
                if funct.checkValue(driver, var.updateProfV.phone, formattedChange) == True:
                    print('PASS - Profile update change for ' + var.updateProfV.phone[2] + ' successfully saved to user.')
                    print('Updated text is "' + change.get_attribute("value") + '"')
                elif funct.checkValue(driver, var.updateProfV.phone, formattedChange) == False:
                    print(
                        'FAIL - Updated ' + var.updateProfV.phone[
                            2] + ' field should say "' + formattedChange + '" , but says "' + change.get_attribute(
                            "value") + '"!')
                    funct.fullshot(driver)
                    try:
                        funct.purgeSSOemail(self, testemail)
                    except:
                        pass
                    raise Exception('Update profile changes failed to save.')
            else:
                funct.fullshot(driver)
                print('FAIL - Update profile redirect screen not reached. Test can not proceed.')
                try:
                    funct.purgeSSOemail(self, testemail)
                except:
                    pass
                raise Exception('Update profile redirected incorrectly')

            # Deleting test data
            print('\n----------\n' + 'Test complete!\n\nTest clean up commencing')
            try:
                funct.purgeSSOemail(self, testemail)
                funct.purgeSSOphone(self, phoneChange)
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