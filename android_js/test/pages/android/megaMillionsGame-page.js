const Utils = require('../../utils/helperUtils');
class MegaMillionsGamePage {

    get megaMillionsGame()
    {
        return $('android=new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().textContains(\"mega\"))');
    }

    get mega_learnMore()
    {
        return $('//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/learnMoreTxt"]');
    }

    get mega_winningNumbersTxt()
    {
        return $('//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/winningNumbersTitle"]');
    }

    get mega_nextDrawCurrentJackpotInfo()
    {
        return $('//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/drawDetailContainer"]');
    }
    
    get mega_winningNumbersInfo()
    {
        return $('//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/outerWinningNumContainer"]');
    }

    get mega_setNotifySwipe()
    {
        return $('android=new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().textContains(\"SET NOTIFICATIONS FOR THIS GAME\"))');
    }

    get mega_setNotificationBtn()
    {
        return $('//*[@text="SET NOTIFICATIONS FOR THIS GAME"]');
    }

    get mega_setNotificationTitle()
    {
        return $('//*[@text="NOTIFICATIONS SETTINGS"]');
    }

    get mega_email()
    {
        return $('//*[@resource-id = "air.com.eprize.nylottery.app.NYLotteryApp:id/loginEmail"]')
    }

    get mega_password()
    {
        return $('//*[@resource-id = "air.com.eprize.nylottery.app.NYLotteryApp:id/loginPassword"]')
    }

    get mega_loginBtn()
    {
        return $('//*[@resource-id = "air.com.eprize.nylottery.app.NYLotteryApp:id/loginButtonYellow"]')

    }

    async megaMillions_Login()
    {
        var data = await Utils.readData();
        await this.mega_email.setValue(data.e_mail);
        await this.mega_password.setValue(data.password);
        await (await this.mega_loginBtn).waitForDisplayed();
        await this.mega_loginBtn.click();
    }
   }
module.exports = new MegaMillionsGamePage();