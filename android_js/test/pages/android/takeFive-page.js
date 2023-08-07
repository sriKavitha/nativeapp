class TakeFivePage {
   
    get TakeFiveGame()
    {
           return $('android=new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().textContains("EVENING"))');
    }

    get take5_evening_WinningNumbers()
    {
        return $('//*[@resource-id = "air.com.eprize.nylottery.app.NYLotteryApp:id/outerWinningNumContainer"]');       
    }

    get take5_midDay_WinningNumbers()
    {
        return $('//*[@resource-id = "air.com.eprize.nylottery.app.NYLotteryApp:id/secondWinningNumContainer"]');
    }

    get take5_Drawings()
    {
        return $('//*[@resource-id = "air.com.eprize.nylottery.app.NYLotteryApp:id/drawDetailContainer"]');
    }

}
module.exports = new TakeFivePage();
