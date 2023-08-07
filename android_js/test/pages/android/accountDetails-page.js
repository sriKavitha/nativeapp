class AccountDetailsPage {
    get accountDetails_firstName()
    {
        return $('//*[@resource-id = "air.com.eprize.nylottery.app.NYLotteryApp:id/settingsAccountDetailsName"]');
    }        
    
    get accountDetails_lastName()
    {
        return $('//*[@resource-id = "air.com.eprize.nylottery.app.NYLotteryApp:id/detailLastName"]');
    }

    get accountDetails_eMail()
    {
        return $('//*[@resource-id = "air.com.eprize.nylottery.app.NYLotteryApp:id/settingsAccountDetailsEmail"]');
    }
    
    get accountDetails_phone()
    {
        return $('//*[@resource-id = "air.com.eprize.nylottery.app.NYLotteryApp:id/settingsAccountDetailsPhone"]');
    }

    get accountDetails_zip()
    {
        return $('//*[@resource-id = "air.com.eprize.nylottery.app.NYLotteryApp:id/settingsAccountDetailsZip"]');
    }

    get accountDetails_saveButton()
    {
        return $('//*[@resource-id = "air.com.eprize.nylottery.app.NYLotteryApp:id/menuSave"]');
    }

    // capture the registered user details from SETTINGS > Account Details screen
    async getAccountDeatils()
    {
        const acctDetails = [];
        
        await acctDetails.push(await this.accountDetails_firstName.getText());
        await acctDetails.push(await this.accountDetails_lastName.getText());
        await acctDetails.push(await this.accountDetails_eMail.getText());
        await acctDetails.push(await this.accountDetails_phone.getText());
        await acctDetails.push(await this.accountDetails_zip.getText());
        
        return acctDetails;
    }

}
module.exports = new AccountDetailsPage();
