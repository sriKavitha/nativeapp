# [Documentation - Setup] This section lists all dependencies
# that are imported for this test file to work
from selenium import webdriver  #webdriver module provides all WebDriver implementations
import warnings
from browsermobproxy import Server
import unittest  #unittest is the testing framework, provides module for organizing test cases
import funct

class globalVar:
    """
    Global variables - change the variables in this section for
    all tests in the suite to inherit the assignment
    """
    # report can be "html" for testrunner reports or "terminal" for direct terminal feedback
    report = 'terminal'
    # report = "html"

    # testdata can be "iddw" or "real" to denote which credential files to use in var.py
    testdata = 'iddw'
    # testdata = 'real'

    # .env can be "dev", "qa", or "stage" to denote which environment and credentials to use
    # env = 'qa'
    env = 'dev'

    # testemail = 'qa+ssotest@rosedigital.co'
    testemail = 'dev+ssotest@rosedigital.co'
    # tester's actual mobile number needed for govid registration flows
    testermobile = '0000000000'

    # secondary phone # for manipulating in test cases https://fakenumber.org/
    tempphone = '2025550113'

###==============================================================###
# NYL Admin Dash
###==============================================================###
class NYLadminBASE(unittest.TestCase):
    testdata = globalVar.testdata
    report = globalVar.report

    def setUp(self):
        """The setUp is part of initialization, this method will get called before every test function which you
        are going to write in the test case class.

        Here you are creating the instance of Chrome WebDriver with specific test configurations needed for
        testing Admin Dashboard web application.
        """
        self.env = globalVar.env
        self.testemail = globalVar.testemail

        self.admin_url = 'https://admin-' + self.env + '.nylservices.net'
        self.pending_del_url = 'https://admin-' + self.env + '.nylservices.net/pending-deletion'
        self.perm_del_url = 'https://admin-' + self.env + '.nylservices.net/purged-users'
        self.admin_users_url = 'https://admin-' + self.env + '.nylservices.net/admins'
        self.features_url = 'https://admin-' + self.env + '.nylservices.net/features'

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        # chrome_options.add_argument("--window-size=1366,768")
        chrome_options.add_argument("--window-size=1440,900")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(12)
        # self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        """The tearDown method will get called after every test method. This is a place to do all cleanup actions."""
        # NOTE: this code for checking for exceptions does NOT work for Safari
        # Python 3.8+ may have this built in. Need to revisit at future date.
        # checking for exceptions or assertion errors, if there are take screenshot
        # for method, error in self._outcome.errors:
        #     if error:
        #         funct.fullshot(self.driver)
        #         funct.generateHAR(self.server, self.driver)
        # # self.driver.quit()
        self.assertEqual([], self.verificationErrors)

###==============================================================###
# NYL Services API
###==============================================================###
class NYLservicesBASE(unittest.TestCase):
    testdata = globalVar.testdata
    report = globalVar.report

    def setUp(self):
        """The setUp is part of initialization, this method will get called before every test function which you
        are going to write in the test case class.

        Here you are creating the instance of Chrome WebDriver with specific test configurations needed for
        testing Nylservices API.
        """
        self.env = globalVar.env
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        # chrome_options.add_argument("--window-size=1366,768")
        chrome_options.add_argument("--window-size=1440,900")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(12)
        # self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        """The tearDown method will get called after every test method. This is a place to do all cleanup actions."""
        # NOTE: this code for checking for exceptions does NOT work for Safari
        # Python 3.8+ may have this built in. Need to revisit at future date.
        # checking for exceptions or assertion errors, if there are take screenshot
        # for method, error in self._outcome.errors:
        #     if error:
        #         funct.fullshot(self.driver)
        #         funct.generateHAR(self.server, self.driver)
        # # self.driver.quit()
        self.assertEqual([], self.verificationErrors)

# ###==============================================================###
# # NYL SSO
# ###==============================================================###
class NYlottoBASE(unittest.TestCase):
    report = globalVar.report
    testdata = globalVar.testdata

    def setUp(self):
        """The setUp is part of initialization, this method will get called before every test function which you
        are going to write in the test case class.

        Here you are creating the instance of Chrome WebDriver with specific test configurations needed for
        testing SSO web application.
        """
        self.aws_login_url = "https://nyl-sso.signin.aws.amazon.com/console"
        self.env = globalVar.env
        self.testemail = globalVar.testemail
        self.testermobile = globalVar.testermobile
        self.tempphone = globalVar.tempphone
        if self.env == 'dev':
            self.reg_url = "https://sso-dev.nylservices.net/?clientId=29d5np06tgg87unmhfoa3pkma7&callbackUri=https://google.com"
            self.login_url = "https://sso-dev.nylservices.net/login?clientId=29d5np06tgg87unmhfoa3pkma7&callbackUri=https://google.com"
            self.reset_url = "https://sso-dev.nylservices.net/reset-password?clientId=29d5np06tgg87unmhfoa3pkma7"
            self.update_url = "https://sso-dev.nylservices.net/update-profile?clientId=29d5np06tgg87unmhfoa3pkma7&callbackUri=https://google.com"
        elif self.env == 'qa':
            self.reg_url = "https://sso-qa.nylservices.net/?clientId=4a0p01j46oms3j18l90lbtma0o&callbackUri=https://google.com"
            self.login_url = "https://sso-qa.nylservices.net/login?clientId=4a0p01j46oms3j18l90lbtma0o&callbackUri=https://google.com"
            self.reset_url = "https://sso-qa.nylservices.net/reset-password?clientId=4a0p01j46oms3j18l90lbtma0o"
            self.update_url = "https://sso-qa.nylservices.net/update-profile?clientId=4a0p01j46oms3j18l90lbtma0o&callbackUri=https://google.com"
        elif self.env == 'stage':
            self.reg_url = "https://sso-stage.nylservices.net/?clientId=6pdeoajlh4ttgktolu3jir8gp6&callbackUri=https://google.com"
            self.login_url = "https://sso-stage.nylservices.net/login?clientId=6pdeoajlh4ttgktolu3jir8gp6&callbackUri=https://google.com"
            self.reset_url = "https://sso-stage.nylservices.net/reset-password?clientId=6pdeoajlh4ttgktolu3jir8gp6"
            self.update_url = "https://sso-stage.nylservices.net/update-profile?clientId=6pdeoajlh4ttgktolu3jir8gp6&callbackUri=https://google.com"

        warnings.simplefilter("ignore", ResourceWarning)
        # self.driver = webdriver.Remote(
        #    command_executor='http://192.168.86.26:4444/wd/hub',
        #    desired_capabilities= {
        #        "browserName": "chrome",
        #        "version": "",
        #        "platform": "ANY",
        #        "javascriptEnabled": True,
        #        'chromeOptions': {
        #            'useAutomationExtension': False,
        #            'args': ['--disable-infobars']
        #        }
        #   })
        # self.server = Server("/Users/browsermob-proxy-2.1.4/bin/browsermob-proxy", options={'port': 8090})
        # self.server.start()

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--proxy-server={0}".format(self.reg_url))
        chrome_options.add_argument("--incognito")
        # chrome_options.add_argument("--window-size=1366,768")
        chrome_options.add_argument("--window-size=1440,900")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(20)
        # self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        """The tearDown method will get called after every test method. This is a place to do all cleanup actions."""
        # NOTE: this code for checking for exceptions does NOT work for Safari
        # Python 3.8+ may have this built in. Need to revisit at future date.
        # checking for exceptions or assertion errors, if there are take screenshot
        # for method, error in self._outcome.errors:
        #     if error:
        #         funct.fullshot(self.driver)
        #         funct.generateHAR(self.server, self.driver)
        # self.driver.quit()
        self.assertEqual([], self.verificationErrors)

# ###==============================================================###
# # NYL AWS
# ###==============================================================###
# class NYawsBASE(unittest.TestCase):
#     # report = globalVar.report
#     # testdata = globalVar.testdata
#
#     def setUp(self):
#         """The setUp is part of initialization, this method will get called before every test function which you
#         are going to write in the test case class.
#
#         Here you are creating the instance of Chrome WebDriver with specific test configurations needed for
#         testing AWS web application.
#         """
#         self.env = globalVar.env
#
#         self.aws_login_url = "https://nyl-sso.signin.aws.amazon.com/console"
#         warnings.simplefilter("ignore", ResourceWarning)
#         chrome_options = webdriver.ChromeOptions()
#         # chrome_options.add_argument("--proxy-server={0}".format(self.reg_url))
#         chrome_options.add_argument("--incognito")
#         # chrome_options.add_argument("--window-size=1366,768")
#         chrome_options.add_argument("--window-size=1440,900")
#         self.driver = webdriver.Chrome(options=chrome_options)
#         self.driver.implicitly_wait(20)
#         self.verificationErrors = []
#         self.accept_next_alert = True
#         if self.env == 'dev':
#             self.reg_url = "https://sso-dev.nylservices.net/?clientId=29d5np06tgg87unmhfoa3pkma7&callbackUri=https://google.com"
#             self.login_url = "https://sso-dev.nylservices.net/login?clientId=29d5np06tgg87unmhfoa3pkma7&callbackUri=https://google.com"
#             self.reset_url = "https://sso-dev.nylservices.net/reset-password?clientId=29d5np06tgg87unmhfoa3pkma7"
#             self.update_url = "https://sso-dev.nylservices.net/update-profile?clientId=29d5np06tgg87unmhfoa3pkma7&callbackUri=https://google.com"
#         elif self.env == 'qa':
#             self.reg_url = "https://sso-qa.nylservices.net/?clientId=4a0p01j46oms3j18l90lbtma0o&callbackUri=https://google.com"
#             self.login_url = "https://sso-qa.nylservices.net/login?clientId=4a0p01j46oms3j18l90lbtma0o&callbackUri=https://google.com"
#             self.reset_url = "https://sso-qa.nylservices.net/reset-password?clientId=4a0p01j46oms3j18l90lbtma0o"
#             self.update_url = "https://sso-qa.nylservices.net/update-profile?clientId=4a0p01j46oms3j18l90lbtma0o&callbackUri=https://google.com"
#         elif self.env == 'stage':
#             self.reg_url = "https://sso-stage.nylservices.net/?clientId=6pdeoajlh4ttgktolu3jir8gp6&callbackUri=https://google.com"
#             self.login_url = "https://sso-stage.nylservices.net/login?clientId=6pdeoajlh4ttgktolu3jir8gp6&callbackUri=https://google.com"
#             self.reset_url = "https://sso-stage.nylservices.net/reset-password?clientId=6pdeoajlh4ttgktolu3jir8gp6"
#             self.update_url = "https://sso-stage.nylservices.net/update-profile?clientId=6pdeoajlh4ttgktolu3jir8gp6&callbackUri=https://google.com"
#
#     def tearDown(self):
#         """The tearDown method will get called after every test method. This is a place to do all cleanup actions."""
#         # NOTE: this code for checking for exceptions does NOT work for Safari
#         # Python 3.8+ may have this built in. Need to revisit at future date.
#         # checking for exceptions or assertion errors, if there are take screenshot
#         # for method, error in self._outcome.errors:
#         #     if error:
#         #         funct.fullshot(self.driver)
#         #         funct.generateHAR(self.server, self.driver)
#         # self.driver.quit()
#         self.assertEqual([], self.verificationErrors)

##Test Runner:
#In python3 you can run discover mode from the terminal without any code changes, the code to run is as folloew:
#$python3 -m unittest discover -s <project_directory> -p "<starting_syntax>*.py"
#EG:
#$python3 -m unittest discover -s nyl/ -p "reg*.py" 
#would, assuming you were in the QA/ directory, run all test-cases on all files that began with "reg" in the nyl/ folder 