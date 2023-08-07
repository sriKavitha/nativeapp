const Utils = require('../../utils/helperUtils');
const QuickDrawGamePage = require('../../pages/android/quickDrawGame-page');

class PickTenPage {
   
    get gameNumberOfBalls() //get number of ball circles
    {
        return $$('//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/gameBall"]')
    }

    get NumberGame()
    {
        return $('android=new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().textContains("WINNING NUMBERS"))');
    }

    get gameName()
    {
           return $('//*[@resource-id = "air.com.eprize.nylottery.app.NYLotteryApp:id/gameLuckyBallText"]')
    }

    get pick10_evening_WinningNumbers()
    {
        return $('//*[@resource-id = "air.com.eprize.nylottery.app.NYLotteryApp:id/winningNumbersTitle"]');
    }

    get pick10_WinningNumbers()
    {
        return $('//*[@resource-id = "air.com.eprize.nylottery.app.NYLotteryApp:id/winningNumbersTitle"]');
    }
    
    get numbers_midDay_WinningNumbers()
    {
        return $('//*[@resource-id = "air.com.eprize.nylottery.app.NYLotteryApp:id/winningNumbersTitle2"]');
    }
    
    get pick10_Drawings()
    {
        return $('//*[@resource-id = "air.com.eprize.nylottery.app.NYLotteryApp:id/drawDetailContainer"]');
    }
    
    async swipePickTenGame()
    {
        await QuickDrawGamePage.QuickDrawGame;
        const thisgame_balls = 20
        await Utils.swipeTillGame(this,thisgame_balls);
    }
}
module.exports = new PickTenPage();
