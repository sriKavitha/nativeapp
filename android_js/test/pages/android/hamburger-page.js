const Utils = require('../../utils/helperUtils');

class HamburgerPage {

    get hamburgerIcon()
    {
        return $('//android.widget.ImageButton[@content-desc="Open Drawer"]');
    }
    get settingsBtn()
    {
        return $('android=new UiScrollable(new UiSelector().scrollable(true)).scrollTextIntoView("SETTINGS")');
    }

    get settingsTxt()
    {
        return $('//*[@text = "SETTINGS"]');
    }

    get homeScreen()
    {
        return $('//*[@text = "GAMES"]');
    }

    get settings_Email()
    {
        return $('//*[@text="Email"]');
    }

    get settings_Password()
    {
        return $('//*[@text="Password"]');
    }

    get settings_LogInBtn()
    {
        return $('//*[@text="LOG IN"]');
    }

    get settings_Loginbtn()
    {
        return $('//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/loginButton"]');
    } 

    get promotionsBtn()
    {
        return $('//*[@text="PROMOTIONS"]');
    }

    get findRetailersBtn()
    {
        return $('//*[@text="FIND RETAILERS"]');
    }
    
    async settings_Login()
    {
        var data = await Utils.readData();
        await this.settings_Email.setValue(data.e_mail);
        await this.settings_Password.setValue(data.password);
        await this.settings_Loginbtn.click();
    }
    
   }
module.exports = new HamburgerPage();