class SettingsPage {

    get settingGeneralHeading()
    {
        return $('//*[@text="General"]')
    }
    get settingAccountHeading()
    {
        return $('//*[@text="Account"]')
    }
    get settingsAboutHeading()
    {
        return $('android=new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().textContains(\"About\"))');
    }

}
module.exports = new SettingsPage();
