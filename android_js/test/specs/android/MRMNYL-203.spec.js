const HomePage = require('../../pages/android/home-page');
const allureReporter = require('@wdio/allure-reporter');
const Utils = require('../../utils/helperUtils');
const LoginPage = require('../../pages/android/login-page');
const GuestPage = require('../../pages/android/guest-page');
const MegaMillionsPage = require('../../pages/android/megaMillionsGame-page');
describe('Android app user - Continue as a Guest to verify that a user can access the draw data from Mega Millions screen', function () {
    
    // Retry 1 time if test fails
    let count = 0;
    this.retries(1);

    const testID = 'https://rosedigital.atlassian.net/browse/MRMNYL-203';

    it('Verify that draw data is displayed for Mega Millions game on My Games', async function() {
    
        // Read the datafile to get the environment name ex: dev/QA/stage
        data=await Utils.readData();

        // This test will retry up to 1 times, in case of failure and take a screenshot
        console.log("Retry attempt # ", count);
        count++;

        // Allure report configuration
        allureReporter.addFeature('Guest User');
        allureReporter.addDescription(`Description: User is able to access the draw data from Mega Millions screen \n\n TestID: ${testID} `);
        allureReporter.addSeverity('Normal');
        allureReporter.addEnvironment("Environment:", data.env);
        
        // 1. Wait for the app till it is fully launched 
        allureReporter.addStep('App is launched');
        await (await HomePage.threeButtons).waitForDisplayed();
        
        // 2. Assert for the NYL LOGO and 3 buttons on the Home screen
        // CONTINUE AS A GUEST, LOG IN, CREATE ACCOUNT 3 buttons 
        const containerBtn = await HomePage.threeButtons;
        await expect(containerBtn).toBeDisplayed({message: "Home page should have NYL Logo and all the three buttons..."});
        
        // 3. tap on CONTINUE AS A GUEST
        allureReporter.addStep('Tap on CONTINUE AS A GUEST button');
        await HomePage.countinueGuestBtnHomePage.click();

        // 4. wait for intro cards are displayed and swipe right 
        await (await LoginPage.loginPage_FullSectionImage).waitForDisplayed({timeout: 2000});
        await Utils.swipe();

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

        // 11. Display console message
        allureReporter.addStep('Verified successfully... Guest User is able to view draw data info for Mega Millions game...');
        console.log("\nVerified successfully... Guest User is able to view draw data for Mega Millions game...");        
    });
});