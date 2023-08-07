const Utils = require('../../utils/helperUtils');
class QuickDrawGamePage {

    get QuickDrawGame()
    {
        return $('android=new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().textContains(\"QUICK DRAW\"))');
    }

    get quickDraw_WinningNumbers_DrawNumbers()
    {
        return $('//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/winningNumbersContainer"]');       
    }

    get quickDraw_GetLuckyNumbersToPlay()
    {
        return $('android=new UiScrollable(new UiSelector().scrollable(true)).scrollTextIntoView("GET LUCKY NUMBERS TO PLAY")');
    }

    get quickDraw_viewDraws()
    {
        return $('//*[@text= "VIEW DRAWS"]');
    }

    get quickDraw_liveDrawTxt()
    {
        return $('//*[@text= "DRAW # "]');
    }

    get quickDraw_changeDrawThemes()
    {
        return $('android=new UiScrollable(new UiSelector().scrollable(true)).scrollTextIntoView("Change Draw Themes")');
    }

    get quickDraw_quickDrawCustomThemes()
    {
        return $('//*[@text = "QUICK DRAW CUSTOM THEMES"]');
    }

    get quickDraw_Email()
    {
        return $('//*[@text="Email"]');
    }

    get quickDraw_Password()
    {
        return $('//*[@text="Password"]');
    }

    get quickDraw_LogInBtn()
    {
        return $('//*[@text="LOG IN"]');
    }

    get quickDraw_Loginbtn()
    {
        return $('//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/loginButton"]');
    }

    get quickDraw_LiveDrawScreen()
    {
        return $('//*[@resource-id = "air.com.eprize.nylottery.app.NYLotteryApp:id/gridview"]');
    }
    
    get hamburgerIcon()
    {
        return $('//android.widget.ImageButton[@content-desc="Open Drawer"]');
    }


    async quickDraw_Login()
    {
        var data = await Utils.readData();
        await this.quickDraw_Email.setValue(data.e_mail);
        await this.quickDraw_Password.setValue(data.password);
        await this.quickDraw_LogInBtn.click();
    }
   }
module.exports = new QuickDrawGamePage();