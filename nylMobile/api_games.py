from selenium import webdriver  #webdriver module provides all WebDriver implementations
import warnings
import unittest, time, re       #unittest is the testing framework, provides module for organizing test cases
from selenium.webdriver.common.keys import Keys     #Keys class provide keys in the keyboard like RETURN, F1, ALT, etc.
from selenium.webdriver.common.by import By         #By class provides method for finding the page elements by NAME, ID, XPATH, etc.
from selenium.webdriver.support.ui import Select    #Select class provides ability to select items in dropdown                        #Custom class for NYL
import confTest
import requests, json
import var, funct, numpy, HtmlTestRunner

# [Documentation - Summary] gathers stubs by running an API call
class NYapi(confTest.NYLmobileBASE):
#class NYapi(unittest.TestCase):
    def test_api(self):
        # [Documentation - detail] using new method to grab target and header from the credential file

        # [Documentation - detail] setting up an api call using the requests method
        # [Documentation - detail] setting headers to let api know that we have proper permissions to run api call
        head = {'x-api-key': var.CREDSmobile.xkey}
        allGames = requests.get(var.CREDSmobile.url, headers = head)
        j_allGames = json.loads(allGames.text)
        games = ["megamillions", "cash4life", "pick10", "lotto", "take5", "powerball", "numbers", "win4", "quickdraw"]
        # [Documentation - detail] lists to keep the game results in for use later
        NYapi.primaries = []
        NYapi.secondaries =[]
        # [Documentation - detail] lists to keep track of any error calls within the APIs
        passedFlags = []
        NYapi.failedFlags = []
        # [Documentation - detail] loop to see which api calls pass or fail
        NYapi.number2 = j_allGames["data"]["numbers"]["draws"][2]["results"][0]['primary']
        NYapi.win2 = j_allGames["data"]["win4"]["draws"][2]["results"][0]['primary']
        for game in games:
            apiCall = requests.get('https://api-stage.nylservices.net/games/' + game + '/draws', headers= head)
            if apiCall.text[10:2000] in allGames.text:
                passedFlags.append(game)
            else:
                passedFlags.append('xfail')
                NYapi.failedFlags.append(game)

        # [Documentation - detail] loop to populate the results of primary and secondary draws into their corresponding lists
        # blank sppots for those values that don't exist due to failed API calls or lacking secondary values
        for p, s in zip(passedFlags, passedFlags):
            if p != 'xfail':
                pstring = str(p)
                apiCall = requests.get('https://api-stage.nylservices.net/games/' + pstring + '/draws', headers= head)
                j_call = json.loads(apiCall.text)
                try:
                    p = j_call["data"]["draws"][1]["results"][0]['primary']
                except:
                    p = j_call["data"]["draws"][2]["results"][0]['primary']
                try:
                    s = j_call["data"]["draws"][1]["results"][0]['secondary']
                except:
                    try:
                        s = j_call["data"]["draws"][2]["results"][0]['secondary']
                    except:
                        s = ''
            else:
                p = ''
                s = ''
            NYapi.primaries.append(p)  
            NYapi.secondaries.append(s)     
        # print(games)
        # print(NYapi.primaries)        
        # print(NYapi.secondaries)
        # [Documentation - detail] merges the three lists into one list of tuples, in case it is needed later
        apiList = []
        for g, p, s in zip(games, NYapi.primaries, NYapi.secondaries):
            apiList.append([(g, p, s)])
        print(apiList)
        # [Documentation - detail] if any API calls failed, this will fail the test (AFTER assigning primary and secondary result values) and alert user to which calls failed
        if len(NYapi.failedFlags) > 0:
            print(NYapi.failedFlags)
            raise Exception("ERROR: above game API calls failed!")
            

#[Documentation - Summary] uses API calls from previous functions to check actual values on mobile front end 
    def test_dashboardCheckText(self):
        driver = self.driver
        funct.checkText(driver, var.NYLdashboard.guestCopy, var.NYLdashboard.guestStub)
        funct.checkText(driver, var.NYLdashboard.loginCopy, var.NYLdashboard.loginStub)
        # [Documentation - detail] starts "continue as guest" workflow
        funct.waitAndClick(driver, var.NYLdashboard.guest_b)
        # [Documentation - detail] swipes leftward until the "get started" button is found, then clicks it
        funct.swipeLeftUntil(driver, var.NYLregistration.pip6, var.NYLregistration.getStarted_b)
        funct.waitAndClick(driver, var.NYLregistration.getStarted_b)
        time.sleep(1)
        # [Documentation - detail] clicks the "all games" tab, and checks the mega million results against those garnered from the api calls
        funct.waitAndClick(driver, var.NYLgamesDB.allGames_b)
#        print(NYapi.MMprimary)
        if "megamillions" in NYapi.failedFlags:
            print('ERROR: megamillions api call failed!')
        else:
            funct.checkText(driver, var.NYLgamesDB.MM_result1, NYapi.primaries[0][0])
            funct.checkText(driver, var.NYLgamesDB.MM_result2, NYapi.primaries[0][1])
            funct.checkText(driver, var.NYLgamesDB.MM_result3, NYapi.primaries[0][2])
            funct.checkText(driver, var.NYLgamesDB.MM_result4, NYapi.primaries[0][3])
            funct.checkText(driver, var.NYLgamesDB.MM_result5, NYapi.primaries[0][4])
            funct.checkText(driver, var.NYLgamesDB.MM_result6, NYapi.secondaries[0][0])
        # [Documentation - detail] swipes upward until PowerBall is in focus, repeats
        # TODO: get unique IDs for different game result sets, this will allow us to use "swipeUpUntil" and be more precise and scalable
            funct.swipeUp(driver, var.NYLgamesDB.mainScreen)
        funct.swipeUp(driver, var.NYLgamesDB.mainScreen)
        if "powerball" in NYapi.failedFlags:
            print('ERROR: powerball api call failed!')
        else:
    #        print(NYapi.PBprimary)
            funct.checkText(driver, var.NYLgamesDB.MM_result1, NYapi.primaries[5][0])
            funct.checkText(driver, var.NYLgamesDB.MM_result2, NYapi.primaries[5][1])
            funct.checkText(driver, var.NYLgamesDB.MM_result3, NYapi.primaries[5][2])
            funct.checkText(driver, var.NYLgamesDB.MM_result4, NYapi.primaries[5][3])
            funct.checkText(driver, var.NYLgamesDB.MM_result5, NYapi.primaries[5][4])
            funct.checkText(driver, var.NYLgamesDB.MM_result6, NYapi.secondaries[5][0])
        # [Documentation - detail] swipes upward until lotto is in focus, repeats
        # TODO: get unique IDs for different game result sets, this will allow us to use "swipeUpUntil" and be more precise and scalable
            funct.swipeUp(driver, var.NYLgamesDB.mainScreen)
        funct.swipeUp(driver, var.NYLgamesDB.mainScreen)
        funct.swipeUp(driver, var.NYLgamesDB.mainScreen)
        if "lotto" in NYapi.failedFlags:
            print('ERROR: lotto api call failed!')
        else:
#        print(NYapi.NYLprimary)
            funct.checkText(driver, var.NYLgamesDB.MM_result1, NYapi.primaries[3][0])
            funct.checkText(driver, var.NYLgamesDB.MM_result2, NYapi.primaries[3][1])
            funct.checkText(driver, var.NYLgamesDB.MM_result3, NYapi.primaries[3][2])
            funct.checkText(driver, var.NYLgamesDB.MM_result4, NYapi.primaries[3][3])
            funct.checkText(driver, var.NYLgamesDB.MM_result5, NYapi.primaries[3][4])
            funct.checkText(driver, var.NYLgamesDB.MM_result6, NYapi.primaries[3][5])
            funct.checkText(driver, var.NYLgamesDB.MM_result7, NYapi.secondaries[3][0])
            funct.swipeUp(driver, var.NYLgamesDB.mainScreen)
        funct.swipeUp(driver, var.NYLgamesDB.mainScreen)
        funct.swipeUp(driver, var.NYLgamesDB.mainScreen)
        if "cash4life" in NYapi.failedFlags:
            print('ERROR: cash4life api call failed!')
        else:
    #        print(NYapi.PBprimary)
            funct.checkText(driver, var.NYLgamesDB.MM_result1, NYapi.primaries[2][0])
            funct.checkText(driver, var.NYLgamesDB.MM_result2, NYapi.primaries[2][1])
            funct.checkText(driver, var.NYLgamesDB.MM_result3, NYapi.primaries[2][2])
            funct.checkText(driver, var.NYLgamesDB.MM_result4, NYapi.primaries[2][3])
            funct.checkText(driver, var.NYLgamesDB.MM_result5, NYapi.primaries[2][4])
            funct.checkText(driver, var.NYLgamesDB.MM_result6, NYapi.secondaries[2][0])
            funct.swipeUp(driver, var.NYLgamesDB.mainScreen)
        funct.swipeUp(driver, var.NYLgamesDB.mainScreen)
        funct.swipeUp(driver, var.NYLgamesDB.mainScreen)
        if "take5" in NYapi.failedFlags:
            print('ERROR: take5 api call failed!')
        else:
#        print(NYapi.NYLprimary)
            funct.checkText(driver, var.NYLgamesDB.MM_result1, NYapi.primaries[4][0])
            funct.checkText(driver, var.NYLgamesDB.MM_result2, NYapi.primaries[4][1])
            funct.checkText(driver, var.NYLgamesDB.MM_result3, NYapi.primaries[4][2])
            funct.checkText(driver, var.NYLgamesDB.MM_result4, NYapi.primaries[4][3])
            funct.checkText(driver, var.NYLgamesDB.MM_result5, NYapi.primaries[4][4])
            funct.swipeUp(driver, var.NYLgamesDB.mainScreen)
        funct.swipeUp(driver, var.NYLgamesDB.mainScreen)
        funct.swipeUp(driver, var.NYLgamesDB.mainScreen)
        
        if "numbers" in NYapi.failedFlags:
            print('ERROR: numbers api call failed!')
        else:
#        print(NYapi.NYLprimary)
            funct.checkText(driver, var.NYLgamesDB.MM_result1, NYapi.primaries[6][0])
            funct.checkText(driver, var.NYLgamesDB.MM_result2, NYapi.primaries[6][1])
            funct.checkText(driver, var.NYLgamesDB.MM_result3, NYapi.primaries[6][2])
            funct.checkText(driver, var.NYLgamesDB.MM_Sresult1, NYapi.number2[0])
            funct.checkText(driver, var.NYLgamesDB.MM_Sresult2, NYapi.number2[1])
            funct.checkText(driver, var.NYLgamesDB.MM_Sresult3, NYapi.number2[2])
            funct.swipeUp(driver, var.NYLgamesDB.mainScreen)
            funct.swipeUp(driver, var.NYLgamesDB.mainScreen)
        funct.swipeUp(driver, var.NYLgamesDB.mainScreen)
        funct.swipeUp(driver, var.NYLgamesDB.mainScreen)
        if "win4" in NYapi.failedFlags:
            print('ERROR: win4 api call failed!')
        else:
#        print(NYapi.NYLprimary)
            funct.checkText(driver, var.NYLgamesDB.MM_result1, NYapi.primaries[7][0])
            funct.checkText(driver, var.NYLgamesDB.MM_result2, NYapi.primaries[7][1])
            funct.checkText(driver, var.NYLgamesDB.MM_result3, NYapi.primaries[7][2])
            funct.checkText(driver, var.NYLgamesDB.MM_result4, NYapi.primaries[7][3])
            funct.checkText(driver, var.NYLgamesDB.MM_Sresult1, NYapi.win2[0])
            funct.checkText(driver, var.NYLgamesDB.MM_Sresult2, NYapi.win2[1])
            funct.checkText(driver, var.NYLgamesDB.MM_Sresult3, NYapi.win2[2])
            funct.checkText(driver, var.NYLgamesDB.MM_Sresult4, NYapi.win2[3])
            funct.swipeUp(driver, var.NYLgamesDB.mainScreen)
            funct.swipeUp(driver, var.NYLgamesDB.mainScreen)
        funct.swipeUp(driver, var.NYLgamesDB.mainScreen)


        # if "quickdraw" in NYapi.failedFlags:
        #     print('ERROR: quickdraw api call failed!')
        # else:
        #     print(NYapi.primaries[8])
        #     funct.checkText(driver, var.NYLgamesDB.MM_result1, NYapi.primaries[8][0])
        #     funct.checkText(driver, var.NYLgamesDB.MM_result2, NYapi.primaries[8][1])
        #     funct.checkText(driver, var.NYLgamesDB.MM_result3, NYapi.primaries[8][2])
        #     funct.checkText(driver, var.NYLgamesDB.MM_result4, NYapi.primaries[8][3])
        #     funct.checkText(driver, var.NYLgamesDB.MM_result5, NYapi.primaries[8][4])
        #     funct.checkText(driver, var.NYLgamesDB.MM_result6, NYapi.primaries[8][5])
        #     funct.checkText(driver, var.NYLgamesDB.MM_result7, NYapi.primaries[8][6])
        #     funct.checkText(driver, var.NYLgamesDB.MM_result8, NYapi.primaries[8][7])
        #     funct.checkText(driver, var.NYLgamesDB.MM_result9, NYapi.primaries[8][8])
        #     funct.checkText(driver, var.NYLgamesDB.MM_result10, NYapi.primaries[8][9])
        #     funct.checkText(driver, var.NYLgamesDB.MM_result11, NYapi.primaries[8][10])
        #     funct.checkText(driver, var.NYLgamesDB.MM_result12, NYapi.primaries[8][11])
        #     funct.checkText(driver, var.NYLgamesDB.MM_result13, NYapi.primaries[8][12])
        #     funct.checkText(driver, var.NYLgamesDB.MM_result14, NYapi.primaries[8][13])
        #     funct.checkText(driver, var.NYLgamesDB.MM_result15, NYapi.primaries[8][14])
        #     funct.checkText(driver, var.NYLgamesDB.MM_result16, NYapi.primaries[8][15])
        #     funct.checkText(driver, var.NYLgamesDB.MM_result17, NYapi.primaries[8][16])
        #     funct.checkText(driver, var.NYLgamesDB.MM_result18, NYapi.primaries[8][17])
        #     funct.checkText(driver, var.NYLgamesDB.MM_result19, NYapi.primaries[8][18])
        #     funct.checkText(driver, var.NYLgamesDB.MM_result20, NYapi.primaries[8][19])
        funct.swipeUp(driver, var.NYLgamesDB.mainScreen)
        funct.swipeUp(driver, var.NYLgamesDB.mainScreen)
        funct.swipeUp(driver, var.NYLgamesDB.mainScreen)

        if "pick10" in NYapi.failedFlags:
            print('ERROR: pick10 api call failed!')
        else:
#        print(NYapi.NYLprimary)
            funct.checkText(driver, var.NYLgamesDB.MM_result1, NYapi.primaries[2][0])
            funct.checkText(driver, var.NYLgamesDB.MM_result2, NYapi.primaries[2][1])
            funct.checkText(driver, var.NYLgamesDB.MM_result3, NYapi.primaries[2][2])
            funct.checkText(driver, var.NYLgamesDB.MM_result4, NYapi.primaries[2][3])
            funct.checkText(driver, var.NYLgamesDB.MM_result5, NYapi.primaries[2][4])
            funct.checkText(driver, var.NYLgamesDB.MM_result6, NYapi.primaries[2][5])
            funct.checkText(driver, var.NYLgamesDB.MM_result7, NYapi.primaries[2][6])
            funct.checkText(driver, var.NYLgamesDB.MM_result8, NYapi.primaries[2][7])
            funct.checkText(driver, var.NYLgamesDB.MM_result9, NYapi.primaries[2][8])
            funct.checkText(driver, var.NYLgamesDB.MM_result10, NYapi.primaries[2][9])
            funct.checkText(driver, var.NYLgamesDB.MM_result11, NYapi.primaries[2][10])
            funct.checkText(driver, var.NYLgamesDB.MM_result12, NYapi.primaries[2][11])
            funct.checkText(driver, var.NYLgamesDB.MM_result13, NYapi.primaries[2][12])
            funct.checkText(driver, var.NYLgamesDB.MM_result14, NYapi.primaries[2][13])
            funct.checkText(driver, var.NYLgamesDB.MM_result15, NYapi.primaries[2][14])
            funct.checkText(driver, var.NYLgamesDB.MM_result16, NYapi.primaries[2][15])
            funct.checkText(driver, var.NYLgamesDB.MM_result17, NYapi.primaries[2][16])
            funct.checkText(driver, var.NYLgamesDB.MM_result18, NYapi.primaries[2][17])
            funct.checkText(driver, var.NYLgamesDB.MM_result19, NYapi.primaries[2][18])
            funct.checkText(driver, var.NYLgamesDB.MM_result20, NYapi.primaries[2][19])
            funct.swipeUp(driver, var.NYLgamesDB.mainScreen)


# Boiler plate code to run the test suite
if __name__ == "__main__":
    # First runner will enable html logs on your current directory, second runner will keep local console logs
    unittest.main(warnings='ignore', testRunner=HtmlTestRunner.HTMLTestRunner(output='html_report_dir'))
    # unittest.main(warnings='ignore')