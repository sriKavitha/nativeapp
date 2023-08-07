// const RegisterAccount = require('../../pages/android/registerAccount-page');
const GamesPage = require('../../pages/android/games-page');
const HomePage = require('../../pages/android/home-page');
const HelperPage = require('../../utils/helperUtils');
const GuestPage = require('../../pages/android/guest-page');
const LoginPage = require('../../pages/android/login-page')
const ScannerPage = require('../../pages/android/scanner-page')
// const AccountDetailsPage = require('../../pages/android/accountDetails-page');
const allureReporter = require('@wdio/allure-reporter');
const Utils = require('../../utils/helperUtils');

describe('Android app user - Ticketscan Login screen opens the Camera screen', function() {

    // Retry 1 time if test fails
    let count = 0;
    this.retries(0);

    it('Verify login from Ticketscan Login screen opens the Camera screen', async function() {
        
        // Read the datafile to get the environment name ex: dev/QA/stage
        data=await Utils.readData();

        // This test will retry up to 1 times, in case of failure and take a screenshot
        console.log("Attempt # ", count);
        count++;

        // allure report configuration
        allureReporter.addFeature('Ticket Scan');
        allureReporter.addTestId('https://rosedigital.atlassian.net/browse/MRMNYL-190');
        allureReporter.addDescription('Description: User uses NYL app to open camera');
        allureReporter.addSeverity('blocker');
        allureReporter.addEnvironment("Environment:", data.env);

        // 1. wait for the app till it is fully launched 
        allureReporter.addStep('App is launched');
        await HomePage.threeButtons.waitForDisplayed();
        
        
        // 2. assert for the NYL LOGO and 3 buttons on the Home screen
        // CONTINUE AS A GUEST, LOG IN, CREATE ACCOUNT 3 buttons 
        const containerBtn = await HomePage.threeButtons;
        await expect(containerBtn).toBeDisplayed({message: "Home page should have NYL Logo and all the three buttons..."});
        
        // 3. Tap on CONTINUE AS A GUEST
        allureReporter.addStep('Tap on CONTINUE AS A GUEST button');
        await HomePage.countinueGuestBtnHomePage.click();

        // 4. wait for intro cards are displayed and swipe right 
        await (await LoginPage.loginPage_FullSectionImage).waitForDisplayed();
        await Utils.swipe();

        // 5. Assert All Games tab
        await expect(GuestPage.allGamesTab).toExist({message: "All Games Tab is not found..."});

        // 6. Tap on camera button
        allureReporter.addStep('Tap on camera button');
        await ScannerPage.scannerImage.waitForDisplayed();
        await (ScannerPage.scannerImage).click();

        // 6. Verify user is on SCAN TICKET screen
        allureReporter.addStep('Verify user is on SCAN TICKET screen');
        await (ScannerPage.scannerPageTitle).waitForDisplayed({timeout:5000});
        await expect(ScannerPage.scannerPageTitle).toHaveTextContaining("SCAN TICKET");

        // 7. User sign in Ticketscan 
        allureReporter.addStep('User sign in Ticketscan');
        await ScannerPage.scannerLogin();

        // 8. Scan message and flashlight are displayed in Scan Ticket screen
        // allureReporter.addStep('Verify Scan message');
        // await ScannerPage.scannerText.waitForDisplayed({timeout:15000});
        // await expect(ScannerPage.scannerText).toHaveTextContaining("Please visit a New York Lottery retailer");
        allureReporter.addStep('Verify Flashlight');

        // await execPath(ScannerPage.scannerText)
        await ScannerPage.scannerFlashLight.waitForExist({message:"FlashLight not exits"});
        await driver.pause(3000);

        // 9. Display a console message to the user 
        allureReporter.addStep('User signed in and landed in ticket scan screen');
        await console.log("\User signed in and landed in ticket scan screen");
    });
});