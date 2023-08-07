const path = require("path");
const fs = require("node:fs/promises");
const GuestPage = require('../pages/android/guest-page');
class Utils {

  // read jsonfile
  async readData() {
    const data = await fs.readFile("./android_js/test/data/appUserDetails.json");
    var userData = [];
    try {
       userData = JSON.parse(data);
    } catch (error) {
      console.log("File not found", error);
    }
    return userData;
  }

  // Generate current time - YYYY_HHMM
  async currentTime() {
    const yr = new Date().getFullYear();
    const min = new Date().getMinutes();
    const hr = new Date().getHours();
    const ss = new Date().getSeconds();
    const currenttime = yr + "_" + hr + min + ss;
    return currenttime; 
  }

  // swipe intro cards and tap GET STARTED button
  async swipe()
  {
      for(var i=1;i<=5;i++)
      {
         await $('android=new UiScrollable(new UiSelector().scrollable(true)).setAsHorizontalList().scrollForward()');
         await driver.pause(1000);
      }
      // await driver.pause(3000);
      await GuestPage.getStartedBtn.waitForDisplayed();
      await GuestPage.getStartedBtn.click();
  }

  // Swipe forward
  async swipeForward()
  {
      await driver.pause(2000)
      await $('android=new UiScrollable(new UiSelector().scrollable(true)).scrollForward()');
  }

  // Swipe backward
  async swipeBackward()
  {
      await driver.pause(2000)
      await $('android=new UiScrollable(new UiSelector().scrollable(true)).scrollBackward()');
  }

    // swipe till game
    async  swipeTillGame(page, thisgame_balls) {
      var balls = await page.gameNumberOfBalls.length;
      console.log("before::::",balls)
      while (true) 
      {
        balls = await page.gameNumberOfBalls.length;
        console.log("begin_1:",balls)
        
        if (balls === thisgame_balls) 
        {
            // tap on LOTTO game
            console.log("before clicking on actual game:",balls)
            await driver.pause(5000)
            await page.NumberGame.click();
            break
        } else 
        {
            balls = await page.gameNumberOfBalls.length;
            console.log("before swipe:",balls)
            await this.swipeForward();
        }
      }
    }
}
module.exports = new Utils();
