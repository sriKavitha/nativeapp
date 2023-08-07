const RegisterAccount = require('../../pages/android/registerAccount-page');
const GamesPage = require('../../pages/android/games-page');
const HomePage = require('../../pages/android/home-page');
const HelperPage = require('../../utils/helperUtils');
const AccountDetailsPage = require('../../pages/android/accountDetails-page');
const allureReporter = require('@wdio/allure-reporter');
const Utils = require('../../utils/helperUtils');

describe('Android app user - Register an user from NYL Home screen successfully', function() {

    // Retry 1 time if test fails
    let count = 0;
    this.retries(1);

    it('Verify NYL Android app user can register an account', async function() {
        
        // Read the datafile to get the environment name ex: dev/QA/stage
        data=await Utils.readData();

        // This test will retry up to 1 times, in case of failure and take a screenshot
        console.log("Retry attempt # ", count);
        count++;

        // allure report configuration
        allureReporter.addFeature('Register User');
        allureReporter.addTestId('https://rosedigital.atlassian.net/browse/MRMNYL-204');
        allureReporter.addDescription('Description: User uses NYL app to register');
        allureReporter.addSeverity('blocker');
        allureReporter.addEnvironment("Environment:", data.env);

        // 1. wait for the app till it is fully launched 
        allureReporter.addStep('App is launched');
        await HomePage.threeButtons.waitForDisplayed();
        
        
        // 2. assert for the NYL LOGO and 3 buttons on the Home screen
        // CONTINUE AS A GUEST, LOG IN, CREATE ACCOUNT 3 buttons 
        const containerBtn = await HomePage.threeButtons;
        await expect(containerBtn).toBeDisplayed({message: "Home page should have NYL Logo and all the three buttons..."});
        
        // 3. click on CREATE ACCOUNT button
        allureReporter.addStep('Click on CREATE ACCOUNT button');
        await HomePage.createAccountHome.click();
        
        // 4. keyin the values for all required fields
        allureReporter.addStep('Key in values for required fields');
        const registrationDetails = await RegisterAccount.submitRegistrationForm();
        
        // 5. assert the registration is successful
        allureReporter.addStep('Assert the Hour glass symbol appears upon tapping the CREATE ACCOUNT button ');
        await expect(RegisterAccount.hourSymbol).toExist({message: "Registration is not successfull..."});
        await HelperPage.swipe();

        // 6. assert user landed into Games Page
        await expect(GamesPage.gamesTxt).toHaveTextContaining("GAMES");

        // 7. goTo Settings page
        await GamesPage.settings_Page();

        // 8. get Account Details
        const acctDetails = await AccountDetailsPage.getAccountDeatils();
        
        // 9. assert registration details matches with account deatils from app
        allureReporter.addStep('Assert registrated details matches with SETTINGS > ACCOUNT > ACCOUNT DETAILS section');
        await expect(registrationDetails).toEqual(acctDetails);

        // 10. display user is successfully registered message on the console
        allureReporter.addStep('Account is successfuly created and Verified');
        await console.log("\nYour registration is successfully completed... Please check your email. ", registrationDetails[2]);
        await console.log("\nregistration user",registrationDetails);
        await console.log("\naccount details",acctDetails);
        
    });
});