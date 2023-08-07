# [Documentation - Setup] This section lists all dependencies
# that are imported for variable file to work
from selenium.webdriver.common.by import By
import funct
# [Documentation - Summary] This file creates the variables for
# NYL App objects for testing user flows

# [Documentation - Variables] Objects on Registration page

class CREDSmobile:
    # opens local file with user data
    notepadfile = open('/Users/Shared/testing/nyl02192020.txt', 'r')
    # turns variable into a list of every line in above notepadfile
    entry_info = notepadfile.read().splitlines()
    url = funct.getCredential(entry_info, 'all-games-target')
    xkey = funct.getCredential(entry_info, 'all-games-api-key')
    fname = funct.getCredential(entry_info, 'first-name')
    userName = funct.getCredential(entry_info, 'mobile-un')
    passWord = funct.getCredential(entry_info, 'mobile-pw')
    sauceUN = funct.getCredential(entry_info, 'sauce-un')
    saucePW = funct.getCredential(entry_info, 'sauce-pw')
class NYLdashboard:
    
    guest_b = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/guestButton"]']
    login_b = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/loginButton"]']
    register_b = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/loginRegister"]']
    guestCopy = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/guestCopy"]']
    loginCopy = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/loginCopy"]']
    forgotPwCopy = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/loginForgotPass"]']
    username_f = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/loginEmail"]']
    password_f = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/loginPassword"]']
    back_b = [By.XPATH, '//*[@content-desc="Navigate up"]']


    guestStub = 'Check winning numbers, prizes, and draw dates\nwithout a New York Lottery account'
    loginStub = 'Log in for the full Lottery experience, including access to Players Club and Second Chance Sweepstakes'
class NYLregistration:
    #main-fields
    base = [By.XPATH, '//*[@class="android.widget.FrameLayout"]']
    email_f = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/registerEmail"]']
    password_f = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/registerPassword"]']
    password_copy = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/registerPasswordError"]']
    confirmPW_f = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/registerConfirmPass"]']
    firstName_f = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/registerFirstName"]']
    phoneDropDown = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/registerPhoneType"]']
    phoneDropDown_HOME = [By.XPATH, '//*[@text="HOME"]']
    phoneDropDown_MOBILE = [By.XPATH, '//*[@text="MOBILE"]']
    phoneDropDown_WORK = [By.XPATH, '//*[@text="WORK"]']
    phone_f = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/registerPhone"]']
    age_copy = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/ageQuestion"]']
    age_stub = 'Are you 18 years or older?'
    yes_b = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/registerYes"]']
    nope_b = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/registerNo"]']
    zip_f = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/registerZip"]']
    newsletter_b = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/newsletter"]']
    reg_b = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/registerButton"]']
    #error fields
    email_e = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/registerEmailError"]']
    password_e = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/registerPasswordError"]']
    confirmPW_e = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/registerConfirmPassError"]']
    firstName_e = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/registerFirstNameError"]']
    lastName_e = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/registerLastNameError"]']
    phone_e = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/registerPhoneError"]']
    age_e = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/registerAgeError"]']
    zip_e = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/registerZipError"]']
    email_e_stub = "Please enter a valid email address."
    password_e_stub = "You'll need a password with at least eight characters and at least one number."
    confirmPW_e_stub = "Whoops! Passwords do not match."
    firstName_e_stub = "Let's try that again."
    lastName_e_stub =  "Let's try that again."
    phone_e_stub = "Re-enter number."
    age_e_stub = "You must be 18 years \nor older to sign up."
    zip_e_stub = "Invalid ZIP Code."
    #success screen variables
    pip1 = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/intro_indicator_0"]']    
    pip6 = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/intro_indicator_5"]']    
    getStarted_b = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/getStarted"]']

class NYLgamesDB:
    hamburger_b = [By.XPATH, '//*[@content-desc="Open Drawer"]']
    menu_GetNumbers = [By.XPATH, '(//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/txt_menu_title"])[4]']
    hamburger_home_copy = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/txt_menu_title"]']
    mainScreen = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/action_bar_root"]']
    allGames_b = [By.XPATH, '(//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/tabTitle"])[2]']
    MM_result1 = [By.XPATH, '(//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/gameBall"][1])']
    MM_result2 = [By.XPATH, '(//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/gameBall"][2])']
    MM_result3 = [By.XPATH, '(//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/gameBall"][3])']
    MM_result4 = [By.XPATH, '(//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/gameBall"][4])']
    MM_result5 = [By.XPATH, '(//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/gameBall"][5])']
    MM_result6 = [By.XPATH, '(//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/gameBall"][6])']
    MM_result7 = [By.XPATH, '(//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/gameBall"][7])']
    MM_result8 = [By.XPATH, '((//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/gameBall"][1])[2])']
    MM_result9 = [By.XPATH, '((//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/gameBall"][2])[2])']
    MM_result10 = [By.XPATH, '((//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/gameBall"][3])[2])']
    MM_result11 = [By.XPATH, '((//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/gameBall"][4])[2])']
    MM_result12 = [By.XPATH, '((//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/gameBall"][5])[2])']
    MM_result13 = [By.XPATH, '((//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/gameBall"][6])[2])']
    MM_result14 = [By.XPATH, '((//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/gameBall"][7])[2])']
    MM_result15 = [By.XPATH, '((//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/gameBall"][1])[3])']
    MM_result16 = [By.XPATH, '((//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/gameBall"][2])[3])']
    MM_result17 = [By.XPATH, '((//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/gameBall"][3])[3])']
    MM_result18 = [By.XPATH, '((//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/gameBall"][4])[3])']
    MM_result19 = [By.XPATH, '((//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/gameBall"][5])[3])']
    MM_result20 = [By.XPATH, '((//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/gameBall"][6])[3])']




    MM_Sresult1 = [By.XPATH, '((//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/gameBall"][1])[2])']
    MM_Sresult2 = [By.XPATH, '((//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/gameBall"][2])[2])']
    MM_Sresult3 = [By.XPATH, '((//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/gameBall"][3])[2])']
    MM_Sresult4 = [By.XPATH, '((//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/gameBall"][4])[2])']

class NYLlogin:
    warningList = [By.XPATH, '//*[@class="android.view.View"]']

class NYLgetNumbers:
    findGame_dropdown = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/game_type_spinner"]']
    dropdown_megamillions = [By.XPATH, '(//*[@resource-id="android:id/text1"])[2]']
    dropdown_powerball = [By.XPATH, '(//*[@resource-id="android:id/text1"])[3]']
    dropdown_lotto = [By.XPATH, '(//*[@resource-id="android:id/text1"])[4]']
    dropdown_cash4life = [By.XPATH, '(//*[@resource-id="android:id/text1"])[2]']
    niagaraGame_b = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/niagara_banner"]']
    midtownGame_b = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/midtown_banner"]']
    bullseye_b = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/state_fair_banner"]']
    niagara_submit = [By.XPATH, '(//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/save"])']
    niagara_startOver = [By.XPATH, '(//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/tryAgain"])']
    

    result_1 = [By.XPATH, '(//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/resultContainer"]//*//*)[3]']
    result_2 = [By.XPATH, '(//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/resultContainer"]//*//*)[6]']
    result_3 = [By.XPATH, '(//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/resultContainer"]//*//*)[9]']
    result_4 = [By.XPATH, '(//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/resultContainer"]//*//*)[12]']
    result_5 = [By.XPATH, '(//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/resultContainer"]//*//*)[15]']

    hamburger_home_copy = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/txt_menu_title"]']
    hamburger_home_copy = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/txt_menu_title"]']
    hamburger_home_copy = [By.XPATH, '//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/txt_menu_title"]']
    
