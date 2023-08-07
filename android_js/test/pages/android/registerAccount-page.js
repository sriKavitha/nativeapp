const Utils = require('../../utils/helperUtils');
class RegisterAccount {

    get eMail()
    {
        return $('//*[@text="Email"]');
    }

    get passWord()
    {
        return $('//*[@text="Password"]');
    }

    get confirmPassWord()
    {
        return $('//*[@text="Password (again)"]');
    }

    get firstName()
    {
        return $('//*[@text="First name"]');
    }

    get lastName()
    {
        return $('//*[@text="Last name"]');
    }

    get phoneType()
    {
        return $('//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/registerPhoneType"]');
    }

    get phNumber()
    {
        return $('//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/registerPhone"]');
    }
    get major()
    {
        return $('//*[@text="Sure am!"]');
    }

    get zip()
    {
        return $('//*[@text="Zip"]');
    }

    get createAccountBtn()
    {
        return $('//*[@text="CREATE ACCOUNT"]');
    }

    get hourSymbol()
    {
        return $('//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/container"]');
    }
    

    // keyin values for the mandatory fields - email, pwd1, pwd2, last and first names, phone, zip
    async submitRegistrationForm()
    {
        var registrationDetails = [];

        var data = await Utils.readData();
        var dateTime = await Utils.currentTime();
       
        // generate the email in the format --> appEmailYYYY_HHMM@gmail.com
        var email = await "appEmail" + dateTime + "@gmail.com";
        await this.eMail.setValue(email);
        await this.passWord.setValue(data.password);
        await this.confirmPassWord.setValue(data.password);
        await this.firstName.setValue(data.firstName);
        await this.lastName.setValue(data.lastName);

        // tap on phone number to keyin the phone number
        await this.phNumber.click();
        // (await this.phNumber).waitForExist
        await this.phNumber.waitForExist();
        await driver.pause(1000);

        var phoneNumber =[];
        var phoneNumber = await data.phone;
        
        for (var i = 0; i < phoneNumber.length; i++) {  
            await driver.pressKeyCode(phoneNumber[i]); 
        }

        // press tab key
        await driver.pressKeyCode(61);

        // tap 18 years or older radio button
        await this.major.click();
        
        // Keyin zipcode
        await this.zip.setValue(data.zipcode);

        // hide the keyboard and press tab
        await driver.hideKeyboard();
        await driver.pressKeyCode(61);
        
        await this.createAccountBtn.click();
        
        // save the registration details
        await registrationDetails.push(data.firstName);
        await registrationDetails.push(data.lastName);
        await registrationDetails.push(email.toLowerCase());
        await registrationDetails.push("(248) 777 - 9999");
        await registrationDetails.push(data.zipcode);
        return registrationDetails;
    }
}
module.exports = new RegisterAccount();