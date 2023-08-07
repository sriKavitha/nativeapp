import unittest, time, re       #unittest is the testing framework, provides module for organizing test cases
import var, funct, util, confTest, HtmlTestRunner   #Custom class for NYL



class NYlotto(confTest.NYlottoBASE):
    """Tests frontend and backend validation of date of birth field
    on 20200609 Hotfix of Register-verify schema regex

    Does not need to run in critical SSO tests, only during an extensive regression.

    """

    def test_01_regBirthMonth(self):
        """Tests months 1-12 can be used for registration
        :param self: Webdriver instance
        :return: None
        """
        print("Testing on " + self.env + " environment")
        print("\nCheck valid birth months can proceed in registration")
        i = 1
        passedBirthMonthFlags = []
        failedBirthMonthFlags = []
        while i < 13:
            if i < 10:
                istring = "0" + str(i)
            elif i >= 10:
                istring = str(i)

            testemail = "qa+month" + istring + "@rosedigital.co"

            # Check for existing test user and wipe it from userpool prior to test execution
            try:
                funct.purgeSSOphone(self, var.credsSSOWEB.phone)
            except:
                print('no test user found')
            driver = self.driver
            driver.get(self.reg_url)
            self.assertIn("Single Sign On", driver.title)

            # Instructions for webdriver to read and input user data via the info on the .txt doc.
            # Credentials are localized to one instance via the var file
            funct.waitAndSend(driver, var.regV.fname, var.credsSSOWEB.fname)
            funct.waitAndSend(driver, var.regV.lname, var.credsSSOWEB.lname)
            funct.waitAndSend(driver, var.regV.housenum, var.credsSSOWEB.housenum)
            funct.waitAndSend(driver, var.regV.street, var.credsSSOWEB.street)
            funct.waitAndSend(driver, var.regV.city, var.credsSSOWEB.city)
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
            funct.waitAndSend(driver, var.regV.dob, (istring + "011980"))
            funct.waitAndSend(driver, var.regV.email, testemail)
            funct.waitAndSend(driver, var.regV.password, var.credsSSOWEB.password)
            funct.waitAndSend(driver, var.regV.confirmPsw, var.credsSSOWEB.password)
            funct.waitAndClick(driver, var.regV.dob_check)
            funct.waitAndClick(driver, var.regV.tos_check)
            funct.waitAndClick(driver, var.regV.submit_button)
            # 2nd screen. OTP selection screen or Failed verification page
            time.sleep(6)
            if driver.find_elements_by_class_name("confirm-otp-header") != []:
                passedBirthMonthFlags.append(istring)
                i = i + 1
            elif "Sorry, we cannot verify your identity." in driver.page_source:
                passedBirthMonthFlags.append(istring)
                i = i + 1
            else:
                funct.fullshot(driver)
                passedBirthMonthFlags.append('xfail')
                failedBirthMonthFlags.append(istring)
                try:
                    funct.purgeSSOemail(self, testemail)
                except:
                    print('no test user found')
                i = i + 1
            try:
                funct.purgeSSOemail(self, testemail)
            except:
                print('no test user found')

        if failedBirthMonthFlags != []:
            print("PASS - Next step (OTP page / Failed Verification page) reached on Month(s):")
            print(passedBirthMonthFlags)
            print("FAIL - Redirect screen not reached on Month(s):")
            print(failedBirthMonthFlags)
            raise Exception("Registration redirected incorrectly")
        else:
            print("PASS - Next step (OTP page / Failed Verification page) reached on Month(s):")
            print(passedBirthMonthFlags)
        print('----------')


    def test_02_regBirthDate(self):
        """Tests dates 1-31 can be used for registration
        :param self: Webdriver instance
        :return: None
        """
        print("Testing on " + self.env + " environment")
        print("\nCheck valid birth dates can proceed in registration")
        i = 1
        passedBirthDateFlags = []
        failedBirthDateFlags = []
        while i < 32:
            if i < 10:
                istring = "0" + str(i)
            elif i >= 10:
                istring = str(i)

            testemail = "qa+date" + istring + "@rosedigital.co"

            # Check for existing test user and wipe it from userpool prior to test execution
            try:
                funct.purgeSSOphone(self, var.credsSSOWEB.phone)
            except:
                print('no test user found')
            driver = self.driver
            driver.get(self.reg_url)
            self.assertIn("Single Sign On", driver.title)

            # Instructions for webdriver to read and input user data via the info on the .txt doc.
            # Credentials are localized to one instance via the var file
            funct.waitAndSend(driver, var.regV.fname, var.credsSSOWEB.fname)
            funct.waitAndSend(driver, var.regV.lname, var.credsSSOWEB.lname)
            funct.waitAndSend(driver, var.regV.housenum, var.credsSSOWEB.housenum)
            funct.waitAndSend(driver, var.regV.street, var.credsSSOWEB.street)
            funct.waitAndSend(driver, var.regV.city, var.credsSSOWEB.city)
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
            funct.waitAndSend(driver, var.regV.dob, ("01" + istring + "1980"))
            funct.waitAndSend(driver, var.regV.email, testemail)
            funct.waitAndSend(driver, var.regV.password, var.credsSSOWEB.password)
            funct.waitAndSend(driver, var.regV.confirmPsw, var.credsSSOWEB.password)
            funct.waitAndClick(driver, var.regV.dob_check)
            funct.waitAndClick(driver, var.regV.tos_check)
            funct.waitAndClick(driver, var.regV.submit_button)
            # 2nd screen. OTP selection screen or Failed verification page
            time.sleep(8)
            if driver.find_elements_by_class_name("confirm-otp-header") != []:
                print("PASS - date: " + istring)
                passedBirthDateFlags.append(istring)
                # print(passedBirthDateFlags)
                i = i + 1
            elif "Sorry, we cannot verify your identity." in driver.page_source:
                print("WARNING - date: " + istring)
                passedBirthDateFlags.append(istring)
                # print(passedBirthDateFlags)
                i = i + 1
            else:
                print("FAIL - date: " + istring)
                passedBirthDateFlags.append('xfail')
                failedBirthDateFlags.append(istring)
                # print(failedBirthDateFlags)
                funct.fullshot(driver)
                try:
                    funct.purgeSSOemail(self, testemail)
                except:
                    print('no test user found')
                i = i + 1
            try:
                funct.purgeSSOemail(self, testemail)
            except:
                print('no test user found')

        if failedBirthDateFlags != []:
            print("PASS - Next Step (OTP page / Failed Verification page) reached on Date(s):")
            print(passedBirthDateFlags)
            print("FAIL - Redirect screen not reached on Date(s):")
            print(failedBirthDateFlags)
            raise Exception("Registration redirected incorrectly")
        else:
            print("PASS - Next Step (OTP page / Failed Verification page) reached on Date(s):")
            print(passedBirthDateFlags)
        print('----------')


    def test_03_regBirthYear(self):
        """Tests decades from 1900 - 2010 can be used for registration
        :param self: Webdriver instance
        :return: None
        """
        print("Testing on " + self.env + " environment")
        print("\nCheck valid birth years can proceed in registration")
        i = 1900
        passedBirthYearFlags = []
        failedBirthYearFlags = []
        while i < 2010:
            if i < 10:
                istring = "0" + str(i)
            elif i >= 10:
                istring = str(i)

            testemail = "qa+year" + istring + "@rosedigital.co"

            # Check for existing test user and wipe it from userpool prior to test execution
            try:
                funct.purgeSSOphone(self, var.credsSSOWEB.phone)
            except:
                print('no test user found')
            driver = self.driver
            driver.get(self.reg_url)
            self.assertIn("Single Sign On", driver.title)

            # Instructions for webdriver to read and input user data via the info on the .txt doc.
            # Credentials are localized to one instance via the var file
            funct.waitAndSend(driver, var.regV.fname, var.credsSSOWEB.fname)
            funct.waitAndSend(driver, var.regV.lname, var.credsSSOWEB.lname)
            funct.waitAndSend(driver, var.regV.housenum, var.credsSSOWEB.housenum)
            funct.waitAndSend(driver, var.regV.street, var.credsSSOWEB.street)
            funct.waitAndSend(driver, var.regV.city, var.credsSSOWEB.city)
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
            funct.waitAndSend(driver, var.regV.dob, ("0101" + istring))
            funct.waitAndSend(driver, var.regV.email, testemail)
            funct.waitAndSend(driver, var.regV.password, var.credsSSOWEB.password)
            funct.waitAndSend(driver, var.regV.confirmPsw, var.credsSSOWEB.password)
            funct.waitAndClick(driver, var.regV.dob_check)
            funct.waitAndClick(driver, var.regV.tos_check)
            funct.waitAndClick(driver, var.regV.submit_button)
            # 2nd screen. OTP selection screen or Failed verification page
            time.sleep(8)
            if driver.find_elements_by_class_name("confirm-otp-header") != []:
                print("PASS - date: " + istring)
                passedBirthYearFlags.append(istring)
                #print(passedBirthYearFlags)
                i = i + 10
            elif "Sorry, we cannot verify your identity." in driver.page_source:
                print("WARNING - date: " + istring)
                passedBirthYearFlags.append(istring)
                #print(passedBirthYearFlags)
                i = i + 10
            else:
                print("FAIL - date: " + istring)
                passedBirthYearFlags.append('xfail')
                failedBirthYearFlags.append(istring)
                #print(failedBirthYearFlags)
                funct.fullshot(driver)
                try:
                    funct.purgeSSOphone(self, var.credsSSOWEB.phone)
                except:
                    print('no test user found')
                i = i + 10
            try:
                funct.purgeSSOemail(self, testemail)
            except:
                print('no test user found')

        if failedBirthYearFlags != []:
            print("PASS - Next Step (OTP page / Failed Verification page) reached on Date(s):")
            print(passedBirthYearFlags)
            print("FAIL - Redirect screen not reached on Date(s):")
            print(failedBirthYearFlags)
            raise Exception("Registration redirected incorrectly")
        else:
            print("PASS - Next Step (OTP page / Failed Verification page) reached on Date(s):")
            print(passedBirthYearFlags)
        print('----------')


    def test_04_regInvalidDOB(self):
        """Tests invalid birthdates cannot be submitted
        :param self: Webdriver instance
        :return: None
        """
        print("Testing on " + self.env + " environment")
        print("\nCheck invalid dates of birth cannot proceed with registration")
        testemail = "qa+ssotest@rosedigital.co"
        # Check for existing test user and wipe it from userpool prior to test execution
        try:
            funct.purgeSSOphone(self, var.credsSSOWEB.phone)
        except:
            print('no test user found')
        driver = self.driver

        passedInvalidDOBFlags = []
        failedInvalidDOBFlags = []
        invalidDOB = ["00000000", "00012000", "13131313", "13012000", "32323232", "01322000", "01012010"]
        #invalidDOB = ["00000000", "00012000", "13131313", "13012000", "32323232", "01322000", "01012010", "02301980", "02311980", "04311980", "06311980", "09311980", "11311980"]

        for DOB in invalidDOB:
            driver.get(self.reg_url)
        # Instructions for webdriver to read and input user data via the info on the .txt doc.
        # Credentials are localized to one instance via the var file
            funct.waitAndSend(driver, var.regV.fname, var.credsSSOWEB.fname)
            funct.waitAndSend(driver, var.regV.lname, var.credsSSOWEB.lname)
            funct.waitAndSend(driver, var.regV.housenum, var.credsSSOWEB.housenum)
            funct.waitAndSend(driver, var.regV.street, var.credsSSOWEB.street)
            funct.waitAndSend(driver, var.regV.city, var.credsSSOWEB.city)
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
            funct.waitAndSend(driver, var.regV.dob, DOB)
            funct.waitAndSend(driver, var.regV.email, testemail)
            funct.waitAndSend(driver, var.regV.password, var.credsSSOWEB.password)
            funct.waitAndSend(driver, var.regV.confirmPsw, var.credsSSOWEB.password)
            funct.waitAndClick(driver, var.regV.dob_check)
            funct.waitAndClick(driver, var.regV.tos_check)
            funct.waitAndClick(driver, var.regV.submit_button)
        # user should remain on registration screen with error message
            time.sleep(5)
            if funct.checkError(driver, var.regV.submit_button_error) == True:
                passedInvalidDOBFlags.append(DOB)
            elif funct.checkError(driver, var.regV.submit_button_error) == False:
                passedInvalidDOBFlags.append('xfail')
                failedInvalidDOBFlags.append(DOB)
                funct.fullshot(driver)
                try:
                    funct.purgeSSOemail(self, testemail)
                except:
                    print('no test user found')
            try:
                funct.purgeSSOemail(self, testemail)
            except:
                print('no test user found')

        if failedInvalidDOBFlags != []:
            print("PASS - Error messages are present for invalid DOB: ")
            print(passedInvalidDOBFlags)
            print("FAIL - Error messages missing for DOB: ")
            print(failedInvalidDOBFlags)
            raise Exception("Registration redirected incorrectly")
        else:
            print("PASS - Error messages are present for invalid DOB: ")
            print(passedInvalidDOBFlags)
        print('----------')


# use "report" variable in conftest.py to change report style on runner
if __name__ == "__main__":
    if confTest.NYlottoBASE.report == "terminal":
        unittest.main(warnings='ignore')
    elif confTest.NYlottoBASE.report == "html":
        unittest.main(warnings='ignore', testRunner=HtmlTestRunner.HTMLTestRunner(output='<html_report_dir>'))