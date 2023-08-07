const HomePage = require('../../pages/android/home-page');
const GuestPage = require('../../pages/android/guest-page');
const LoginPage = require('../../pages/android/login-page');
const HelperPage = require('../../utils/helperUtils');
const HamburgerPage = require('../../pages/android/hamburger-page');
const MegaMillionsPage = require('../../pages/android/megaMillionsGame-page');
const allureReporter = require('@wdio/allure-reporter');
const Utils = require('../../utils/helperUtils')

describe('Android app user - Continue as a Guest to login from Mega Millions Notifications', function () {

    // Retry 1 time if test fails
    let count =0;
    this.retries(1);
    
    it('Verify android user is able to log in from Mega Millions NOTIFICATION SETTINGS screen', async function() {

        // Read the datafile to get the environment name ex: dev/QA/stage
        data=await Utils.readData();

         // This test will retry up to 1 times, in case of failure and take a screenshot
         console.log('Retry attempt # ',count);
         count++;

         // allure report configuration
        allureReporter.addFeature('Guest User');
        allureReporter.addTestId('https://rosedigital.atlassian.net/browse/MRMNYL-195');
        allureReporter.addDescription('Description: User is able to login from Mega Millions NOTIFICATION SETTINGS screen');
        allureReporter.addSeverity('normal');
        allureReporter.addEnvironment("Environment:", data.env);
        
         // 1. wait for the app till it is fully launched 
         allureReporter.addStep('App is launched');
         await (await HomePage.threeButtons).waitForDisplayed();
        
         // 2. assert for the NYL LOGO and 3 buttons on the Home screen
         // CONTINUE AS A GUEST, LOG IN, CREATE ACCOUNT 3 buttons 
         const containerBtn = await HomePage.threeButtons;
         await expect(containerBtn).toBeDisplayed({message: "Home page should have NYL Logo and all the three buttons..."});
 
         // 3. tap on CONTINUE AS A GUEST
         allureReporter.addStep('Tap on CONTINUE AS A GUEST button');
         await HomePage.countinueGuestBtnHomePage.click();
 
         // 4. wait for intro cards are displayed and swipe right 
         await (await LoginPage.loginPage_FullSectionImage).waitForDisplayed({timeout: 2000});
         await HelperPage.swipe();

        //5. assert All Games tab
        await expect(GuestPage.allGamesTab).toExist({message: "All Games Tab is not found..."});

        //  6. tap on ALL GAMES
        allureReporter.addStep('Tap on ALL GAMES tab');
        await GuestPage.allGamesTab.click();

        // 7. Swipe until Mega Millions game appears and tap
        allureReporter.addStep('Swipe until Mega Millions game appears and tap');
        await MegaMillionsPage.megaMillionsGame;

        // 8. Assert the Learn More and Winning numbers text
        await expect(await MegaMillionsPage.mega_learnMore).toExist({message: 'Learn More text is unavailable on the Mega Millions game..'});
        await expect(await MegaMillionsPage.mega_winningNumbersTxt).toExist({message: 'WInning numbers text is unavailable on the Mega Millions game..'});

        // 9. Tap on Mega Millions game
        allureReporter.addStep('Tap on Mega Millions game');
        await (await MegaMillionsPage.megaMillionsGame).click();

        // 10. Assert winning numbers, next drawing & current jackpot info
        allureReporter.addStep('Assert winning numbers, next drawing & current jackpot info');
        await expect(await MegaMillionsPage.mega_winningNumbersInfo).toExist();
        await expect(await MegaMillionsPage.mega_nextDrawCurrentJackpotInfo).toExist();

        // 11. Swipe until SET NOTIFICATIONS FOR THIS GAME button and tap on it
        allureReporter.addStep('Swipe down to see SET NOTIFICATIONS FOR THIS GAME button and tap on it');
        await MegaMillionsPage.mega_setNotifySwipe;
        await (await MegaMillionsPage.mega_setNotificationBtn).click();

        // 12. Login using valid credentials
        allureReporter.addStep('Login using valid credentials');
        await MegaMillionsPage.megaMillions_Login();
        allureReporter.addStep('User is successfully signed in from Mega Millions NOTIFICATION SETTINGS screen');

        // 13. Assert home page is displayed
        await expect(HamburgerPage.homeScreen).toExist({message: 'Should display the Home screen...'});
        
        // 14. Display console message
        console.log("\nVerified successfully... Guest User is able to signin from Mega Millions NOTIFICATION SETTINGS screen...");
    });
});