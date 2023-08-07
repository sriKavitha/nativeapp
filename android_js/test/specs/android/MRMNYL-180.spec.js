const allureReporter = require('@wdio/allure-reporter');
const HomePage = require('../../pages/android/home-page');
const LoginPage = require('../../pages/android/login-page')
const HelperPage = require('../../utils/helperUtils');
const HamburgerPage = require('../../pages/android/hamburger-page')
const SettingsPage = require('../../pages/android/settings-page')
const Utils = require('../../utils/helperUtils')

describe('Android app user - Guest user can access Settings screen through navigation menu', function () {

     // Retry 1 time if test fails
     let count =0;
     this.retries(1);
     
     it('Verify NYL Android app user can access Settings screen through the nav menu', async function () {  

        // Read the datafile to get the environment name ex: dev/QA/stage
        data=await Utils.readData();

        // This test will retry up to 1 times, in case of failure and take a screenshot
        console.log('Retry attempt # ',count);
        count++;
        
        // allure report configuration
        allureReporter.addFeature('Guest User');
        allureReporter.addTestId('https://rosedigital.atlassian.net/browse/MRMNYL-180');
        allureReporter.addDescription('Description: Guest user can access Settings screen through navigation menu');
        allureReporter.addSeverity('normal');
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

         // 4. wait for intro cards are displayed and swipe right 
         await (await LoginPage.loginPage_FullSectionImage).waitForDisplayed({timeout: 2000});
         await HelperPage.swipe();

         // 5. click on Hamburger Icon
        allureReporter.addStep('click on Hamburger Icon');
        await HamburgerPage.hamburgerIcon.waitForDisplayed();
        await HamburgerPage.hamburgerIcon.click();

        // 6. swipe down till SETTINGS and click
        allureReporter.addStep('swipe down till SETTINGS and click');
        await HamburgerPage.settingsBtn;
        await HamburgerPage.settingsBtn.click();

        // 7. assert the sections: General, Account, About on the screen
        await expect(await SettingsPage.settingGeneralHeading).toHaveTextContaining('General');
        await expect(await SettingsPage.settingAccountHeading).toHaveTextContaining('Account');
        await expect(await SettingsPage.settingsAboutHeading).toHaveTextContaining('About');

    });
});
