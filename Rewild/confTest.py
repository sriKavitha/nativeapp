# [Documentation - Setup] This section lists all dependencies
# that are imported for this test file to work
from selenium import webdriver  #webdriver module provides all WebDriver implementations
import warnings
from browsermobproxy import Server
import unittest, time, re       #unittest is the testing framework, provides module for organizing test cases
from selenium.webdriver.common.keys import Keys     #Keys class provide keys in the keyboard like RETURN, F1, ALT, etc.
from selenium.webdriver.common.by import By         #By class provides method for finding the page elements by NAME, ID, XPATH, etc.
from selenium.webdriver.support.ui import Select    #Select class provides ability to select items in dropdown
import var, funct, util                         #Custom class

class RewildBrowserBASE(unittest.TestCase):
    # report can be 'html' for testrunner reports or 'terminal' for direct terminal feedback
    report = 'terminal'
    # report = 'html'

    # The setUp is part of initialization, this method will get called before every test function which you
    # are going to write in this test case class. Here you are creating the instance of Chrome WebDriver.
    def setUp(self):
        # .env can be 'dev', 'qa', or 'stage' to denote which environment and credentials to use
        self.env = 'dev'
        # run can be 'local' for local machine executions, 'grid' for runs on selenium grid,
        # 'remote' for runs on saucelabs grid
        run = 'local'

        if self.env == 'dev':
            self.url = 'https://dev.rewild-dev.org/'
        elif self.env == 'qa':
            self.url = 'https://qa.rewild-dev.org/'
        elif self.env == 'stage':
            self.url = 'https://stage.rewild-dev.org/'
        elif self.env == 'preview':
            self.url = 'https://preview.rewild.org'
        elif self.env == 'prod':
            self.url = 'https://www.rewild.org'

        warnings.simplefilter('ignore', ResourceWarning)

        if run == 'local':
            chrome_options = webdriver.ChromeOptions()
            # chrome_options.add_argument('--proxy-server={0}'.format(self.url))
            chrome_options.add_argument('--incognito')
            self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.implicitly_wait(12)
            self.driver.maximize_window()
            self.verificationErrors = []
            self.accept_next_alert = True
        elif run == 'grid':
            self.driver = webdriver.Remote(
                command_executor='http://192.168.86.21:4444/wd/hub',    # add local grid address here
                desired_capabilities={
                    'browserName': 'chrome',
                    'version': '',
                    'platform': 'ANY',
                    'javascriptEnabled': True,
                    'chromeOptions': {
                        'useAutomationExtension': False,
                        'args': ['--disable-infobars']
                    }
                })
            self.driver.implicitly_wait(12)
            self.driver.maximize_window()
            self.verificationErrors = []
            self.accept_next_alert = True
        # TODO add saucelabs creds to test on saucelabs grid
        # import os
        # sauce_username = os.environ['SAUCE_USERNAME']
        # sauce_access_key = os.environ['SAUCE_ACCESS_KEY']
        # elif run == 'remote':
        #     self.driver = webdriver.Remote(
        #         command_executor='https://ondemand.saucelabs.com:443/wd/hub',
        #         desired_capabilities={
        #             'browserName': 'chrome',
        #             'version': '',
        #             'platform': 'ANY',
        #             'javascriptEnabled': True,
        #             'username': sauce_username,
        #             'accessKey': sauce_access_key,
        #             'chromeOptions': {
        #                 'useAutomationExtension': False,
        #                 'args': ['--disable-infobars']
        #             }
        #         })
        #     self.driver.implicitly_wait(12)
        #     self.driver.maximize_window()
        #     self.verificationErrors = []
        #     self.accept_next_alert = True

        # self.server = Server('/Users/browsermob-proxy-2.1.4/bin/browsermob-proxy', options={'port': 8090})
        # self.server.start()

    # The tearDown method will get called after every test method. This is a place to do all cleanup actions.
    def tearDown(self):
        # NOTE: this code for checking for exceptions does NOT work for Safari
        # Python 3.8+ may have this built in. Need to revisit at future date.
        # # checking for exceptions or assertion errors, if there are take screenshot
        # for method, error in self._outcome.errors:
        #     if error:
        #         funct.fullshot(self.driver)
        #         # funct.generateHAR(self.server, self.driver)
        # self.driver.quit()
        self.assertEqual([], self.verificationErrors)


class RewildHeadlessBASE(unittest.TestCase):
    # report can be 'html' for testrunner reports or 'terminal' for direct terminal feedback
    report = 'terminal'
    # report = 'html'

    # The setUp is part of initialization, this method will get called before every test function which you
    # are going to write in this test case class. Here you are creating the instance of Chrome WebDriver.
    def setUp(self):
        self.verificationErrors = []
        self.accept_next_alert = True

    # The tearDown method will get called after every test method. This is a place to do all cleanup actions.
    def tearDown(self):
        self.assertEqual([], self.verificationErrors)
