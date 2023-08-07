class PromotionsPage {

    get promotionsHeading()
    {
        return $('//*[@text="PROMOTIONS"]')
    }

    get promotionsTitle()
    {
        return $('//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/txt_promotion_title"]');
    }
    
    get promotionsIcon()
    {
        return $('//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/img_promtion"]');
    }

}
module.exports = new PromotionsPage();
