const Utils = require('../../utils/helperUtils');
const QuickDrawGamePage = require('../../pages/android/quickDrawGame-page');
class WinFourPage {
   
    get gameNumberOfBalls() 
    {
        return $$('//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/gameBall"]')
    }

    get NumberGame()
    {
        return $('android=new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().textContains("EVENING"))');
    }

    get win4_evening_WinningNumbers()
    {
        return $('//*[@resource-id = "air.com.eprize.nylottery.app.NYLotteryApp:id/winningNumbersTitle"]');
    }

    get win4_midDay_WinningNumbers()
    {
        return $('//*[@resource-id = "air.com.eprize.nylottery.app.NYLotteryApp:id/winningNumbersTitle2"]');
    }
    
    async swipeWinFourGame()
    {
        await QuickDrawGamePage.QuickDrawGame;
        await Utils.swipeBackward()
        await Utils.swipeForward()
        await this.NumberGame.click();
    }
}
module.exports = new WinFourPage();
