import unittest, time, re       #unittest is the testing framework, provides module for organizing test cases
import var, funct, util, confTest, HtmlTestRunner   #Custom class for NYL



class NYlotto(confTest.NYlottoBASE):


    def test_regSSNSuccess(self):
        """Tests user workflow of successful registration with valid SSN4 and OTP pass

        Jira test ticket - https://rosedigital.atlassian.net/browse/NYL-2400
        Checks for existing user in userpool and removes it, then opens registration page and submits
        new user registration with test data in credentials file.
        :param self: Webdriver instance
        :return:
        """
        testenv = self.env
        print("TESTING " + testenv + " ENVIRONMENT")
        testemail = self.testemail
        print("\nChecks successful registration with SSN4 and OTP pass on Browser method")

        print('\n----------\n' + 'Test setup')
        # Check for existing test user and wipe it from userpool prior to test execution
        try:
            try:
                funct.purgeSSOemail(self, testemail)
            except:
                funct.purgeSSOphone(self, var.credsSSOWEB.phone)
        except:
            print('no test user found')
        print('----------')
        driver = self.driver
        # The driver.get method will navigate to a page given by the URL.
        # WebDriver will wait until the page has fully loaded (that is, the “onload” event has fired)
        # before returning control to your test or script.
        # url is pulled from confTest
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
        funct.waitAndSend(driver, var.regV.dob, (var.credsSSOWEB.dob_month + var.credsSSOWEB.dob_date + var.credsSSOWEB.dob_year))
        funct.waitAndClick(driver, var.regV.dob_check)
        funct.waitAndSend(driver, var.regV.email, testemail)
        funct.waitAndSend(driver, var.regV.password, var.credsSSOWEB.password)
        funct.waitAndSend(driver, var.regV.confirmPsw, var.credsSSOWEB.password)
        funct.waitAndClick(driver, var.regV.tos_check)
        funct.waitAndClick(driver, var.regV.submit_button)
        # 2nd screen. OTP selection screen
        funct.waitAndClick(driver, var.otpV.text_button)
        # 3rd screen. OTP code entry screen
        funct.waitAndSend(driver, var.otpV.otp_input, "111111")
        funct.waitAndClick(driver, var.otpV.otp_continue_button)
        time.sleep(5)
        # 4th screen. Successful registration should redirect to Google.com.
        # Checking that the search field on google.com is present on page.
        if driver.find_elements_by_name("q") != []:
             print("PASS - registration successful and redirected to callback uri")
        else:
            funct.fullshot(driver)
            print("FAIL - Redirect screen not reached.")
            try:
                funct.purgeSSOemail(self, testemail)
            except:
                pass
            raise Exception('Registration redirected incorrectly.')

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
    if confTest.NYlottoBASE.report == 'terminal':
        unittest.main(warnings='ignore')
    elif confTest.NYlottoBASE.report == 'html':
        unittest.main(warnings='ignore', testRunner=HtmlTestRunner.HTMLTestRunner(output='<html_report_dir>'))