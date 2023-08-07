###NYL README

1. What this project does
2. How to install it and setup the dev environment
3. Test execution notes & Example usage
4. How to make changes
5. Change log

## What this project does
Automated testing of the NYL project. Currently tests consists of UI tests of the SSO, Admin Dashboard web
applications and API tests of Nylservices backend.

## How to install it
1. Download Pycharm from https://www.jetbrains.com/pycharm/download
2. Download and install Python 3.8 from https://www.python.org/downloads/
3. Connect your github account to Pycharm via SSH https://docs.github.com/en/authentication/connecting-to-github-with-ssh
4. Download Chromedriver for your version of Chrome from here https://sites.google.com/chromium.org/driver/
and add Chromedriver to /usr/local/bin. Open the Chromedriver executable to trigger the warning on Mac. Navigate to
System Preferences > Security and Privacy and allow the executable to run.
   
#####Required Modules
Certain python modules are required to run the automation, install steps are detailed in the following Confluence Docs
https://rosedigital.atlassian.net/wiki/spaces/RDKB/pages/1031700488/Setting+up+Selenium+Webdriver+Python
https://rosedigital.atlassian.net/wiki/spaces/RDKB/pages/697958453/Reporting+via+HtmlTestRunner
https://rosedigital.atlassian.net/wiki/spaces/RDKB/pages/782630975/NYL+-+Purge+Tool+-+Readme
https://rosedigital.atlassian.net/wiki/spaces/RDKB/pages/697892910/HAR+file+generation+with+BrowserMobProxy
https://rosedigital.atlassian.net/wiki/spaces/RDKB/pages/698351640/Image+manipulation+with+Pillow+PIL

The below modules can be added simply through Pycharm > Preferences > Project > Python Interpreter > +
- PyJWT
- json

## Test execution notes & example usage
You will need to create the following directories on your host machine.
~/Users/Shared/testing

Place up to date credentials file in the ~/Users/Shared/testing folder. Contact NYL QA lead to receive this file.
- Test Data Version: andrewpii1212022.txt
- Real Data Version: nyl1212022.txt

###Test execution notes:
- Suites of tests for various systems have been collected in runner.py and can be executed as a whole.
- Open the runner.py file and comment / comment out the suite that you wish to execute and click Run from Pycharm dropdown menu.
- For the SSO tests, registration flows that involve government ID verification start with "MANUAL" in the file name.
These "MANUAL" tests will fail without a testers input at the correct step.
An Alert will pop up on the first capture screen with instructions.
- Tests can also be executed on the individual file level through the IDE by simply selecting the file and
right click to open contextual menu and hitting RUN or through Pycharm UI.

###Terminal commands to run tests

Tests can be executed on the individual file level via terminal with the following steps. 

1. CD into the QA folder 
2. Execute command to run test suite or individual tests using patterns below.

In python3 you can run discover mode from the terminal without any code changes and can run a suite of tests.
The command to run test cases with a pattern is as follows:

$python3 -m unittest discover -s <project_directory> -p "<starting_syntax>*.py"

EG:
$ python3 -m unittest discover -s nyl/ -p "SSO*.py" 

would, assuming you were in the QA/ directory, run all test-cases on all files that began with "SSO" in the nyl/ folder

You can also pass in individual test files to test with the following command:

$ python3 -m unittest project_directory/test_file.py

EG:
$python3 -m unittest nyl/API_services_status.py

would run the single test file "API_services_status"

## How to make changes
- Create branch off of main
- Make additions/changes
- Submit PR for review
- Merge upon approval

More detailed steps are in the following confluence doc
https://rosedigital.atlassian.net/wiki/spaces/RDKB/pages/539885675/Repo+The+Aesthetic+Operatives

When making changes follow the below naming convention for the python files.

HELPER - denotes helper files that are not tests but are used during manual testing process

MANUAL - denotes tests that require tester interaction to complete

AD - denotes Admin Dashboard tests

API - denotes NYL Services API tests

SSO - denotes NYL Single Sign On tests

## Change log
08/26/2022: V1.0 - Created Readme, updated documentation, fixed user deletion