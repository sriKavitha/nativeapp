class FindRetailersPage {

    get findRetailersHeading()
    {
        return $('//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/tittle"]')
    }

    get findRetailersFilter()
    {
        return $('//*[@resource-id="air.com.eprize.nylottery.app.NYLotteryApp:id/filtersButton"]');
    }
    
    get findRetailersMap()
    {
        return $('//*[@content-desc="Google Map"]');
    }

}
module.exports = new FindRetailersPage();
