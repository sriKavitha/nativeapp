const Utils = require('../../utils/helperUtils');

class LottoPage {
   
    get gameNumberOfBalls()
    {
        return $$('//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/gameBall"]')
    }

    get lotto_WinningNumbers()
    {
        return $('//*[@resource-id = "air.com.eprize.nylottery.app.NYLotteryApp:id/winningNumbersTitle"]');
    }

    get lotto_Drawings()
    {
        return $('//*[@resource-id = "air.com.eprize.nylottery.app.NYLotteryApp:id/drawDetailContainer"]');
    }

    get NumberGame()
    {
        return $('android=new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().textContains("WINNING"))');
    }

    async swipeLottoGame()
    {
        const thisgame_balls = 7
        await Utils.swipeTillGame(this,thisgame_balls);
    }

}
module.exports = new LottoPage();
