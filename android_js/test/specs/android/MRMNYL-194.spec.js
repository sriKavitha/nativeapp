const allureReporter = require('@wdio/allure-reporter');
const HomePage = require('../../pages/android/home-page');
const GuestPage = require('../../pages/android/guest-page');
const QuickDrawGamePage = require('../../pages/android/quickDrawGame-page');
const LoginPage = require('../../pages/android/login-page')
const HelperPage = require('../../utils/helperUtils');
const quickDrawGamePage = require('../../pages/android/quickDrawGame-page');
const Utils = require('../../utils/helperUtils')

describe('Android app user - Continue as a Guest for Quickdraw Login', function () {

     // Retry 1 time if test fails
     let count =0;
     this.retries(1);
     
    it('Verify Android app user is able to login from QUICK DRAW CUSTOM THEMES screen', async function() {

        // Read the datafile to get the environment name ex: dev/QA/stage
        data=await Utils.readData();

        // This test will retry up to 1 times, in case of failure and take a screenshot
        console.log('Retry attempt # ',count);
        count++;
        
        // Allure report configuration
        allureReporter.addFeature('Guest User');
        allureReporter.addTestId('https://rosedigital.atlassian.net/browse/MRMNYL-194');
        allureReporter.addSeverity('critical');
        allureReporter.addDescription('Description: User is able to login from QUICK DRAW CUSTOM THEMES screen');
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
 
         // 4. Wait for intro cards are displayed and swipe right  
         await (await LoginPage.loginPage_FullSectionImage).waitForDisplayed({timeout: 2000});
         await HelperPage.swipe();

         //5. Assert All Games tab
         await expect(GuestPage.allGamesTab).toExist({message: "All Games Tab is not found..."});

        //  6. Tap on ALL GAMES
        allureReporter.addStep('Tap on ALL GAMES tab');
        await GuestPage.allGamesTab.click();

        // 7. Scroll down till QUICK DRAW game and tap
        allureReporter.addStep('Scroll down till Quick Draw game and tap on Quick draw');
        await QuickDrawGamePage.QuickDrawGame.click();
        
        // 8. Assert WINNING NUMBERS, DRAW NUMBER on the screen
        allureReporter.addStep('Assert for WINNING NUMBERS, DRAW NUMBER information');
        await QuickDrawGamePage.quickDraw_WinningNumbers_DrawNumbers.waitForDisplayed();
        await expect(await QuickDrawGamePage.quickDraw_WinningNumbers_DrawNumbers).toExist();

        // 9. Scroll down till View Draws button is displayed
        allureReporter.addStep('Scroll down in the same screen to see View Draws button');
        await QuickDrawGamePage.quickDraw_GetLuckyNumbersToPlay;

        // 10. Tap on View Draws button
        allureReporter.addStep('Tap on View Draws button');
        await QuickDrawGamePage.quickDraw_viewDraws.click();

        // 11. Scroll down till Change Draw Themes to view and tap on Change Draw Themes
        allureReporter.addStep('Scroll down in the same screen to see Change Draw Themes and tap on it');
        await quickDrawGamePage.quickDraw_changeDrawThemes;
        await quickDrawGamePage.quickDraw_changeDrawThemes.click();

        // 12. Login
        allureReporter.addStep('Login using valid credentials');
        await quickDrawGamePage.quickDraw_Login();
        allureReporter.addStep('User is successfully signed in');

        // 13. Assert Live Draw screen
        await (await quickDrawGamePage.quickDraw_LiveDrawScreen).waitForExist({timeout: 60000});
        await expect(await quickDrawGamePage.quickDraw_LiveDrawScreen).toExist({message: "Live draw screen should be displayed..."});
        
        // 14. Display console message
        console.log("\nVerified successfully... Guest User is able to login from QUICK DRAW CUSTOM THEMES screen");
    }).timeout(160000);
});