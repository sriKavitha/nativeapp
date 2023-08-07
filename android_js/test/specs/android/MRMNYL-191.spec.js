const allureReporter = require('@wdio/allure-reporter');
const HomePage = require('../../pages/android/home-page');
const LoginPage = require('../../pages/android/login-page')
const Utils = require('../../utils/helperUtils')
describe('Android app user - Cannot login with invalid credentials', function () {
    
    // Retry 1 time if test fails
    let count =0;
    this.retries(1);
    
    it('Verify Error Icon and error message are displayed', async function() {
        
        // Read the datafile to get the environment name ex: dev/QA/stage
        data=await Utils.readData();
        
        // This test will retry up to 1 times, in case of failure and take a screenshot
        console.log('Retry attempt # ',count);
        count++;

        // allure report configuration
        allureReporter.addFeature('Login');
        allureReporter.addTestId('https://rosedigital.atlassian.net/browse/MRMNYL-191');
        allureReporter.addDescription('Description: Verify error icon and error message is displayed when invalid credentials are keyed in to login');
        allureReporter.addSeverity('normal');
        allureReporter.addEnvironment("Environment:", data.env);

         // 1. Wait for the app till it is fully launched 
        allureReporter.addStep('App is launched');
        await HomePage.threeButtons.waitForDisplayed();

        // 2. Assert for the NYL LOGO and 3 buttons on the Home screen
        // CONTINUE AS A GUEST, LOG IN, CREATE ACCOUNT 3 buttons 
        const containerBtn = await HomePage.threeButtons;
        await expect(containerBtn).toBeDisplayed({message: "Home page should have NYL Logo and all the three buttons..."});
        
        // 3. Tap on LOG IN button
        allureReporter.addStep('Tap on LOGIN button');
        await HomePage.loginBtnHomePage.click();

         // 4. Verify the title LOG IN text in Login page
         const loginTitleTxt = LoginPage.loginPage_TitleText;
         await expect(loginTitleTxt).toExist({message: "The title is missing in the Login Page "});
         allureReporter.addStep('Verified the title LOG IN in Login page');


        // 5. Login with invalid creds
        allureReporter.addStep('Key in invalid credentials for Email and Password values');
        await LoginPage.login_invalidCreds("bad_appEmail@gmail.com","badpassword");

         // 6. Assert the error message
        allureReporter.addStep('Assert error message');
        const elem = await LoginPage.invalid_eMailPasswordMessage;
        await elem.waitUntil(async function () {
            return (await elem.getText()) === 'Whoops! Incorrect email or password. Try again.'
        }, {
            timeoutMsg: `Expected: Whoops! Incorrect email or password. Try again. is displayed \nActual: ${await elem.getText()} should be displayed\n `
        });
        
        // 7. Display user can't log in with invalid creds on console
        allureReporter.addStep('User cant login with invalid credentials');
        await console.log("\n\nNYL user cannot login due to the error message..", await LoginPage.invalid_eMailPasswordMessage.getText());
    });
});