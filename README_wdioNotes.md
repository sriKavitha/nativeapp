
5. Project setup:
JavaScript and WDIO installation instructions:

https://knapsackpro.com/testing_frameworks/difference_between/webdriver-io/vs/mochajs

1. Install Node. When Node is installed NPM is also installed
2. For WDIO, node 14 and above is good
3. npm -v    && node -v  => find version on your machine
4. Install VS Code. Click on extension when you open editor.
5. Add extensions like theme (One Dark Pro), material icon theme(for colorful folder structure), ES6 Mocha Snippets(it will generate the it/desc blocks for you), ESLint (for code lint), Colonize(to add ; after the statement
For Mac, hold cmd,shipt,P and search for theme

6. After node is installed, create a folder for testing and cd to that folder
    a. npm init -y     => To initiliaze the project, which means package.json file is created
    b. Package.json file will contain all the packages needed for this project
    c. Now, install WebdriverIO CLI:  
        i. npm install @wdio/cli   to setup webdriverIO in the project
        ii. Now, set up configuration for wdio : npx wdio config (just follow the instructions and keeping pressing ENTER key)
        iii. Now, a file wdio.conf.js is generated at project root level and it has all the configuration
        iv. Testcases should be in this structure. So, create a “test” folder and in “test folder”, create a “specs” folder and in “specs” folder, create “.js” files
        v. test/specs/**/*.js  =>as per wdio.conf.js file
        vi. To run the test case, npx wdio


? Where should your tests be launched? local - for e2e testing of web and mobile applications
? Where is your automation backend located? On my local machine
? Which framework do you want to use? Mocha (https://mochajs.org/)
? Do you want to use a compiler? No!
? Do you want WebdriverIO to autogenerate some test files? No
? Which reporter do you want to use? spec
? Do you want to add a plugin to your test setup? 
? Do you want to add a service to your test setup? chromedriver, appium
? What is the base url? http://localhost
? Do you want me to run `npm install` Yes


7. Framework setup:
    a. Create jsconfig.json in root directory: (autocompletion)
    {
    "compilerOptions": {
        "types": [
            "node",
            "@wdio/globals/types",
            "@wdio/mocha-framework"
        ]
    },”exclude”:”node_modules”
    }

    b. Babel: In order to setup Babel, you have to do 2 steps. Babel is a JS compiler
    c. Step1: npm install eslint --save-dev this will install @babel/core @babel/cli @babel/preset-env @babel/register
       Step2: Create a file babel.config.js in root directory
        module.exports = {
        presets: [
        ['@babel/preset-env', {
            targets: {
                node: '14'
            }
        }]
        ]
        }

    d. Install ESLint: Helps discover the problems in the code before it’s executed or without executing the code. Checks syntax.
        a. npm install eslint --save-dev
        b. Npm install eslint-plugin-wdio --save-dev
  
            .eslintrc to be created in root directory
            {
            "plugins": [
                "wdio"
            ],
                "extends": "plugin:wdio/recommended",
                "parserOptions": {
                    "ecmaVersion": 2020,
                    "sourceType": "module"
                }
            }


9.Cross broswser testing, use selenium standalone service, which you need to install:
    a. npm install @wdio/selenium-standalone-service --save-dev

Make changes in wdio.config.js
1.services: ['selenium-standalone’],  (replace with chromedriver). In logs, we see selenium-standalone, but not chrome browser(when npc wdio is given).
2.to run on Firefox, safari,IE: in capabilities - add the below code:
{
       maxInstances: 5,
         browserName: 'safari'
     },
     {
       maxInstances: 5,
       browserName: ‘firefox'
     },
     {
       maxInstances: 5,
       browserName: ‘internetExplorer'
     },



10. .Reporter:
Default reporter is spec reporter is a terminal report.
HTML report is Allure reporter
Installation steps:
npm install @wdio/allure-reporter --save-dev
1. const allure = require('allure-commandline')
2.in reporters:you will have [’spec’], delete and replace with: which means the wdio will generate spec and allure reports for us when a TC is executed:
reporters: ['spec',['allure', {
        outputDir: 'allure-results',
        disableWebdriverStepsReporting: false,
        disableWebdriverScreenshotsReporting: false,
    }]],

It will create a `allure-results` folder in the project path. This folder has a bunch of Jason files.
To generate a html report using the json files, follow these steps:
npm i allure-commandline
Run this command: npx allure generate allure-results && npx  allure open
If the allure report does open, use this:     npx allure serve -h localhost or npx allure open -h localhost

Browserstack integration: install: npm install @wdio/browserstack-service --save-dev
   npm install @wdio/browserstack-service --save-dev 

VS COde extensions:
1.colonize to add semicolons at the end of line
2.Mocha snippets (to generate describe and it blocks) to autogenerate the code
3.ES6 Lint - check JS code
4.Prettier (cmd, shift P) to format the code (shift opt F) to format the code
5.Bracket pair colonizer ( for colorful brackets
6.One dark pro (theme) for code in different colors
7.Material icon theme (for folders, files in different color)



To run tests:
npx wdio (it will execute the file specified in specs section)
In order to execute a specific file from command line: 'npx wdio --spec test/specs/android/MRMNYL-191.spec.js'

To save the output of spec report into text file `npx wdio | tee test-report.txt` will save the output of spec report into test-report.txt file
a. npx wdio --spec test/specs/abc.spec.js | tee test-report.txt
b. npx wdio | tee test-report.txt

Await $(‘#get-started’).click(); // find element by id

Assertions:
await expect(browser).toHaveTitle(‘actual Page title')
await expect(browser).toHaveUrl(‘actualurl’)
await expect(browser).toHaveUrlContaining(‘actualurl')

await expect(browser).not.toHaveUrlContaining(‘actualurl’)

Two ways to do:
1.await expect(await element.getText()).toEqual(“Think before you act and Make different”)
2.await expect(element).toHaveText("Think before you act and Make different”)


getUrl()
getTitle()
getText()
getElementText()
toEqual()
toHaveText()
toHaveTextContaining()
toHaveLength(4)
toBeGreaterThan(10)



For (const item of items)
{
const text = await item.getText()
await expect(text.length).toBeGreaterThan(10);
}
Await expect(elements).toHaveLength(4)




Webdriverio: has builtin assertions and also has wait and retry capability. Chai does have retry capability.
Webdriverio expect assertion ex: toHaveText()—> retries 10 times
Jest assertion: toEqual() —>deep equal and tried only one time. Coming from Jest library and no retry capability and is part of webdriverio and no need to install.

Jest/Jasmine assertions work well with -> non element assertions like array or a string. Then go for Jest/Jasmine assertions.
Wdio -> for element specific assertions
 

Wait commands:::
1.browser.pause(2000); //pause 2 secs
2.waitForDisplayed() - element is displayed on the screen
3.waitForClickable() - element is cliackable
4.waitForEnabled() - input field is enabled
5.waitForExist() - to check if element exists in DOM
6.waitUntil()  - to check for a particular condition

Ex:
1.await $(‘#primary-menu’).waitForDisplayed(); //default global wait is 10secs
2.await $(‘#primary-menu’).waitForDisplayed({timeout:1000}); // only this test case
3.If you change in wdio.conf.js file, it is changed for all the test cases and is globally. The parameter in wdio.conf.js file:  waitforTimeout: 10000,
4.waitUntil() ex:

// waitUntil() without custom error message
Await browser.waitUntil(async function(){
 Const text =  await $(‘#primary menu li’);  // will return Home
 Return text.getText() === ‘HOME'
})

// waitUntil() with custom error message
Await browser.waitUntil(async function(){
 Const text =  await $(‘#primary menu li’);  // will return Home
 Return text.getText() === ‘HOME'
}
{
timeout :5000,
timeoutMsg: ‘Could not verify the HOME text from #primary-menu li’}
);


// iFrame commands
await browser.switchToFrame(iFrameName)
Await browser.switchToParentFrame()

// debugging:
1.browser.pause(2000) //adding a pause
2.await console.log(“asasa”)
    You can print the element: console.log(await $(‘#button[type=submit]’)
3.await browser.debug(); we need to increate mocha timeout in wdio.conf.js file
Currently we have 1 min timeout, we can increase this to 600000
Execute `npx wdio` the execution will be stopped at the place where you have given await browser.debug();
Now you can type the element which we have an error on the console
When browser.debug() is used on the console, you can give all the commands on the console that are in your js file
mochaOpts: {
        ui: 'bdd',
        timeout: 60000  (1 min timeout)



Take screenshot: with date and time:
// var name = 'ERROR-chrome-' + Date.now()
            // browser.saveScreenshot('./errorShots/' + name + '.png')
            // https://github.com/webdriverio-boneyard/wdio-allure-reporter/blob/master/README.md



https://webdriver.io/docs/selectors/


npm show webdriverio version => will show the latest wdio version available in the market
npx wdio —version
List wdio versions from 8.2 to 8.10:
npm view webdriverio versions --json | grep -E '8\.[2-9]\.[0-9]+|8\.10\.[0-9]+'

Install specific @wdio/cli version:
npm install @wdio/cli@8.2
