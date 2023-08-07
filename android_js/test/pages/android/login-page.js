const Utils = require('../../utils/helperUtils');
class LoginPage {

    get loginPage_TitleText()
    {
        return $('//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/tittle"]');
    }

    get loginPage_Email()
    {
        return $('//*[@resource-id = "air.com.eprize.nylottery.app.NYLotteryApp:id/loginEmail"]');
    }

    get loginPage_Password()
    {
        return $('//*[@resource-id = "air.com.eprize.nylottery.app.NYLotteryApp:id/loginPassword"]');
    }

    get loginPage_LoginBtn()
    {
        return $('//*[@resource-id = "air.com.eprize.nylottery.app.NYLotteryApp:id/loginButton"]');
    }

    get loginPage_FullSectionImage()
    {
        return $('//*[@resource-id = "air.com.eprize.nylottery.app.NYLotteryApp:id/fullPage"]');
    }

    get invalid_eMailPasswordMessage()
    {
        return $('//*[@text = "Whoops! Incorrect email or password. Try again."]');
    }

    get errorIcon_eMail()
    {
        return $('//android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.view.View');
    }

    get errorIcon_password()
    {
        return $('//android.widget.RelativeLayout[2]/android.view.View');
    }

    get resetPwd()
    {
        return $('//*[contains(@text,"FORGOT PASSWORD?")]')
    }
    
    // Login with valid creds - User data is from file
    async login()
    {
        var data = await Utils.readData();
        await this.loginPage_Email.setValue(data.e_mail);
        await this.loginPage_Password.setValue(data.password);
        await this.loginPage_LoginBtn.click();
    }


    // Login with invalid creds
    async login_invalidCreds(email,password)
    {
        await this.loginPage_Email.setValue(email);
        await this.loginPage_Password.setValue(password);
        await this.loginPage_LoginBtn.click();
        await this.invalid_eMailPasswordMessage.waitForDisplayed({timeout: 15000});
        await this.errorIcon_eMail.waitForDisplayed({timeout: 15000});
        await this.errorIcon_password.waitForDisplayed({timeout: 15000});
    }
   }
module.exports = new LoginPage();
