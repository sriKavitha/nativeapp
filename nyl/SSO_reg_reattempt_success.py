import unittest, time, re       #unittest is the testing framework, provides module for organizing test cases
import var, funct, util, confTest, HtmlTestRunner   #Custom class for NYL

class NYlotto(confTest.NYlottoBASE):


    def test_01_regReattempt(self):
        """Tests reattempting verification after a failed registration

        Jira test ticket - https://rosedigital.atlassian.net/browse/NYL-2370

        Registers user with empty SSN4 & gov ID check box checked and bad OTP entered.
        Exits registration process with unverified account.
        User should be able to login and retry verification.
        Successful verification should result in redirect to callback Uri and successful registration.

        :param self: Webdriver instance
        :return:
        """

        testenv = self.env
        print("TESTING " + testenv + " ENVIRONMENT")
        print("\nChecks reattempting registration with SSN4 & correct OTP code redirects successfully to callback Uri")
        testemail = self.testemail
        driver = self.driver
        print('\n----------\n' + 'Test setup')
        # tries 2 times to create a Unverified user with a failed registration
        i = 1
        while funct.createUnverifiedUser(self, testemail) == False:
            i += 1
            print(f'\nAttempt #{i}')
            if funct.createUnverifiedUser(self, testemail) == True:
                break
            elif i == 2:
                funct.purgeSSOemail(self, testemail)
                raise Exception(f'Failed to make unverified user. Check screenshot or error msg. Aborting test.')
        print('----------')
        # switch to login page
        driver.get(self.login_url)
        # Login attempt
        funct.waitAndSend(driver, var.loginV.email, testemail)
        funct.waitAndSend(driver, var.loginV.password, var.credsSSOWEB.password)
        funct.waitAndClick(driver, var.loginV.login_button)
        funct.waitUntil(driver, var.regV.fname)
        # Redirects to the verification screen, supply SSN and continue
        funct.waitAndSend(driver, var.regV.ssn4, var.credsSSOWEB.ssn4)
        # Clicks Confirm Details button
        funct.waitAndClick(driver, var.confirmDetailsV.submit_button)
        # OTP selection screen
        funct.waitAndClick(driver, var.otpV.text_button)
        # OTP code entry screen
        time.sleep(3)
        funct.waitAndSend(driver, var.otpV.otp_input, "111111")
        funct.waitAndClick(driver, var.otpV.otp_continue_button)
        time.sleep(5)
        # Successful registration should redirect to Google.com.
        # Checking that the search field on google.com is present on page.
        funct.verifyRedirect(self, driver, testemail, var.resetPswV.google)

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