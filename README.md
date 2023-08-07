# QA
Test case execution
WDIO testcase execution:
A. cd QA
B. npm install => to install node modules

1. To execute or run the testcase with “config folder” config file: 
a. navegate to QA folder
b. npx wdio ./android_js/config/wdio.android.conf.js --spec android_js/test/specs/android/MRMNYL-201.spec.js 

2. Run the testcase with “root folder” config file: 
a. navegate to QA folder
b. npx wdio wdio.android.conf.js --spec android_js/test/specs/android/MRMNYL-203.spec.js 

3. To execute pwd change testcase all the three at a time:
npx wdio android_js/test/specs/android/runPWDChange.spec.js

4. Three parts can be executed individually:
    a. npx wdio wdio.android.conf.js --spec android_js/test/specs/android/MRMNYL-186_sendEmail.spec.js
    b. npx wdio wdio.changepwd.conf.js --spec android_js/test/specs/android/MRMNYL-186_changePassword.spec.js
    c. npx wdio wdio.android.conf.js --spec android_js/test/specs/android/MRMNYL-193.spec.js


