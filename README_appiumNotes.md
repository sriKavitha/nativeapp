Appium
1. To find driver list:
“npx appium driver list” or “appium driver list”
2. to install drivers:
npx appium driver install uiautomator2 (OR try: npm i appium-uiautomator2-driver)
npx appium driver install xcuitest (OR try npm i appium-xcuitest-driver)
If it is already installed, it will give error saying its already installed
Try this “appium driver install uiautomator2”

3. To verify the drivers are installed: “npx appium driver list - -installed”
4. “appium-doctor --version”  
5. “appium --version” 
6. “adb devices” ( to see the list of devices that are currently spinning)
7. adb -s emulator-5554 emu kill (will kill the emulator)
8. adb kill-server 
9. To Kill the emulator:
    1. Find the PID and kill the PID:
        1. ps -ax | grep emulator 
        2. Kill PID
10. 
appWaitForLaunch=false


Web driver API doc:
https://webdriver.io/docs/api/browser/keys/

http://www.temblast.com/ref/akeyscode.htm pressKeyCode 66 for Enter Key and 61 for Tab key
        await driver.pressKeyCode(153) // numeric 9


======
1. Npm init wdio foldername
2. 
3. https://github.com/appium/appium/issues/14144


======
iOS setup:
1. Install Xcode (development env for iOS to spin the simulators)
2. Xcode command line tools => “xcode-select - -install” => to install command line tools
3. Carthage is dependency manager for macOS and iOS and to install Carthage, (brew should be installed) Carthage is dependency manager for Mac OS and iOS
    1. “brew install carthage” 
4. Run Appium-doctor
    1. “appium-doctor --ios”
5. XCUITest is a driver for iOS needs to be installed => “npx appium driver install xcuitest”  or “appium driver install xcuitest”
    1. To check if it is installed, “appium driver list” or “appium driver list --installed”
6. Setup capabilities for iOS in wdio.conf.js file and appium inspector as well
7. Appium inspector capabilities:
iOS:
{
  "platformName": "iOS",
  "appium:platformVersion": "16.2",
  "appium:deviceName": "iPhone 14 Pro",
  "appium:app": "/private/var/kavitha/Documents/ks/app/ios/UIKitCatalog.app",
  "appium:automationName": "XCUITest"
}

Android:
{
  "platformName": "Android",
  "appium:platformVersion": "10",
  "appium:deviceName": "Nexus S",
  "appium:app": "/private/var/kavitha/Documents/webdriverio-appium/app/Android/app-staging.apk",
  "appium:automationName": "UIAutomator2"
}

=====
import { Key } from 'webdriverio'
await driver.keys([Key.Ctrl, 'a', 'c'])
=====
Here is a solution that can help you dump all the logs onto a text file
adb logcat -d > logs.txt
=====

Using real device:
======
Using a real Android device isn't much different than using an emulator. You just need to set up a few more things like the device name and UDID in your capabilities.
========




Appium allure report: unknown status-> https://github.com/webdriverio/webdriverio/issues/4856