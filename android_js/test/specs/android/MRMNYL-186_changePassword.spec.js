const accessEmails= require('../../utils/emailAccess')
const ResetPasswordPage = require('../../pages/android/resetPassword-page');
const allureReporter = require('@wdio/allure-reporter')
const Utils = require('../../utils/helperUtils')

describe('Android app user - Change Password in mobile browser', function() {
    // Retry 1 time if test fails
    let count = 0;
    this.retries(1);

    it('Get the latest reset password email from the eMail server and change the password', async function() 
    {
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

        // 1. Access the reset password link from eMail server 
        console.log('===============+++==============')
        var resetPwd_url = await accessEmails.retrieveEmail();
        console.log("Password URL link:\n",resetPwd_url)

        // 2. Access the reset pwd link in mobile browser
        await driver.url(resetPwd_url);

        // 3. Reset the password
        console.log('===============+++==============');
        await ResetPasswordPage.resetPwd();
        await driver.pause(3000)
        console.log('\n\n\n===============+++==============')
        
        // 4. Display console message to the user - Password is reset successfully
        await console.log("\n Password is reset successfully");
        await console.log("\n ===============+++==============\n\n");
    });
});