# [Documentation - Setup] This section lists all dependencies
# that are imported for this test file to work
from selenium import webdriver  #webdriver module provides all WebDriver implementations
import unittest, time  #unittest is the testing framework, provides module for organizing test cases
import var, funct, HtmlTestRunner                    #Custom class for NYL


class NYLmobileSmoke(unittest.TestCase):

# The setUp is part of initialization, this method will get called before every test function which you
# are going to write in this test case class. Here you are creating the instance of Chrome WebDriver.

    def setUp(self):
        desired_caps = {
            "deviceName": "Galaxy S7",
            "udid": "emulator-5554",
            "platformName": "Android",
            "version" : "9.0",
            "app": "/Users/Shared/testing/app-qa2.apk",
            "realDevice": False
        }
        caps = {}
        caps['deviceName'] = "Samsung Galaxy S7 HD GoogleAPI Emulator"
        caps['deviceOrientation'] = "portrait"
        caps['platformVersion'] = "8.0"
        caps['platformName'] = "Android"
        caps['app'] = "sauce-storage:NYLqa.apk"
        caps['build'] = "smokeTest"
        #Saucelab driver, WIP
        
        self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_caps)
        self.verificationErrors = []
        self.driver.implicitly_wait(12)

    def test_dashboardCheckText(self):
        driver = self.driver
        # [Documentation - detail] tests the text on the dashboard page
        funct.checkText(driver, var.NYLdashboard.guestCopy, var.NYLdashboard.guestStub)
        funct.checkText(driver, var.NYLdashboard.loginCopy, var.NYLdashboard.loginStub)

    def test_guest(self):
        driver = self.driver
        # [Documentation - detail] starts "continue as guest" workflow
        funct.waitAndClick(driver, var.NYLdashboard.guest_b)
        # [Documentation - detail] swipes leftward until the "get started" button is found, then clicks it
        funct.swipeLeftUntil(driver, var.NYLregistration.pip6, var.NYLregistration.getStarted_b)
        funct.waitAndClick(driver, var.NYLregistration.getStarted_b)
        time.sleep(1)
        # [Documentation - detail] clicks the "hamburger" button, and checks left drawer menu appears with proper title
        funct.waitAndClick(driver, var.NYLgamesDB.hamburger_b)
        funct.checkText(driver, var.NYLgamesDB.hamburger_home_copy, 'HOME')
    
    def test_login(self):
        driver = self.driver
        # [Documentation - detail] starts "login" workflow
        funct.waitAndClick(driver, var.NYLdashboard.login_b)
        # [Documentation - detail] causes username error to appear
        funct.waitUntil(driver, var.NYLdashboard.username_f)
        funct.waitAndClick(driver, var.NYLdashboard.login_b)
        # [Documentation - detail] checks that username error has appeared (with no unique identifier, we are forced to check how many elements are in the error's class)
        wlist = funct.getList(driver, var.NYLlogin.warningList)
        if len(wlist) == 7:
            pass
        else:
            print(len(wlist))
        funct.waitAndSend(driver, var.NYLdashboard.username_f, var.CREDSmobile.userName)
        funct.waitAndClick(driver, var.NYLdashboard.login_b)
        # [Documentation - detail] checks that pw error has appeared (through same method as above)
        wlist = funct.getList(driver, var.NYLlogin.warningList)
        if len(wlist) == 8:
            pass
        else:
            print(len(wlist))
        # [Documentation - detail] checks that valid email/pw will allow login
        funct.waitAndSend(driver, var.NYLdashboard.password_f, var.CREDSmobile.passWord)
        time.sleep(1)
        funct.waitAndClick(driver, var.NYLdashboard.login_b)
        time.sleep(3)
        funct.waitUntil(driver, var.NYLregistration.pip1)

    def test_register(self):
        driver = self.driver
        funct.waitAndClick(driver, var.NYLdashboard.register_b)
        # [Documentation - detail] checks registration page copy
        funct.waitAndClick(driver, var.NYLregistration.age_copy)
        funct.checkText(driver, var.NYLregistration.age_copy, var.NYLregistration.age_stub)
        funct.waitAndClick(driver, var.NYLregistration.reg_b)
        funct.swipeUp(driver, var.NYLregistration.base, .15)
        funct.swipeUp(driver, var.NYLregistration.base, .3)
        # [Documentation - detail] checks error messages upon registration page
        e_messages = [var.NYLregistration.email_e, var.NYLregistration.password_e, var.NYLregistration.confirmPW_e, var.NYLregistration.firstName_e, var.NYLregistration.lastName_e, var.NYLregistration.phone_e, var.NYLregistration.age_e, var.NYLregistration.zip_e]
        e_stubs = [var.NYLregistration.email_e_stub, var.NYLregistration.password_e_stub, var.NYLregistration.confirmPW_e_stub, var.NYLregistration.firstName_e_stub, var.NYLregistration.lastName_e_stub, var.NYLregistration.phone_e_stub, var.NYLregistration.age_e_stub, var.NYLregistration.zip_e_stub]
        for mes, stub in zip(e_messages, e_stubs):
            funct.checkText(driver, mes, stub)

# The tearDown method will get called after every test method. This is a place to do all cleanup actions.
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        var.CREDSmobile.notepadfile.close()


if __name__ == "__main__":
    #First runner will enable html logs on your current directory, second runner will keep local console logs
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='html_report_dir'))
    #unittest.main()
    