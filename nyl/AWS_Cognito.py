import unittest, time, re  # unittest is the testing framework, provides module for organizing test cases
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import var, funct, util, confTest, HtmlTestRunner  # Custom class for NYL

class NYlotto(confTest.NYlottoBASE):

    def test_01_AWSCognito(self):
        """
        Register the SSO web user. As part of post-registration verification, validate user data in AWS Cognito
        is same as user registration info and LexID is generated in AWS Services(Cognito)
        Purge the SSO user after the verification.
        Dev/QA/Stage/Prod env:
        1. User has to be successfully registered (pre-requisite)
        2. Signin into AWS with QA user credentials
        3. Search and select Cognito
        4. Verify the page header
        5. Click Manage User Pools > qa-nyl-sso-pools
        6. Click Users and groups
        7. From dropdown select the option Email
        8. Key in the registered email and hit enter key to search
        9. Check if there are users for the matching email address
        10. Click the link under the Username only if there is a match for the email
        11. Verify the firstname, lastname, address, DOB, phone#, email and LexID in Users page
            a. firstname
            b. lastname
            c. address
            d. DOB
            e. phone
            f. email
            g. LexID
        https://rosedigital.atlassian.net/browse/MRMNYL-388 (as part of new LexId changes)
        """

        # 1. User has to be successfully registered (pre-requisite)
        driver = self.driver
        # email, testenv = funct.sso_register_customEmail(self)
        email = "testa+sso@rosedigital.co"
        testenv = "qa"
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

            # 3.Search and select Cognito from Services
            print('Click on \'Services\' in AWS homepage')
            funct.waitAndClick(driver, var.cloudWatchAWS.aws_services)
            print('In the search textbox, type \'Cognito\'')
            funct.waitAndSend(driver, var.cloudWatchAWS.aws_services_search, "cognito")
            print('Click \'Cognito\' under Services option')
            funct.waitAndClick(driver, var.cognitoAWS.aws_cognito_search);
            # 4. Verify the page header
            funct.waitAndFind(driver, var.cognitoAWS.aws_cognito_cognitoPageHeader)
            print('PASS - Amazon Cognito Page header verified... ')

            # 5. Click Manage User Pools > qa-nyl-sso-pools (based on env)
            print('Click on \'Manage User Pools\' in Amazon Cognito page')
            funct.waitAndClick(driver, var.cognitoAWS.aws_cognito_ManageUserPools)
            print('Click on \'QA-sso-pool\'')
            funct.waitAndClick(driver, var.cognitoAWS.aws_cognito_userPool)

            # 6. Click Users and groups
            print('Click on Users and groups')
            funct.waitAndClick(driver, var.cognitoAWS.aws_cognito_usersAndGroups)

            # 7. From dropdown select the option Email
            print('Select the option \'Email\' from the dropdown menu')
            funct.waitAndClick(driver, var.cognitoAWS.aws_cognito_userNameDropdown)
            funct.waitAndClick(driver, var.cognitoAWS.aws_cognito_selectEmailOption)

            # 8. Key in the registered email and hit enter key to search
            print('Key in the registered email and hit Enter key to search')
            funct.waitAndSend(driver, var.cognitoAWS.aws_cognito_inputSearch, email)
            funct.waitAndSend(driver, var.cognitoAWS.aws_cognito_inputSearch, Keys.RETURN)
            time.sleep(1)

            # 9. Check if there are users for the matching email address
            count = driver.find_elements_by_xpath("//table[@class='cog-user-table']/tbody/tr/td")
            if len(count) == 1:
                # No users found, so just display the below text to indicate no users found
                print('No users found for this email... ' + '"' + email + '"')
                print('Key in the correct Email...')
            else:
                # Users found and perform below steps...
                temp_xpath = '//table[@class=\'cog-user-table\']//td[contains(text(),'
                email_xpath = temp_xpath + "'" + email + "')]"
                userEmail = [By.XPATH, email_xpath]
                # Verify the userEmail with the search email keyed in
                funct.waitAndFind(driver, userEmail)
                print('-------')
                print('PASS - Email is verified with the search email keyed in User Pools page...')

                # 10. Click the link under the Username only if there is a match for the email
                print('Clicked the link to verify other details...')
                funct.waitAndClick(driver, var.cognitoAWS.aws_cognito_emailRow)
                time.sleep(3)
                # call verify details
                self.verify_details(email);

        except Exception as e:
            print('Error occurred...', e)
            funct.fullshot(self)
            funct.closeWindow(driver, 'Sign in as IAM user')
        # print("Purging the SSO registered user in Admin Dashboard... by phone number and Email address")
        # funct.purgeSSOemail(self, email)
        # funct.purgeSSOphone(self, var.credsSSOWEB.phone)

    # 11. Verify the firstname, lastname, address, DOB, phone#, email and LexID  in Users page
    def verify_details(self, email):
        # a. Verify firstname => SSO web - First name with AWS cognito - First name
        firstName = funct.waitAndGetText(self.driver, var.cognitoAWS.aws_cognito_firstName)
        if var.credsSSOWEB.fname == firstName.capitalize():
            print('PASS: First Name is successfully verified and is matching with registered firstname...')
        else:
            print('FAIL: First Name in AWS cognito is NOT matching with registered firstname...')
            print(f'\tErr.. First name should be \'{var.credsSSOWEB.fname}\' while it is \'{firstName.capitalize()}\'')
        # print(f"Unverified user account {email} successfully created.")

        # b. Verify lastname => SSO web - Last name with AWS cognito - Last name
        lastName = funct.waitAndGetText(self.driver, var.cognitoAWS.aws_cognito_lastName)
        if var.credsSSOWEB.lname == lastName.capitalize():
            print('PASS: Last Name in AWS cognito is successfully verified and is matching with registered lastname...')
        else:
            print('FAIL: Last Name in AWS cognito is NOT matching with registered lastname...')
            print(f'\tErr.. Last name should be \'{var.credsSSOWEB.lname}\' while it is \'{lastName.capitalize()}\'')

        # c. Verify Address => SSO web - address with AWS cognito - Address
        address_ssoweb = var.credsSSOWEB.housenum + ' ' + var.credsSSOWEB.street + ' ' + var.credsSSOWEB.city + ', ' + var.credsSSOWEB.state + ' ' + var.credsSSOWEB.zip
        address_aws = funct.waitAndGetText(self.driver, var.cognitoAWS.aws_cognito_address)
        if address_ssoweb.lower() == address_aws.lower():
            print('PASS: Address in AWS cognito is successfully verified and is matching with registered address...')
        else:
            print('FAIL: Address in AWS cognito is NOT matching with registered address...')
            print(f'\tErr.. Address should be \'{address_ssoweb.lower()}\' while it is \'{address_aws.lower()}\'')


        # d. Verify DOB => SSO web - DOB with AWS cognito - DOB
        dob_aws = funct.waitAndGetText(self.driver, var.cognitoAWS.aws_cognito_birthdate)
        dob_sso = str(var.credsSSOWEB.dob_month) + "/" + str(var.credsSSOWEB.dob_date) + "/" + str(var.credsSSOWEB.dob_year)
        if dob_sso == dob_aws:
            print('PASS: DOB in AWS cognito is successfully verified and is matching with registered DOB...')
        else:
            print('FAIL: DOB in AWS cognito is NOT matching with registered DOB ...')
            print(f'\tErr.. DOB should be \'{dob_sso}\' while it is \'{dob_aws}\'')

        # e. Verify phone number => SSO web - phone number with AWS cognito - phone number
        phoneNum = funct.waitAndGetText(self.driver, var.cognitoAWS.aws_cognito_phoneNumber)
        phoneWithNumberOne = "+1" + str(var.credsSSOWEB.phone)
        if phoneWithNumberOne == phoneNum:
            print('PASS: Phone# in AWS cognito is successfully verified and is matching with registered Phone#...')
        else:
            print('FAIL: Phone# in AWS cognito is NOT matching with registered Phone# ...')
            print(f'\tErr.. Phone# should be \'{phoneWithNumberOne}\' while it is \'{phoneNum}\'')

        # f. Verify email address => SSO web - email with AWS cognito - email
        if email == funct.waitAndGetText(self.driver, var.cognitoAWS.aws_cognito_email):
            print('PASS: eMail in AWS cognito is successfully verified and is matching with registered eMail address...')
        else:
            print('FAIL: eMail in AWS cognito is NOT matching with registered eMail address...')
            print(f'\tErr.. Phone# should be \'{email}\' while it is \'{var.cognitoAWS.aws_cognito_email}\'')

        # g. Verify LexID
        try:
            lex = funct.waitAndGetText(self.driver, var.cognitoAWS.aws_cognito_lexId)
            print('PASS: LexID is successfully generated...', lex)
        except:
            print('FAIL: LexID is not generated...')

        print('\n ---------Registered \'SSO web user\' details are verified against \'AWS Cognito\'-----')

# use "report" variable in conftest.py to change report style on runner
if __name__ == "__main__":
    if confTest.NYlottoBASE.report == "terminal":
        unittest.main(warnings='ignore')
    elif confTest.NYlottoBASE.report == "html":
        unittest.main(warnings='ignore', testRunner=HtmlTestRunner.HTMLTestRunner(output='<html_report_dir>'))
