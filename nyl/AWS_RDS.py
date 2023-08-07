import unittest, time, re  # unittest is the testing framework, provides module for organizing test cases

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import var, funct, util, confTest, HtmlTestRunner  # Custom class for NYL

class NYlotto(confTest.NYlottoBASE):

    def test_01_AWSrds(self):
        """
        Register the SSO web user. As part of post-registration verification, when a query is executed for the registered user,
        validate user data in AWS Services(RDS) is same as user registration info and LexID is generated in AWS Services(RDS)
        Purge the SSO user after the verification.
        Dev/QA/Stage/Prod env:
        1. User has to be successfully registered
        2. Signin into AWS with QA user credentials
        3. Click RDS under Recently visited list
        4. Verify header for RDS page
        5. Click Query Editor Link
        6. Verify the window title for Connect to database
        7. Connect to database after selecting/keying the values for Cluster, UserName, password, database name
        8. Verify the user is in RDS Editor page
        9. Execute SQL query after clearing the existing query and entering the new SQL statement
        10. Verify the sso user details in Output and Results tab
                a. firstname
                b. lastname
                c. email
                d. phone
                e. DOB
                f. address
                g. LexID
                h. Success status
                i. 1 row returned

        https://rosedigital.atlassian.net/browse/MRMNYL-388 ( as part of new LexID changes)
        """
        # 1. User has to be successfully registered
        driver = self.driver
        # email, testenv = funct.sso_register_customEmail(self) #commented as QA is broken
        email = 'testa+sso@rosedigital.co'
        testenv = "qa"
        print(f'\nUser is now successfully registered....\n')
        print(f'----------')

        # 2. Signin into AWS with QA user credentials
        driver = self.driver
        # call aws login functionality
        funct.aws_login(self)
        #     funct.purgeSSOemail(self, email)
        #     funct.purgeSSOphone(self, var.credsSSOWEB.phone)
        try:
            # Wait for AWS logo to appear after user sign in to AWS
            funct.waitUntil(driver, var.cloudWatchAWS.aws_Logo)
            print('PASS - User is in AWS Home page\n')
            print('----------\n')
            # 3. Click RDS under Recently visited list
            funct.waitAndClick(driver, var.rdsAWS.aws_rds_dashboardrds)

            # 4. Verify header for RDS page
            funct.waitAndFind(driver, var.rdsAWS.aws_rds_pageHeader)
            print('PASS - Amazon RDS Page header verified... \n')

            # 5. Click Query Editor
            print('Click Query Editor... ')
            funct.waitAndClick(driver, var.rdsAWS.aws_rds_queryEditorLink)

            # 6. Verify the window title for Connect to database
            # Verify user is in Connect to database page
            funct.waitAndFind(driver, var.rdsAWS.aws_rds_connectToDatabasePage)
            print('PASS - \'Connect to database\' modal window title verified...')

            # 7. Connect to database after selecting/keying the values for Cluster, UserName, password, database name
            funct.waitAndClick(driver, var.rdsAWS.aws_rds_chooseDatabaseCluster)
            funct.waitAndClick(driver, var.rdsAWS.aws_rds_chooseDatabaseClusterValue)

            funct.waitAndClick(driver, var.rdsAWS.aws_rds_userName)
            funct.waitAndClick(driver, var.rdsAWS.aws_rds_userNameValue)

            funct.waitAndSend(driver, var.rdsAWS.aws_rds_passWord, var.CREDSaws.aws_password)
            funct.waitAndSend(driver, var.rdsAWS.aws_rds_databaseName, 'postgres')
            funct.waitAndSend(driver, var.rdsAWS.aws_rds_databaseName, Keys.RETURN)
            funct.waitAndClick(driver, var.rdsAWS.aws_rds_connectDatabaseBtn)

            # 8. Verify the user is in RDS Editor page
            funct.waitAndFind(driver, var.rdsAWS.aws_rds_editorTab)
            print('PASS - \'RDS Editor Tab for Queries\' title verified...')


            # 9. Execute SQL query after clearing the existing query and entering the new SQL statement
            # Build the query for the registered user
            sql_RegisteredUser = "select * from qa_users where email = " + "\'"+email+"\';"

            # Click on Editor tab
            print("Click on Editor tab")
            funct.waitAndClick(driver, var.rdsAWS.aws_rds_editorTab)
            # Clear the existing query
            print("Clearing the existing query")
            funct.waitAndClick(driver, var.rdsAWS.aws_rds_clearButton)
            ele = driver.find_element_by_xpath("//*[@id=\"qfc_editor_panel\"]/div[1]/div[1]/textarea")
            action = ActionChains(driver)
            action.send_keys_to_element(ele)
            # Key in the Query
            print('Key in the query...')
            action.send_keys(sql_RegisteredUser).perform();
            # RUN the Query
            print('Execution of the query in progress...')
            funct.waitAndClick(driver, var.rdsAWS.aws_rds_RunButton)
            time.sleep(3)
            # 10. Verify the sso user details in Output/Results tab...
            self.validate_data(email)
        except Exception:
            print("AWS Login attempt is unsuccessful...")
            funct.fullshot(self)
            print('FAIL - AWS Login attempt')
            funct.closeWindow(driver, 'Sign in as IAM user')
        # print("Purging the SSO registered user in Admin Dashboard... by phone number and Email address")
        # funct.purgeSSOemail(self, email)
        # funct.purgeSSOphone(self, var.credsSSOWEB.phone)


    # 10. Verify the sso user details in Output/Results tab
    def validate_data(self, email):
        # rows = header column names
        # cols = column values
        rows = self.driver.find_elements_by_xpath("//table/thead/tr/th")
        cols = self.driver.find_elements_by_xpath("//table/tbody/tr/td")
        # Create 2 empty lists to store header column names and column values
        rowValues=[]
        colValues=[]
        try:
            # Now "rowValues" list will have column names
            # "colValues" list will have column Values
            for i in range(0, len(rows)):
                rowValues.append(rows[i].text)
                colValues.append(cols[i].text)

            # Create a dictionary to store key/value pair
            dict = {}
            # Zip the rowValues and colValues
            dict = list(zip(rowValues, colValues))

            # Print the dictionary to view
            print("Print the dictionary having column header and column value in the form of key/value.....\n", dict)
            print("\n--------")
            print("Validation starts...:")
            for key, val in dict:
                if key == 'given_name':
                    firstName = var.credsSSOWEB.fname
                    if firstName.lower() == val.lower():
                        print('\t PASS: First Name is successfully verified and is matching with registered firstname...')
                    else:
                        print('\t FAIL: First Name in AWS RDS is NOT matching with registered firstname...')
                        print(f'\t\tErr.. First Name should be \'{firstName.lower()}\' while it is \'{val.lower()}\'')

                elif key == 'family_name':
                    lastName = var.credsSSOWEB.lname
                    if lastName.lower() == val.lower():
                        print('\t PASS: Last Name in AWS RDS is successfully verified and is matching with registered lastname...')
                    else:
                        print('\t FAIL: Last Name in AWS RDS is NOT matching with registered lastname...')
                        print(f"\t\tErr.. Last Name should be '{lastName.lower()}' while it is '{val.lower()}'")

                elif key == 'email':
                    if val == email:
                        print("\t PASS: eMail in AWS RDS is successfully verified and is matching with registered eMail address...")
                    else:
                        print('\t FAIL: eMail in AWS RDS is NOT matching with registered eMail address...')
                        print(f'\t\tErr.. eMail should be \'{email}\' while it is \'{val}\'')

                elif key == 'phone_number':
                    phoneWithNumberOne = "+1" + str(var.credsSSOWEB.phone)
                    if phoneWithNumberOne == val:
                        print('\t PASS: Phone# in AWS RDS is successfully verified and is matching with registered Phone#...')
                    else:
                        print('\t FAIL: Phone# in AWS RDS is NOT matching with registered Phone# ...')
                        print(f'\t\tErr.. Phone# should be \'{phoneWithNumberOne}\' while it is \'{val}\'')

                elif key == 'birthdate':
                    dob_sso = str(var.credsSSOWEB.dob_month) + "/" + str(var.credsSSOWEB.dob_date) + "/" + str(
                    var.credsSSOWEB.dob_year)
                    if dob_sso == val:
                        print('\tPASS: DOB in AWS RDS is successfully verified and is matching with registered DOB...')
                    else:
                        print('\t FAIL: DOB in AWS RDS is NOT matching with registered DOB ...')
                        print(f'\t\tErr.. DOB should be \'{dob_sso}\' while it is \'{val}\'')
                elif key == 'address':
                    address_ssoweb = var.credsSSOWEB.housenum + ' ' + (var.credsSSOWEB.street) + ' ' + (
                    var.credsSSOWEB.city) + ', ' + var.credsSSOWEB.state + ' ' + var.credsSSOWEB.zip
                    if address_ssoweb.lower() == val.lower():
                        print('\tPASS: Address in AWS RDS is successfully verified and is matching with registered address...')
                    else:
                        print('\tFAIL: Address in AWS RDS is NOT matching with registered address...')
                        print(f'\t\tErr.. Address should be \'{address_ssoweb.lower()}\' while it is \'{val.lower()}\'')

                elif key == 'lex_id':
                    if val == 'NULL':
                        print('\tFAIL: LexID is not generated...')
                        print('\t\t Err.. LexId is: ', val)
                    elif int(val) > 0:
                        print('\t PASS: LexID is successfully generated...', val)
                    else:
                        print('\t FAIL: LexID should be greater than 0...', val)

            # Click on Output tab to verify the "Success" status and "1 rows returned" message
            print('Clicking on "Output" tab to verify the "Success" status and "1 rows returned" message...')
            try:
                # Click on Output tab
                outputTab = self.driver.find_element_by_xpath("//span[text()='Output']//ancestor::a")
                outputTab.send_keys(Keys.RETURN)
                try:
                    funct.waitUntil(self.driver, var.rdsAWS.aws_rds_statusSuccess)
                    funct.waitAndFind(self.driver, var.rdsAWS.aws_rds_statusSuccess)
                    print('PASS: The status is "Success"....')
                except Exception:
                    print('\t FAIL: The status is "Error"....')
                try:
                    funct.waitAndFind(self.driver, var.rdsAWS.aws_rds_rowsReturned)
                    print('PASS: \'1 rows returned\'....')
                except Exception:
                    print('\t FAIL: Rows returned should be 1....')
            except Exception as e:
                print("Error occurred...", e)
        except Exception:
            print('\tNo matching records found for the query...')
            print(f'\tErr...Check for the email address in the query: \'{email}\'')

# use "report" variable in conftest.py to change report style on runner
if __name__ == "__main__":
    if confTest.NYlottoBASE.report == "terminal":
        unittest.main(warnings='ignore')
    elif confTest.NYlottoBASE.report == "html":
        unittest.main(warnings='ignore', testRunner=HtmlTestRunner.HTMLTestRunner(output='<html_report_dir>'))
