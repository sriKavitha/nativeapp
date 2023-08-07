# [Documentation - Setup] This section lists all dependencies
# that are imported for variable file to work
from selenium.webdriver.common.by import By
import funct

# [Documentation - Summary] This file creates the variables for
# NYL Single Sign On page objects for testing user flows

# [Documentation - Variables] Objects on Registration page
# Credentials for SSO Web user
class creds:
    # opens local file with user data
    notepadfile = open('/Users/Shared/testing/movCreds.txt', 'r')
    # turns variable into a list of every line in above notepadfile
    entry_info = notepadfile.read().splitlines()
    phone = funct.getCredential(entry_info, 'Phone-number')
    password = funct.getCredential(entry_info, 'password')
    authToken = funct.getCredential(entry_info, 'authToken')
    authPW = funct.getCredential(entry_info, 'authPW')
# Reg page elements
class signIn:
    doneB = [By.XPATH, '//*[@name="Done"]', "doneButton"]
    xB = [By.XPATH, '//*[@name="arrow left 1"]', "xButton"]
    registerB = [By.XPATH, '//*[@name="Register"]', "registerButton"]
    loginB = [By.XPATH, '//*[@name="Login"]', "LoginButton"]
    pwF = [By.XPATH, '//*[@type="XCUIElementTypeSecureTextField"]', "pwField"]
    numF = [By.XPATH, '//*[@type="XCUIElementTypeTextField"]', "phoneNumberField"]
    invalidPhoneNumber = [By.XPATH, '//*[@name="Invalid Phone Number"]', "Invalid Phone Number error"]
    noPwError = [By.XPATH, '//*[@name="Password field cannot be empty"]', "No PW error"]
    invalidData = [By.XPATH, '//*[@name="Your login data is not correct"]', "Invalid Data error"]
    okB = [By.XPATH, '//*[@name="Ok"]', "okButton"]
    continueB = [By.XPATH, '//*[@name="Continue"]', "continueButton"]
    newShareB = [By.XPATH, '//*[@name="newShare"]', "newShareButton"]
    newShareB = [By.XPATH, '//*[@name="newShare"]', "newShareButton"]

class register:
    username = "Qa5"
    usedNumber = "3185456266"
    registerB = [By.XPATH, '//*[@name="Register"]', "registerButton"]
    backArrow = [By.XPATH, '//*[@name="backArrow"]', "backArrow"]
    okB = [By.XPATH, '(//*[@name="Ok"])[1]', "OK button"]
    unField = [By.XPATH, '//*[@type="XCUIElementTypeTextField"]', "user name field"]
    continueB = [By.XPATH, '(//*[@name="Continue"])[1]', "continue button"]
    unError1 = [By.XPATH, '(//*[@name="User name cannot be left empty"])[1]', "no blank UN error"] 
    unError2 = [By.XPATH, '(//*[@name="The user name must be at least 3 characters"])[1]', "must be at least 3 characters error"]
    phoneF = [By.XPATH, '(//XCUIElementTypeTextField)[2]', "phone number field"]
    phoneError1 = [By.XPATH, '//XCUIElementTypeStaticText[@name="Please enter a valid phone number to continue"]', "invalid Phone Number Error"]
    phoneError2 = [By.XPATH, '//XCUIElementTypeStaticText[@name="The phone has already been taken."]', "Already Used Phone Number Error"]
    pinF = [By.XPATH, '//*[@type="XCUIElementTypeTextField"]', "PinNumberField"]
    pinError1 = [By.XPATH, '//XCUIElementTypeStaticText[@name="OTP Field is empty"]', "Empty PIN field"]
    pinError2 = [By.XPATH, '//XCUIElementTypeStaticText[@name="The pin must be 4 digits."]', "pin must be 4 digits Error"]
    pinError3 = [By.XPATH, '//XCUIElementTypeStaticText[@name="Invalid PIN. Please try again."]', "invalid PIN Error"]
    pwField = [By.XPATH, '//*[@type="XCUIElementTypeSecureTextField"]', 'pw field']
    pwError1 = [By.XPATH, '//XCUIElementTypeStaticText[@name="Password Empty"]', "Empty PW field"]
    pwError2 = [By.XPATH, '//XCUIElementTypeStaticText[@name="Invalid Password"]', "Invalid PW field"]
    pwError3 = [By.XPATH, '//XCUIElementTypeStaticText[@name="OTP Field is empty"]', "Empty PW field"]


   
   
class homePage:
    allowB2 = [By.XPATH, '//*[@name="Allow While Using App"]', "allow button 2"]
    allowB = [By.XPATH, '//*[@name="Allow"]', "allowButton"]
    homeB = [By.XPATH, '//*[@name="home"]', "homeButton"]
    searchB = [By.XPATH, '//*[@name="search"]', "searchButton"]
    addB = [By.XPATH, '//*[@name="add"]', "addButton"]
    notificationB = [By.XPATH, '//*[@name="notification"]', "notificationButton"]
    ticketB = [By.XPATH, '//*[@name="Ticket"]', "TicketButton"]
    ticketV = [By.XPATH, '//*[@elementId="2D000000-0000-0000-5D0C-000000000000"]', "ticketValue"]
    newShareB = [By.XPATH, '//*[@name="newShare"]', "newShareButton"]
    ticketCostV = [By.XPATH, '//*[@elementId="37000000-0000-0000-5D0C-000000000000"]', "ticketCostValue"]

