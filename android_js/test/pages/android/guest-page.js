class GuestPage {

    get getStartedBtn()
    {
        return $('//*[@text = "GET STARTED"]');
    }  
    
    get allGamesTab()
    {
        return $('//*[@text = "ALL GAMES"]');
    }
   }
module.exports = new GuestPage();