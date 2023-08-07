import unittest, time, re       #unittest is the testing framework, provides module for organizing test cases
import var, funct, util, confTest, HtmlTestRunner   #Custom class for NYL
import imaplib
import email
import re
from io import StringIO
import sys

class NYlotto(confTest.NYlottoBASE):


    def test_01_forgotPassword(self):
        """Verifies that  user can reset password and login with new password.

        Jira ticket - https://rosedigital.atlassian.net/browse/NYL-2408

        Submits a forgot password request, opens the subsequent email, changes password.
        Verifies new password works with a login attempt.
        :return:
        """
        testenv = self.env
        print("TESTING " + testenv + " ENVIRONMENT")
        print("\nChecks password reset functionality")
        testemail = self.testemail
        #set term that emails will be filtered by
        subjectFilter = "NYL SSO Password Reset Request"
        oldUrl = self.returnEmailLink(var.credsSSOWEB.imapEmail,var.credsSSOWEB.imapPW, "NYL SSO Password Reset Request")
        driver = self.driver
        # creates a verified user with valid SSN4
        funct.createVerifiedUser(self, testemail)
        print('\n----------\n' + 'Test setup')
        driver.get(self.login_url)
        funct.waitAndClick(driver, var.loginV.forgot_password_link)
        funct.waitAndFind(driver, var.resetPswV.email)
        funct.waitAndSend(driver, var.resetPswV.email, 'x')
        funct.waitAndClick(driver, var.resetPswV.reset_submit_button)
        funct.verifyErrorText(driver, var.resetPswV.error1, var.resetPswV.error1Stub)
        funct.verifyErrorText(driver, var.resetPswV.error2, var.resetPswV.error2Stub)
        funct.clearTextField(driver, var.resetPswV.email)
        funct.waitAndSend(driver, var.resetPswV.email, self.testemail)
        funct.waitAndClick(driver, var.resetPswV.reset_submit_button)
        funct.waitAndFind(driver, var.resetPswV.success)
        newUrl = self.returnEmailLink(var.credsSSOWEB.imapEmail,var.credsSSOWEB.imapPW, subjectFilter)
        #logging for problem solving
        # print(oldUrl)
        # print(newUrl)
        #checks to make sure new confirm pw email has been received 
        while oldUrl == newUrl:
            # print(str(oldUrl))
            # print('equals') 
            # print(str(newUrl))
            time.sleep(3)
            newUrl = self.returnEmailLink(var.credsSSOWEB.imapEmail,var.credsSSOWEB.imapPW, subjectFilter)
        #print(newUrl)
        #takes you to verification email
        driver.get(newUrl[0])
        #changes pw
        funct.waitAndClick(driver, var.resetPswV.resetPwButton)
        funct.verifyErrorText(driver, var.resetPswV.resetError, var.resetPswV.resetErrorStub)
        funct.waitAndSend(driver, var.resetPswV.newPwField, "Test1234!")
        funct.waitAndClick(driver, var.resetPswV.resetPwButton)
        funct.verifyErrorText(driver, var.resetPswV.matchError, var.resetPswV.matchErrorStub)
        funct.clearTextField(driver, var.resetPswV.newPwField)
        funct.waitAndSend(driver, var.resetPswV.newPwField, var.credsSSOWEB.tempPW)
        funct.waitAndSend(driver, var.resetPswV.confirmPwField, var.credsSSOWEB.tempPW)
        funct.waitAndClick(driver, var.resetPswV.resetPwButton)
        funct.waitUntil(driver, var.resetPswV.success)

        #checks changed pw
        driver.get(self.login_url)
        # Login attempt
        funct.waitAndSend(driver, var.loginV.email, testemail)
        funct.waitAndSend(driver, var.loginV.password, var.credsSSOWEB.password)
        funct.waitAndClick(driver, var.loginV.login_button)
        funct.waitAndFind(driver, var.resetPswV.error2)
        funct.clearTextField(driver, var.loginV.password)
        funct.waitAndSend(driver, var.loginV.password, var.credsSSOWEB.tempPW)
        funct.waitAndClick(driver, var.loginV.login_button)
        funct.verifyRedirect(self, driver, testemail, var.resetPswV.google)

        print("Test completed successfully, cleaning up!")

        #puts pw back to original pw, and makes sure it works
        oldUrl = self.returnEmailLink(var.credsSSOWEB.imapEmail,var.credsSSOWEB.imapPW, "NYL SSO Password Reset Request")
        driver.get(self.login_url)
        funct.waitAndClick(driver, var.loginV.forgot_password_link)
        funct.waitAndFind(driver, var.resetPswV.email)
        funct.waitAndSend(driver, var.resetPswV.email, self.testemail)
        funct.waitAndClick(driver, var.resetPswV.reset_submit_button)
        funct.waitAndFind(driver, var.resetPswV.success)
        newUrl = self.returnEmailLink(var.credsSSOWEB.imapEmail,var.credsSSOWEB.imapPW, "NYL SSO Password Reset Request")
        while oldUrl == newUrl:
            # print(str(oldUrl))
            # print('equals') 
            # print(str(newUrl))
            time.sleep(3)
            newUrl = self.returnEmailLink(var.credsSSOWEB.imapEmail,var.credsSSOWEB.imapPW, "NYL SSO Password Reset Request")

        driver.get(newUrl[0])
        funct.waitAndSend(driver, var.resetPswV.newPwField, var.credsSSOWEB.password)
        funct.waitAndSend(driver, var.resetPswV.confirmPwField, var.credsSSOWEB.password)
        funct.waitAndClick(driver, var.resetPswV.resetPwButton)
        funct.waitUntil(driver, var.resetPswV.success)
        driver.get(self.login_url)
        funct.waitAndSend(driver, var.loginV.email, testemail)
        funct.waitAndSend(driver, var.loginV.password, var.credsSSOWEB.password)
        funct.waitAndClick(driver, var.loginV.login_button)
        funct.waitAndFind(driver, var.resetPswV.google)
        #purges test user
        funct.purgeSSOemail(self, testemail)


    def returnEmailLink(self, un ,pw, subject1):
            m = imaplib.IMAP4_SSL("imap.gmail.com", 993)
            #m.login(var.credsSSOWEB.imapEmail,var.credsSSOWEB.imapPW)
            m.login(un,pw)
            m.list()
            ##decide whether you are looking in inbox or all mail
            # m.select('"[Gmail]/All Mail"')
            m.select('inbox')

            search = str('HEADER Subject "' + subject1 + '"')
            #print(search)
            result, data = m.uid('search', None, search) # (ALL/UNSEEN)
            #result, data = m.uid('search', None, 'HEADER Subject "NYL SSO Password Reset Request"') # (ALL/UNSEEN)
            
            i = len(data[0].split())
            for x in range(i):
                #print('x ' + str(x))
                if x == i-1:
                    latest_email_uid = data[0].split()[x]
                    result, email_data = m.uid('fetch', latest_email_uid, '(RFC822)')
                    # result, email_data = conn.store(num,'-FLAGS','\\Seen') 
                    # if you need to look only at unseen emails etc
                    raw_email = email_data[0][1]
                    raw_email_string = raw_email.decode('utf-8')
                    email_message = email.message_from_string(raw_email_string)
                    #print(raw_email_string)
                    # output_file = open('test.txt', 'w')
                    # output_file.write(raw_email_string)
                    # output_file.close()

                    url = re.findall(r'href=[\'"]?([^\'" >]+)', raw_email_string)
                    print(url)
                    return url
                

# use "report" variable in conftest.py to change report style on runner
if __name__ == "__main__":
    if confTest.NYlottoBASE.report == "terminal":
        unittest.main(warnings='ignore')
    elif confTest.NYlottoBASE.report == "html":
        unittest.main(warnings='ignore', testRunner=HtmlTestRunner.HTMLTestRunner(output='<html_report_dir>'))