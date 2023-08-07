class PowerBallPage {

    get powerball_drawFreq()
    {
        return $('//*[@text="Draws Mondays, Wednesdays and Saturdays"]');
    }

    get powerball_winningNumbersTxt()
    {
        return $('//*[@text="WINNING NUMBERS"]');
    }                            

    get powerBallGame()
    {
        return $('android=new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().textContains(\"POWERBALL\"))');
    }
    get results()
    {
        return $$('//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/rowOfBalls"]');
    }
   }
module.exports = new PowerBallPage();