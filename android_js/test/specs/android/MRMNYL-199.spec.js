const allureReporter = require('@wdio/allure-reporter');
const HomePage = require('../../pages/android/home-page');
const LoginPage = require('../../pages/android/login-page')
const NumbersPage = require('../../pages/android/numbers-page');
const GuestPage = require('../../pages/android/guest-page');
const Utils = require('../../utils/helperUtils')

describe('Android app user - Continue as a Guest user to view All Games draw data for NUMBERS Game', function () {
    
     // Retry 1 time if test fails
     let count =0;
     this.retries(1);
     
     const testID = 'https://rosedigital.atlassian.net/browse/MRMNYL-199';

     it('Verify Android app user is able to view All games draw data in NUMBERS screen', async function () {  

        // Read the datafile to get the environment name ex: dev/QA/stage
        var data=await Utils.readData();

        // This test will retry up to 1 times, in case of failure and take a screenshot
        console.log('Retry attempt # ',count);
        count++;
        
        // allure report configuration
        allureReporter.addFeature('Guest User');
        allureReporter.addDescription(`Description: Guest user can view All games draw data in NUMBERS game Screen\n\n TestID: ${testID}`);
        allureReporter.addSeverity('normal');
        allureReporter.addEnvironment("Environment:", data.env);
        
         // 1. Wait for the app till it is fully launched 
         allureReporter.addStep('App is launched');
         await HomePage.threeButtons.waitForDisplayed();
        
         // 2. Assert for the NYL LOGO and 3 buttons on the Home screen
         // CONTINUE AS A GUEST, LOG IN, CREATE ACCOUNT 3 buttons 
         const containerBtn = await HomePage.threeButtons;
         await expect(containerBtn).toBeDisplayed({message: "Home page should have NYL Logo and all the three buttons..."});
 
         // 3. Tap on CONTINUE AS A GUEST
         allureReporter.addStep('Tap on CONTINUE AS A GUEST button');
         await HomePage.countinueGuestBtnHomePage.click();

         // 4. wait for intro cards are displayed and swipe right 
         await (await LoginPage.loginPage_FullSectionImage).waitForDisplayed({timeout: 2000});
         await Utils.swipe();

         //5. Assert All Games tab
         await expect(GuestPage.allGamesTab).toExist({message: "All Games Tab is not found..."});

        //  6. Tap on ALL GAMES
        allureReporter.addStep('Tap on ALL GAMES tab');
        await GuestPage.allGamesTab.click();

        // 7. swipe until Numbers game and tap
        allureReporter.addStep('Swipe till NUMBERS game and tap on NUMBERS');
        await NumbersPage.swipeNumberGame();
        
        // 8. assert for Evening Winning numbers, Midday winning numbers
        await expect(await NumbersPage.numbers_evening_WinningNumbers).toExist({message: "Evening winning numbers should be available"});
        await expect(await NumbersPage.numbers_midDay_WinningNumbers).toExist({message: "Mid day winning numbers should be available"});
        allureReporter.addStep('Verified successfully... Guest user can view All games draw data in NUMBERS game Screen...');

        // 9. Display console message
        console.log('NYL Android user as a Guest user can view All games draw data in NUMBERS game Screen');
    });
});
