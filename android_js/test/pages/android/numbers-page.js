const Utils = require('../../utils/helperUtils');
const QuickDrawGamePage = require('../../pages/android/quickDrawGame-page');
class NumbersPage {
   
    get gameNumberOfBalls() 
    {
        return $$('//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/gameBall"]')
    }

    get NumberGame()
    {
        return $('android=new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().textContains("EVENING"))');
    }

    get gameName()
    {
           return $('//*[@resource-id = "air.com.eprize.nylottery.app.NYLotteryApp:id/gameLuckyBallText"]')
    }

    get numbers_evening_WinningNumbers()
    {
        return $('//*[@resource-id = "air.com.eprize.nylottery.app.NYLotteryApp:id/winningNumbersTitle"]');
    }

    get numbers_midDay_WinningNumbers()
    {
        return $('//*[@resource-id = "air.com.eprize.nylottery.app.NYLotteryApp:id/winningNumbersTitle2"]');
    }

    async swipeNumberGame()
    {
        await QuickDrawGamePage.QuickDrawGame;
        await Utils.swipeBackward()
        await this.NumberGame.click();
    }
}
module.exports = new NumbersPage();
