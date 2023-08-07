const path = require('path')
const { config } = require('../QA/wdio.shared.conf');

// ====================
// Runner Configuration
// ====================
config.port= 4723;

// ====================
// Specs
// ====================
config.specs= [
    // ToDo: define location for spec files here
    './android_js/test/specs/android/MRMNYL-186.spec.js'
];

// ====================================
// Capabilities for all Android scripts
// ====================================
config.capabilities = [{
        'appium:platformName': 'Android',
        'appium:platformVersion': '11.0',
        'appium:deviceName': 'Pixel 3',
        'appium:automationName': 'UIAutomator2',
        'appium:app': path.join(process.cwd(),'./android_js/app/android/app-staging.apk'),
        'appium:autoGrantPermissions':true
}];

exports.config = config;