import unittest, time, re       #unittest is the testing framework, provides module for organizing test cases
import var, funct, util, confTest, HtmlTestRunner   #Custom class for NYL

class NYlotto(confTest.NYlottoBASE):


    def test_01_loginSuccess(self):
        """Checks that a user can login in successfully

        Jira test ticket - https://rosedigital.atlassian.net/browse/NYL-2407

        Creates a verified user via the registration page, navigates to the login page and attempts login.
        :return:
        """

        testenv = self.env
        print("TESTING " + testenv + " ENVIRONMENT")
        print("\nChecks login with correct email & password redirects successfully")
        testemail = self.testemail
        driver = self.driver
        print('\n----------\n' + 'Test setup')
        # creates a verified user with valid SSN4
        funct.createVerifiedUser(self, testemail)
        print('----------')
        # switch to login page
        driver.get(self.login_url)
        # Login attempt
        funct.waitAndSend(driver, var.loginV.email, testemail)
        funct.waitAndSend(driver, var.loginV.password, var.credsSSOWEB.password)
        funct.waitAndClick(driver, var.loginV.login_button)
        # Successful login should redirect to Google.com.
        # Checking that the search field on google.com is present on page.
        if driver.find_elements_by_name("q") != []:
            print('PASS - login successful and redirected to callback uri')
        else:
            funct.fullshot(driver)
            print('FAIL - Login attempt failed or redirected incorrectly')
            raise Exception('Unexpected behavior encountered')
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