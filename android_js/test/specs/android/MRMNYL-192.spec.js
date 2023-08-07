const HomePage = require('../../pages/android/home-page');
const GuestPage = require('../../pages/android/guest-page');
const LoginPage = require('../../pages/android/login-page')
const HelperPage = require('../../utils/helperUtils');
const HamburgerPage = require('../../pages/android/hamburger-page');
const RegisterAccount = require('../../pages/android/registerAccount-page')
const allureReporter = require('@wdio/allure-reporter');
const Utils = require('../../utils/helperUtils')

describe('Android app user - Continue as a Guest to login from Settings', function () {

    // Retry 1 time if test fails
    let count =0;
    this.retries(0);

    it('Verify Android app user is able to login from SETTINGS screen', async function() {
        
        // Read the datafile to get the environment name ex: dev/QA/stage
        data=await Utils.readData();

        // This test will retry up to 1 times, in case of failure and take a screenshot
        console.log('Retry attempt # ',count);
        count++;

        // Allure report configuration
        allureReporter.addFeature('Guest User');
        allureReporter.addTestId('https://rosedigital.atlassian.net/browse/MRMNYL-192');
        allureReporter.addSeverity('critical');
        allureReporter.addDescription('Description: User is able to login from SETTINGS screen');
        allureReporter.addEnvironment("Environment:", data.env);
        
         // 1. Wait for the app till it is fully launched
         allureReporter.addStep('App is launched');
         await (await HomePage.threeButtons).waitForDisplayed();
        
         // 2. Assert for the NYL LOGO and 3 buttons on the Home screen
         // CONTINUE AS A GUEST, LOG IN, CREATE ACCOUNT 3 buttons 
         const containerBtn = await HomePage.threeButtons;
         await expect(containerBtn).toBeDisplayed({message: "Home page should have NYL Logo and all the three buttons..."});
        
         // 3. Tap on CONTINUE AS A GUEST
         allureReporter.addStep('Tap on CONTINUE AS A GUEST button');
         await HomePage.countinueGuestBtnHomePage.click();
 
         // 4. Wait for full section image is displayed and swipe right 
         await (await LoginPage.loginPage_FullSectionImage).waitForDisplayed({timeout: 2000});
         await HelperPage.swipe();

         // 5. Assert All Games tab
         await expect(GuestPage.allGamesTab).toExist({message: "All Games Tab is not found..."});

         // 6. Tap on Hamburger Icon
         allureReporter.addStep('Tap on Hamburger');
         await HamburgerPage.hamburgerIcon.waitForDisplayed();
         await HamburgerPage.hamburgerIcon.click();

        // 7. Scroll down till SETTINGS and tap
        allureReporter.addStep('Swipe down till you see SETTINGS button and tap on it');
        (await HamburgerPage.settingsBtn).waitForDisplayed({timeouut:10000});
        await HamburgerPage.settingsBtn.click();

        // 8. Assert for SETTINGS text
        await HamburgerPage.settingsTxt.waitForDisplayed({timeout:15000});
        await expect(HamburgerPage.settingsTxt).toHaveText('SETTINGS',{message:'User should be in SETTINGS page.'});

        allureReporter.addStep('Tap on Log In button');
        await HamburgerPage.settings_LogInBtn.click();

        allureReporter.addStep('Signin using valid credentials');
        await HamburgerPage.settings_Login();
        await (RegisterAccount.hourSymbol).waitForExist({reverse:true})
        allureReporter.addStep('User successfully signed in using valid credentials');

        // 9. Assert for home screen
        await expect(await HamburgerPage.homeScreen).toBeDisplayed({message:'User should be in Home screen with MYGAMES and ALLGAMES buttons displayed'});

        // 10. Display console message
        console.log('NYL Android user continued as a Guest and is able to login from SETTINGS screen');

    });
});