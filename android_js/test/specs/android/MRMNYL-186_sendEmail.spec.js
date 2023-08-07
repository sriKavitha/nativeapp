const HomePage = require('../../pages/android/home-page');
const LoginPage = require('../../pages/android/login-page');
const allureReporter = require('@wdio/allure-reporter')
const Utils = require('../../utils/helperUtils')
const ResetPasswordPage = require('../../pages/android/resetPassword-page');

describe('Android app user - Send password recovery link', function() {
   
    // Retry 1 time if test fails
    let count = 0;
    this.retries(1);

    it.only('Send a password recovery link to QA eMail server', async function() {
  
        // Read the datafile to get the environment name ex: dev/QA/stage
        data=await Utils.readData();

        // This test will retry up to 1 times, in case of failure and take a screenshot
        console.log("Attempt # ", count+1);
        count++;

        const testID = 'https://rosedigital.atlassian.net/browse/MRMNYL-186';

        // Allure report configuration
        allureReporter.addFeature('Reset Password')
        allureReporter.addDescription(`Description: Verify that forgot password link works\n\nTest ID: ${testID}`);
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
        allureReporter.addStep('Tap on LOGIN button');
        await HomePage.loginBtnHomePage.click();

        // 4. Tap on Reset Password
        allureReporter.addStep('Click on RESET PASSWORD link');
        await LoginPage.resetPwd;
        await LoginPage.resetPwd.click();

        // 5. Keyin the email address to reset the password
        allureReporter.addStep('Keyin the email address');
        (await ResetPasswordPage.resetPasswordPage_pageTitleText).waitForDisplayed();
        (await ResetPasswordPage.resetPasswordPage_pageTitleText).isExisting();
        (await ResetPasswordPage.resetPasswordPage_Email).waitForDisplayed()
        await ResetPasswordPage.resetPasswordPage_Email.setValue('qa@rosedigital.co');

        // 6. Tap on SEND PASSWORD RESET EMAIL button
        allureReporter.addStep('Tap on SEND PASSWORD RESET EMAIL button');
        await ResetPasswordPage.resetPasswordPage_sendPasswordBtn
        await ResetPasswordPage.resetPasswordPage_sendPasswordBtn.click();

        // 7. Tap on OK button in the popup window
        allureReporter.addStep('Tap on OK button in the popup window');
        (await ResetPasswordPage.resetPasswordPage_confirmResetPwdPopUpOkBtn).waitForDisplayed();
        await ResetPasswordPage.resetPasswordPage_confirmResetPwdPopUpOkBtn.click();
        await driver.pause(3000);
        
        // 8. Display console message to the user about recovery link has been sent to the email
        await console.log("\n A password recovery link has been sent to your email.");
        await console.log("\n\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n");
    });
});