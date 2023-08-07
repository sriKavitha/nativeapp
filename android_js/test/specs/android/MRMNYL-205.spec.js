const HomePage = require('../../pages/android/home-page');
const allureReporter = require('@wdio/allure-reporter');
const Utils = require('../../utils/helperUtils');
const LoginPage = require('../../pages/android/login-page');
const GuestPage = require('../../pages/android/guest-page');
const PowerBallPage = require('../../pages/android/powerball-page');
describe('Android app user - Continue as a Guest to verify that a user can access the draw data from Powerball screen', function () {
    
    // Retry 1 time if test fails
    let count = 0;
    this.retries(1);

    const testID = 'https://rosedigital.atlassian.net/browse/MRMNYL-205';
    
    it('Verify that draw data is displayed for Powerball game on My Games', async function() {
    
        // Read the datafile to get the environment name ex: dev/QA/stage
        data=await Utils.readData();

        // This test will retry up to 1 times, in case of failure and take a screenshot
        console.log("Retry attempt # ", count);
        count++;

        // Allure report configuration
        allureReporter.addFeature('Guest User');
        allureReporter.addDescription(`Description: User is able to access the draw data from PowerBall screen \n\n TestID: ${testID} `);
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

        // 7. Swipe until PowerBall game appears and tap
        allureReporter.addStep('Swipe until PowerBall game appears and tap');
        await PowerBallPage.powerBallGame;

        // 8. Tap on PowerBall game
        allureReporter.addStep('Tap on PowerBall game');
        await (await PowerBallPage.powerBallGame).click();

        // 9. Assert the Learn More and Winning numbers text
        await expect(await PowerBallPage.powerball_drawFreq).toExist();
        await expect(await PowerBallPage.powerball_winningNumbersTxt).toExist({message: 'Winning numbers text is unavailable on the PowerBall game..'});

        // 10. Display console message
        allureReporter.addStep('Verified successfully... Guest User is able to view draw data info for PowerBall game...');
        console.log("\nVerified successfully... Guest User is able to view draw data for PowerBall game...");        
    });
});