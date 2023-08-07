const Utils = require('../../utils/helperUtils');
class ScannerPage {

    get scannerImage()
    {
        return $('//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/scanner_button"]')
    }

    get scannerPageTitle()
    {
        return $('//*[@text="SCAN TICKET"]');
    }

    get scannerLogInBtn()
    {
        return $('//*[@text="LOG IN"]');   
    }

    get scannerEmailTxtBox()
    {
        return $('//*[@text="Email"]');
    }
    get scannerPasswordTxtBox()
    {
        return $('//*[@text="Password"]');   
    }
    
    get scannerCameraImage()
    {
        return $('//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/camera_icon"]');
    }

    get scannerEnableCameraBtn()
    {
        return $('//*[@text="ENABLE YOUR CAMERA"]');
    }

    get scannerText()
    {
        return    $('//*[contains(@text,"Please visit a New York Lottery retailer")]')
    }

    get scannerFlashLight()
    {
        return $('//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/flashlight_button"]')
    }

    async scannerLogin()
    {
        var data = await Utils.readData();
    
        await this.scannerEmailTxtBox.setValue(data.e_mail);
        await this.scannerPasswordTxtBox.setValue(data.password);
        await this.scannerLogInBtn.click();
        await driver.pause(3000)
    }
}
module.exports = new ScannerPage();
