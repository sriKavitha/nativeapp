class HomePage {

    get threeButtons()
    {
        return $('//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/container"]');
    }                               

    get createAccountHome()
    {
        return $('//*[@resource-id = "air.com.eprize.nylottery.app.NYLotteryApp:id/loginRegister"]');
    }

    get loginBtnHomePage()
    {
        return $('//*[@resource-id = "air.com.eprize.nylottery.app.NYLotteryApp:id/loginButton"]');
    }

    get countinueGuestBtnHomePage()
    {
        return $('//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/guestButton"]');
    }
   }
module.exports = new HomePage();
