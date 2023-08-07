import unittest, time, re       #unittest is the testing framework, provides module for organizing test cases
import var, funct, util, confTest, HtmlTestRunner   #Custom class for NYL

class NYlotto(confTest.NYlottoBASE):

    def test_regHardFailFakeData(self):
        """Tests the user flow when User with fake data attempts to register.

        Jira test ticket - https://rosedigital.atlassian.net/browse/NYL-1922
        Opens the registration page and submits bad information.
        The test checks that the failure redirects to the correct page.
        :return:
        """

        testenv = self.env
        print("TESTING " + testenv + " ENVIRONMENT")
        print("\nChecks that user is redirected to Hard Fail screen when fake data is submitted")
        testemail = self.testemail
        driver = self.driver
        # url is pulled from confTest
        driver.get(self.reg_url)
        # putting in acceptable but invalid data
        funct.waitAndSend(driver, var.regV.fname, "Fake")
        funct.waitAndSend(driver, var.regV.lname, "Test")
        funct.waitAndSend(driver, var.regV.housenum, "12345")
        funct.waitAndSend(driver, var.regV.street, "First Street")
        funct.waitAndSend(driver, var.regV.city, "Anytown")
        funct.waitAndClick(driver, var.regV.state_dropdown)
        driver.find_element_by_css_selector("#app-container > div > div.container__content > div > div > form > "
                                            "div:nth-child(1) > div:nth-child(10) > div > select > option:nth-child("
                                            "2)").click()
        funct.waitAndSend(driver, var.regV.zip, "11223")
        funct.waitAndSend(driver, var.regV.phone, "5559876543")
        funct.waitAndSend(driver, var.regV.ssn4, "1234")
        funct.waitAndSend(driver, var.regV.dob, "01/01/1990")
        funct.waitAndClick(driver, var.regV.dob_check)
        funct.waitAndSend(driver, var.regV.email, testemail)
        funct.waitAndSend(driver, var.regV.password, "Test1234")
        funct.waitAndSend(driver, var.regV.confirmPsw, "Test1234")
        funct.waitAndClick(driver, var.regV.tos_check)
        funct.waitAndClick(driver, var.regV.submit_button)

        # checking that we get to the "can not verify your identity" screen
        try:
            driver.find_elements_by_class_name("migration-failed-body")
        except:
            print("Can not find 'Identity verification failed' screen")
        if "Sorry, we cannot verify your identity." in driver.page_source:
             print("PASS - 'Identity verification failed' screen reached.")
        elif driver.find_elements_by_name("q") != []:
            print("FAIL - Reached successful registration and redirected to callback uri (Google.com)")
            funct.fullshot(driver)
            try:
                funct.purgeSSOemail(self, self.testemail)
                print('test user purged')
            except:
                print('no test user found')
            raise Exception('Registration succeeded where it was supposed to fail.')
        else:
            print("FAIL - Neither Identity verification failed screen nor Registration successful screen reached.")
            funct.fullshot(driver)
            try:
                funct.purgeSSOemail(self, self.testemail)
                print('test user purged')
            except:
                print('no test user found')
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
    if confTest.NYlottoBASE.report == "terminal":
        unittest.main(warnings='ignore')
    elif confTest.NYlottoBASE.report == "html":
        unittest.main(warnings='ignore', testRunner=HtmlTestRunner.HTMLTestRunner(output='<html_report_dir>'))