import unittest, time, re  # unittest is the testing framework, provides module for organizing test cases
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import var, funct, util, confTest, HtmlTestRunner  # Custom class for NYL

class NYlotto(confTest.NYlottoBASE):

    def test_01_AWSCloudWatch(self):
        """
        Verify the logs in AWS(cloudwatch) after a SSO user is successfully registered in
        Dev/QA/Stage/Prod env:
        1. User has to be successfully registered
        2. Signin into AWS with QA user credentials
        3. Search and select CloudWatch from Services
        4. Click Logs > Log Groups
        5. Filter and Select the appropriate log groups based on environment
        6. Click the Search All Log Streams button and select 1hour button
        7. Key in the registered email in double quotation to search log events for the email
        8. Check if the userEmail has any event logs before verifying the success code/status/userEmail
        9. Click the Open all button only if there are event logs
        10. Verify the userEmail, Status SUCCESS, and Status Code

        https://rosedigital.atlassian.net/browse/MRMNYL-369
        https://rosedigital.atlassian.net/browse/MRMNYL-370 (Manual testcase for MRMNYL-369)

        """
        # 1. User has to be successfully registered
        driver = self.driver
        # email, testenv = funct.sso_register_customEmail(self) # if QA is stable, uncomment this line and comment testenv, email
        email = 'kavithatestdec5@rosedigital.co'
        testenv = 'qa'
        print('\nUser is now successfully registered....')
        print('----------')

        # 2. Signin into AWS with QA user credentials
        driver = self.driver
        # call aws login functionality
        funct.aws_login(self)
        try:
            # Wait for AWS logo to appear after user sign in to AWS
            funct.waitUntil(driver, var.cloudWatchAWS.aws_Logo)
            print('PASS - User is in AWS Home page')
            print('----------')

            # 3.Search and select CloudWatch from Services
            print('Click on \'Services\' in AWS homepage')
            funct.waitAndClick(driver, var.cloudWatchAWS.aws_services)
            print('In the search textbox, type \'CloudWatch\'')
            funct.waitAndSend(driver, var.cloudWatchAWS.aws_services_search, "cloudwatch")
            print('Click \'CloudWatch\' under Services option')
            funct.waitAndClick(driver, var.cloudWatchAWS.aws_cloudwatch_search);

            # 4. Click Logs > Log Groups
            print('Click on \'Logs\' in Cloud Watch page')
            funct.waitAndClick(driver, var.cloudWatchAWS.aws_logs)
            print('Navigate to \'Log Groups\' page upon clicking on \'Log groups\' link')
            funct.waitAndClick(driver, var.cloudWatchAWS.aws_logGroups)

            # 5. Filter and Select the appropriate log groups based on environment
            driver.switch_to.frame('microConsole-Logs')
            time.sleep(5)
            print('Keyin ' + "'" +testenv + '-postssoregisterverify\' in filter log groups textbox to search the required log groups')
            funct.waitUntilNot(driver, var.cloudWatchAWS.aws_logGroupsSearch)
            funct.waitAndSend(driver, var.cloudWatchAWS.aws_logGroupsSearch, testenv+'-postssoregisterverify')
            print('Click the ' + "'" + testenv + '-postssoregisterverify\' group name')
            time.sleep(5)
            funct.waitAndClick(driver, var.cloudWatchAWS.aws_logGroupsSearchResults)

            #  6. Click the Search All Log Streams button and select 1hour button to view the logs for the past 1 hour
            funct.waitAndClick(driver, var.cloudWatchAWS.aws_searchAllLogStreams)
            funct.waitAndClick(driver, var.cloudWatchAWS.aws_1hLogs)

            # 7. Key in the registered email in double quotation to search log events for the email
            print('Key in the email used for registration...')
            email_in_quotes = '"' + email + '"'
            funct.waitAndSend(driver, var.cloudWatchAWS.aws_logEventsSearch, email_in_quotes)
            time.sleep(2)
            funct.waitAndSend(driver, var.cloudWatchAWS.aws_logEventsSearch, Keys.RETURN)
            time.sleep(7)
            print("UserEmail keyed in...")

            # 8. Check if the userEmail has any event logs before verifying the success code/status/userEmail
            if funct.waitAndGetText(driver, var.cloudWatchAWS.aws_noEventsFound) != 'No events found':
                # 9. Click the Open all button only if there are event logs
                print("Click Open all log events button to verify the userEmail, status code and success...")
                funct.waitAndClick(driver, var.cloudWatchAWS.aws_openAll)
                print("Clicked open all events...")
                time.sleep(2)

                # 10. Verify the userEmail, Status SUCCESS, and Status Code
                funct.waitAndFind(driver, var.cloudWatchAWS.aws_logStatus_SUCCESS)
                funct.waitAndFind(driver, var.cloudWatchAWS.aws_logStatusCode_successCode)
                # build xpath for userEmail value to verify
                temp_xpath = '//span[@class=\'logs__events__json-string\'][contains(text(),'
                email_xpath = temp_xpath + "'" +email_in_quotes+ "')]"
                userEmail = [By.XPATH, email_xpath]
                # Verify the userEmail
                funct.waitAndFind(driver, userEmail)
                print('PASS - AWS CloudWatch logs are successfully verified for userEmail, "200" and "SUCCESS"...')
            else:
                print('No events found for this email... ' + email)
                print('User Email is incorrectly keyed in... or change the date/time')
        except Exception:
            print("AWS Login attempt is unsuccessful...")
            funct.fullshot(self)
            print('FAIL - AWS Login attempt')
            funct.closeWindow(driver, 'Sign in as IAM user')
        # print("Purging the SSO registered user in Admin Dashboard... by phone number and Email address")
        # funct.purgeSSOemail(self, email)
        # funct.purgeSSOphone(self, var.credsSSOWEB.phone)

# use "report" variable in conftest.py to change report style on runner
if __name__ == "__main__":
    if confTest.NYlottoBASE.report == "terminal":
        unittest.main(warnings='ignore')
    elif confTest.NYlottoBASE.report == "html":
        unittest.main(warnings='ignore', testRunner=HtmlTestRunner.HTMLTestRunner(output='<html_report_dir>'))
