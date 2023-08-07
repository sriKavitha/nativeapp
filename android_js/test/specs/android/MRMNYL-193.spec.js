const HomePage = require('../../pages/android/home-page');
const LoginPage = require('../../pages/android/login-page');
const allureReporter = require('@wdio/allure-reporter')
const Utils = require('../../utils/helperUtils')

describe('Android app user - Login from NYL Home screen with valid credentials', function() {
    
    // Retry 1 time if test fails
    let count = 0;
    this.retries(1);

    it('Verify NYL Android app user can login into the account successfully', async function() {
    
        // Read the datafile to get the environment name ex: dev/QA/stage
        data=await Utils.readData();

        // This test will retry up to 1 times, in case of failure and take a screenshot
        console.log("Retry attempt # ", count);
        count++;

        // Allure report configuration
        allureReporter.addFeature('Login')
        allureReporter.addTestId('https://rosedigital.atlassian.net/browse/MRMNYL-193')
        allureReporter.addDescription('Description: Verify NYL user can login with valid credentials from NYL app')
        allureReporter.addSeverity('critical')
        allureReporter.addEnvironment("Environment:", data.env);
        
        // 1. Wait for the app till it is fully launched 
        allureReporter.addStep('App is launched')
        await (await HomePage.threeButtons).waitForDisplayed();
        
        // 2. Assert for the NYL LOGO and 3 buttons on the Home screen
        // CONTINUE AS A GUEST, LOG IN, CREATE ACCOUNT 3 buttons 
        const containerBtn = await HomePage.threeButtons;
        await expect(containerBtn).toBeDisplayed({message: "Home page should have NYL Logo and all the three buttons..."});
        
        // 3. Tap on LOG IN button
        allureReporter.addStep('Click on LOGIN button');
        await HomePage.loginBtnHomePage.click()
        
        // 4. Verify the title LOG IN text in Login page
        const loginTitleTxt = LoginPage.loginPage_TitleText;
        await expect(loginTitleTxt).toExist({message: "The title is missing in the Login Page "});
        await driver.pause(1000);
        allureReporter.addStep('Verified the title LOG IN in Login page');
        
        // 5. Login with valid email, password
        allureReporter.addStep('Key in valid credentials')
        await LoginPage.login();

        // 6. Assert banner image is dispalyed after NYL user sign in
        const flag = await (LoginPage.loginPage_FullSectionImage).waitForDisplayed({timeout: 20000});
        await expect(flag).toEqual(true, {message: "Banner image is not displayed after NYL user signed in...\n"});
        allureReporter.addStep('NYL user is successfully signed into NYL app using valid credentials');

        // 7. Display user is successfully signed in message on the console
        await console.log("\nNYL user is successfully signed in...\n\n");
    });
});