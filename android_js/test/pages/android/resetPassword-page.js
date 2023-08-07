const Utils = require('../../utils/helperUtils');
class ResetPasswordPage 
{

    get resetPasswordPage_pageTitleText()
    {
        return $('//*[@text="RESET YOUR PASSWORD"]');
    }

    get resetPasswordPage_Email()
    {
        return $('//*[@text="Email"]');
    }

    get resetPasswordPage_sendPasswordBtn()
    {
        return $('//*[@text="SEND PASSWORD RESET EMAIL"]');
    }

    get resetPasswordPage_resetTxt()
    {
        return $('//*[@text="Enter your email and we’ll send you a password reset email."]');
    }
    
    get resetPasswordPage_confirmResetPwdPopUpTitle()
    {
        return $('//*[@text="Your request was sent!"]');
    }
    
    get resetPasswordPage_confirmResetPwdPopUpTitle()
    {
        return $('//*[@text="Your request was sent!"]');
    }

    get resetPasswordPage_confirmResetPwdPopUpText()
    {
        return $('//*[@text="Please check your email to recover your password."]');
    }
    
    get resetPasswordPage_confirmResetPwdPopUpOkBtn()
    {
        return $('//*[@text="OK"]');
    }

    get resetPasswordPage_confirmResetPwdPopUpCancelBtn()
    {
        return $('//*[@text="CANCEL"]');
    }

    get newPassword()
    {
        return $('//input[@name="password"]');
    }

    get ConfirmNewPassword()
    {
        return $('//input[@name="confirmPassword"]');
    }

    get resetPasswordBtn()
    {
        return $('//span[text()="Reset Password"]//ancestor::button');
    }

    async resetPwd()
    {
        // Read the datafile to get the password
        var data = await Utils.readData();

        await this.newPassword.setValue(data.password);
        await this.ConfirmNewPassword.setValue(data.password);
        await this.resetPasswordBtn.waitForDisplayed();
        await this.resetPasswordBtn.click();
    }

}
module.exports = new ResetPasswordPage();
