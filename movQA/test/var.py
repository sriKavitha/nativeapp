# [Documentation - Setup] This section lists all dependencies
# that are imported for variable file to work
from selenium.webdriver.common.by import By
import funct

# [Documentation - Summary] This file creates the variables for
#MOV e2e testing

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
   

   
   
class homePage:
    allowB2 = [By.XPATH, '//*[@name="Allow While Using App"]', "allow button 2"]
    allowB = [By.XPATH, '//*[@name="Allow"]', "allowButton"]
    homeB = [By.XPATH, '//*[@name="home"]', "homeButton"]
    searchB = [By.XPATH, '//*[@name="search"]', "searchButton"]
    addB = [By.XPATH, '//*[@name="add"]', "addButton"]
    notificationB = [By.XPATH, '//*[@name="notification"]', "notificationButton"]
    ticketB = [By.XPATH, '(//XCUIElementTypeButton)[1]', "TicketButton"]
    ticketV = [By.XPATH, '//*[@elementId="2D000000-0000-0000-5D0C-000000000000"]', "ticketValue"]
    newShareB = [By.XPATH, '//*[@name="newShare"]', "newShareButton"]
    raffleB = [By.XPATH, '(//*[@name="newTicketon"]//parent::*)[2]', "raffle entry button"]
    ticketCostV = [By.XPATH, '//*[@elementId="37000000-0000-0000-5D0C-000000000000"]', "ticketCostValue"]

class tickets:
    buyMoreB = [By.XPATH, '//*[@name="Buy more"]', "buy tickets button"]
    tix1 = [By.XPATH, '//*[@name="1"]', "1 ticket choice"]
    tix5 = [By.XPATH, '//*[@name="5"]', "5 ticket choice"]
    tix10 = [By.XPATH, '//*[@name="10"]', "10 ticket choice"]
    tix15 = [By.XPATH, '//*[@name="15"]', "15 ticket choice"]
    tix25 = [By.XPATH, '//*[@name="25"]', "25 ticket choice"]               
    tix50 = [By.XPATH, '//*[@name="50"]', "50 ticket choice"]
    tixPlus = [By.XPATH, '//*[@name="+"]', "+ ticket choice"]
    nextB = [By.XPATH, '//*[@name="Next"]', "next button"]
    buyB = [By.XPATH, '//*[@name="Buy"]', "buy button"]
    cancelB = [By.XPATH, '//*[@name="Cancel"]', "cancel button"]
    buyTixF = [By.XPATH, '(//XCUIElementTypeTextField)', 'buy tickets field']
    buyTixError1 = [By.XPATH, '(//*[@name="Bulk purchase requires more than 100 tickets"])[1]', "bulk purchase error message"]
    ccF = [By.XPATH, '//*[@name="Credit or debit card number"]', "cc field"]
    ccExpF = [By.XPATH, '//*[@name="Credit or debit card expiration date"]', "cc experiation field"]
    payB = [By.XPATH, '//*[@name="Pay"]', "cc pay button"]
    testCC = '4242424242424242112512311385'
    doneB = [By.XPATH, '(//*[@name="Done"])[4]', "done button"]
    okB = [By.XPATH, '(//*[@name="Ok"])[1]', "OK button"]
    ticketCount = [By.XPATH, '(//*[@type="XCUIElementTypeStaticText"])[2]', "ticket count"]
    
class raffle:
    secondNumber = 'TouchAction(driver).tap(x=211, y=371).perform()'
    xB = [By.XPATH, '//*[@name="arrow left 1"]', "xButton"]
    selectB = [By.XPATH, '//*[@name="Select"]', "select Button"]
    customB = [By.XPATH, '//*[@name="Enter Custom Amount"]', "enter custom amount Button"]
    dontAllowB = [By.XPATH, '(//XCUIElementTypeButton)[1]', "don't allow button"]
    okB = [By.XPATH, '(//XCUIElementTypeButton)[2]', "ok button"]
    okB2 = [By.XPATH, '//XCUIElementTypeButton[@name="Ok"]', 'single okay button']
    #customF = [By.XPATH, '(//*[@type="XCUIElementTypeTextField"])[1], "custom tickets field']
    customF = [By.XPATH, '//XCUIElementTypeApplication[@name="Mov"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField', "ticketCostValue"]

    customE1 = [By.XPATH, '(//*[@name="Custom ticket amount should be more than 50"])[1]', "buy more error"]
    customE2 = [By.XPATH, '(//*[@name="You need more tickets!"])[1]', "need more error"]
    reloadB = [By.XPATH, '//*[@name="Reload Tickets"]', "reload Button"]
    cancelB = [By.XPATH, '//*[@name="Cancel"]', "cancel reload Button"]
    
    
    
    

