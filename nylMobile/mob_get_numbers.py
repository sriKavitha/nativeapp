import unittest, time  #unittest is the testing framework, provides module for organizing test cases
import confTest
import var, funct, numpy, PIL, cv2, HtmlTestRunner
from PIL import Image

# [Documentation - Summary] uses image detection to click on objects based on the file they look like
class NYapi(confTest.NYLmobileBASE):
    def test_01niagaraFalls(self):
        driver = self.driver
        funct.waitAndClick(driver, var.NYLdashboard.guest_b)
        # [Documentation - detail] swipes leftward until the "get started" button is found, then clicks it
        funct.swipeLeftUntil(driver, var.NYLregistration.pip6, var.NYLregistration.getStarted_b)
        funct.waitAndClick(driver, var.NYLregistration.getStarted_b)
        time.sleep(1)
        # [Documentation - detail] Navigated to the chosen game
        funct.waitAndClick(driver, var.NYLgamesDB.hamburger_b)
        funct.waitAndClick(driver, var.NYLgamesDB.menu_GetNumbers)
        funct.waitAndClick(driver, var.NYLgetNumbers.findGame_dropdown)
        funct.waitAndClick(driver, var.NYLgetNumbers.dropdown_megamillions)
        funct.waitAndClick(driver, var.NYLgetNumbers.niagaraGame_b)
        # [Documentation - detail] setup prior to image detection
        numpy.set_printoptions(threshold=numpy.inf)
        list1 = []
        list2 = []
        counter = 0
        while True:
            # [Documentation - detail] Saves a screenshot every second, and then uses the "template" to find that image in the screenshot
            counter += 1
            ## [Documentation - detail] if enabled, this will make a new screenshot for every second, instead of reusing the same name every second (enable for debugging)
            #print(counter)
            # driver.save_screenshot('frame' + str(counter) + '.png')
            # img_rgb = cv2.imread('frame' + str(counter) + '.png')
            driver.save_screenshot('frame.png')
            img_rgb = cv2.imread('frame.png')
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
            # [Documentation - detail] This is the template image that will be searched for and clicked on
            img = Image.open('barrel3.png')
            size= driver.get_window_size()
            width = int(size['width'])
            height = int(size['height'])
            tw = int(width*0.100925)
            wpercent = (tw / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((tw, hsize), PIL.Image.ANTIALIAS)
            img.save('resized_image.png')  
            


            template = cv2.imread('resized_image.png',0)
            w, h = template.shape[::-1]
            res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
            # [Documentation - detail] Set how much of a match something must be before it counts as a match
            threshold = 0.65
            loc = numpy.where( res >= threshold)
            # [Documentation - detail] As soon as more than one match is found, find their coordinates, and click the spot (plus extra pixels for the tiem delay between taking the screenshot, and finding the image)
            if len(str(loc)) > 0:
               for pt in zip(*loc[::-1]):
                    x = pt[0]
                    y = pt[1]
                    size= driver.get_window_size()
                    width = int(size['width'])
                    height = int(size['height'])
                    xw = width*0.042
                    yw = height*0.138
                    funct.coordinateClick(driver, x + xw, y + yw)
                    # print('-----truck found!')
                    # print(counter)
                    # print(pt)
                    # driver.save_screenshot('foleyres' + str(counter) + '.png')
                    break
            pip5 = driver.find_element_by_xpath(var.NYLgetNumbers.result_5[1]).text        
            pip4 = driver.find_element_by_xpath(var.NYLgetNumbers.result_4[1]).text        
            pip3 = driver.find_element_by_xpath(var.NYLgetNumbers.result_3[1]).text        
            pip2 = driver.find_element_by_xpath(var.NYLgetNumbers.result_2[1]).text        
            pip1 = driver.find_element_by_xpath(var.NYLgetNumbers.result_1[1]).text        
          
            if pip5 != '':
                pips = [pip1, pip2, pip3, pip4, pip5]
                for pip in pips:
                    list1.append(pip)
                break
            else:
                pass
        funct.waitAndClick(driver, var.NYLgetNumbers.niagara_startOver)
        while True:
            counter += 1
            #print(counter)
            driver.save_screenshot('frame.png')
            img_rgb = cv2.imread('frame.png')
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
            img = Image.open('barrel3.png')
            size= driver.get_window_size()
            width = int(size['width'])
            height = int(size['height'])
            tw = int(width*0.100925)
            wpercent = (tw / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((tw, hsize), PIL.Image.ANTIALIAS)
            img.save('resized_image.png')  
            template = cv2.imread('resized_image.png',0)
            w, h = template.shape[::-1]
            res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
            threshold = 0.65
            loc = numpy.where( res >= threshold)
            if len(str(loc)) > 0:
                for pt in zip(*loc[::-1]):
                    x = pt[0]
                    y = pt[1]
                    size= driver.get_window_size()
                    width = int(size['width'])
                    height = int(size['height'])
                    xw = width*0.042
                    yw = height*0.138
                    funct.coordinateClick(driver, x + xw, y + yw)
            pip5 = driver.find_element_by_xpath(var.NYLgetNumbers.result_5[1]).text        
            pip4 = driver.find_element_by_xpath(var.NYLgetNumbers.result_4[1]).text        
            pip3 = driver.find_element_by_xpath(var.NYLgetNumbers.result_3[1]).text        
            pip2 = driver.find_element_by_xpath(var.NYLgetNumbers.result_2[1]).text        
            pip1 = driver.find_element_by_xpath(var.NYLgetNumbers.result_1[1]).text        
            
            if pip5 != '':
                pips = [pip1, pip2, pip3, pip4, pip5]
                for pip in pips:
                    list2.append(pip)
                break
            else:
                pass
        if list1 == list2:
            print(list1)
            print(list2)
            raise Exception("Numbers not random!")
        else:
            print(list1)
            print(list2)

    def test_02midtownMadness(self):
        driver = self.driver
        funct.waitAndClick(driver, var.NYLdashboard.guest_b)
        # [Documentation - detail] swipes leftward until the "get started" button is found, then clicks it
        funct.swipeLeftUntil(driver, var.NYLregistration.pip6, var.NYLregistration.getStarted_b)
        funct.waitAndClick(driver, var.NYLregistration.getStarted_b)
        time.sleep(1)
        # [Documentation - detail] Navigated to the chosen game
        funct.waitAndClick(driver, var.NYLgamesDB.hamburger_b)
        funct.waitAndClick(driver, var.NYLgamesDB.menu_GetNumbers)
        funct.waitAndClick(driver, var.NYLgetNumbers.findGame_dropdown)
        funct.waitAndClick(driver, var.NYLgetNumbers.dropdown_megamillions)
        funct.waitAndClick(driver, var.NYLgetNumbers.midtownGame_b)
        numpy.set_printoptions(threshold=numpy.inf)
        list1 = []
        list2 = []
        counter = 0
        while True:
            # [Documentation - detail] Saves a screenshot every second, and then uses the "template" to find that image in the screenshot
            counter += 1
            # driver.save_screenshot('frame' + str(counter) + '.png')
            # img_rgb = cv2.imread('frame' + str(counter) + '.png')
            driver.save_screenshot('frame.png')
            img_rgb = cv2.imread('frame.png')
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
            img = Image.open('truck.png')
            size= driver.get_window_size()
            width = int(size['width'])
            height = int(size['height'])
            tw = int(width*0.31944444)
            wpercent = (tw / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((tw, hsize), PIL.Image.ANTIALIAS)
            img.save('resized_image.png')  
            


            template = cv2.imread('resized_image.png',0)
            w, h = template.shape[::-1]
            res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
            threshold = 0.6
            loc = numpy.where( res >= threshold)
            # [Documentation - detail] As soon as more than one match is found, find their coordinates, and click the spot (plus extra pixels for the tiem delay between taking the screenshot, and finding the image)
            if len(str(loc)) > 0:
                for pt in zip(*loc[::-1]):
                    x = pt[0]
                    y = pt[1]
                    size= driver.get_window_size()
                    width = int(size['width'])
                    height = int(size['height'])
                    xw = width*0.208
                    yw = height*0.038
                    funct.coordinateClick(driver, x + xw, y + yw)
                    print('-----truck found!')
                    #print(counter)
                    #print(pt)
                    #driver.save_screenshot('foleyres' + str(counter) + '.png')
                    break
            pip5 = driver.find_element_by_xpath(var.NYLgetNumbers.result_5[1]).text        
            pip4 = driver.find_element_by_xpath(var.NYLgetNumbers.result_4[1]).text        
            pip3 = driver.find_element_by_xpath(var.NYLgetNumbers.result_3[1]).text        
            pip2 = driver.find_element_by_xpath(var.NYLgetNumbers.result_2[1]).text        
            pip1 = driver.find_element_by_xpath(var.NYLgetNumbers.result_1[1]).text        
          
            if pip5 != '':
                pips = [pip1, pip2, pip3, pip4, pip5]
                for pip in pips:
                    list1.append(pip)
                break
            else:
                pass
        funct.waitAndClick(driver, var.NYLgetNumbers.niagara_startOver)
        while True:
            counter += 1
            #print(counter)
            driver.save_screenshot('frame.png')
            img_rgb = cv2.imread('frame.png')
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
            template = cv2.imread('resized_image.png',0)
            w, h = template.shape[::-1]
            res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
            threshold = 0.5
            loc = numpy.where( res >= threshold)
            if len(str(loc)) > 0:
                #print("found Fire Truck(s)")
                for pt in zip(*loc[::-1]):
                    #print(pt)
                    x = pt[0]
                    y = pt[1]
                    size= driver.get_window_size()
                    width = int(size['width'])
                    height = int(size['height'])
                    xw = width*0.208
                    yw = height*0.038
                    funct.coordinateClick(driver, x + xw, y + yw)
                    break
            pip5 = driver.find_element_by_xpath(var.NYLgetNumbers.result_5[1]).text        
            pip4 = driver.find_element_by_xpath(var.NYLgetNumbers.result_4[1]).text        
            pip3 = driver.find_element_by_xpath(var.NYLgetNumbers.result_3[1]).text        
            pip2 = driver.find_element_by_xpath(var.NYLgetNumbers.result_2[1]).text        
            pip1 = driver.find_element_by_xpath(var.NYLgetNumbers.result_1[1]).text        
            
            if pip5 != '':
                pips = [pip1, pip2, pip3, pip4, pip5]
                for pip in pips:
                    list2.append(pip)
                break
            else:
                pass
        if list1 == list2:
            print(list1)
            print(list2)
            raise Exception("Numbers not random!")
        else:
            print(list1)
            print(list2)

   
    def test_03bullseye(self):
        driver = self.driver
        funct.waitAndClick(driver, var.NYLdashboard.guest_b)
        # [Documentation - detail] swipes leftward until the "get started" button is found, then clicks it
        funct.swipeLeftUntil(driver, var.NYLregistration.pip6, var.NYLregistration.getStarted_b)
        funct.waitAndClick(driver, var.NYLregistration.getStarted_b)
        time.sleep(1)
        funct.waitAndClick(driver, var.NYLgamesDB.hamburger_b)
        funct.waitAndClick(driver, var.NYLgamesDB.menu_GetNumbers)
        funct.waitAndClick(driver, var.NYLgetNumbers.findGame_dropdown)
        funct.waitAndClick(driver, var.NYLgetNumbers.dropdown_powerball)
        funct.swipeUpUntil(driver, var.NYLregistration.base, var.NYLgetNumbers.bullseye_b)
        funct.waitAndClick(driver, var.NYLgetNumbers.bullseye_b)
        numpy.set_printoptions(threshold=numpy.inf)
        list1 = []
        list2 = []
        counter = 0
        while True:
            counter += 1
            #print(counter)
            # driver.save_screenshot('frame' + str(counter) + '.png')
            # img_rgb = cv2.imread('frame' + str(counter) + '.png')
            driver.save_screenshot('frame.png')
            img_rgb = cv2.imread('frame.png')
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

            img = Image.open('target.png')
            size= driver.get_window_size()
            width = int(size['width'])
            height = int(size['height'])
            tw = int(width*0.05185185)
            wpercent = (tw / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((tw, hsize), PIL.Image.ANTIALIAS)
            img.save('resized_image.png')  

            template = cv2.imread('resized_image.png',0)
            w, h = template.shape[::-1]
            res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
            threshold = 0.65
            loc = numpy.where( res >= threshold)
            if len(str(loc)) > 0:
                for pt in zip(*loc[::-1]):
                    x = pt[0]
                    y = pt[1]
                    # print(counter)
                    #print('----truck found')
                    # print(pt)
                    # driver.save_screenshot('foleyres' + str(counter) + '.png')
                    size= driver.get_window_size()
                    width = int(size['width'])
                    height = int(size['height'])
                    xw = width*0.104
                    yw = height*0.006
                    funct.coordinateClick(driver, x + xw, y + yw)
            pip5 = driver.find_element_by_xpath(var.NYLgetNumbers.result_5[1]).text        
            pip4 = driver.find_element_by_xpath(var.NYLgetNumbers.result_4[1]).text        
            pip3 = driver.find_element_by_xpath(var.NYLgetNumbers.result_3[1]).text        
            pip2 = driver.find_element_by_xpath(var.NYLgetNumbers.result_2[1]).text        
            pip1 = driver.find_element_by_xpath(var.NYLgetNumbers.result_1[1]).text        
          
            if pip5 != '':
                pips = [pip1, pip2, pip3, pip4, pip5]
                for pip in pips:
                    list1.append(pip)
                break
            else:
                pass
        funct.waitAndClick(driver, var.NYLgetNumbers.niagara_startOver)
        while True:
            counter += 1
            #print(counter)
            driver.save_screenshot('frame.png')
            img_rgb = cv2.imread('frame.png')
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
            template = cv2.imread('resized_image.png',0)
            w, h = template.shape[::-1]
            res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
            threshold = 0.65
            loc = numpy.where( res >= threshold)
            if len(str(loc)) > 0:
                for pt in zip(*loc[::-1]):
                    x = pt[0]
                    y = pt[1]
                    size= driver.get_window_size()
                    width = int(size['width'])
                    height = int(size['height'])
                    xw = width*0.104
                    yw = height*0.006
                    funct.coordinateClick(driver, x + xw, y + yw)
            pip5 = driver.find_element_by_xpath(var.NYLgetNumbers.result_5[1]).text        
            pip4 = driver.find_element_by_xpath(var.NYLgetNumbers.result_4[1]).text        
            pip3 = driver.find_element_by_xpath(var.NYLgetNumbers.result_3[1]).text        
            pip2 = driver.find_element_by_xpath(var.NYLgetNumbers.result_2[1]).text        
            pip1 = driver.find_element_by_xpath(var.NYLgetNumbers.result_1[1]).text        
            
            if pip5 != '':
                pips = [pip1, pip2, pip3, pip4, pip5]
                for pip in pips:
                    list2.append(pip)
                break
            else:
                pass
        if list1 == list2:
            print(list1)
            print(list2)
            raise Exception("Numbers not random!")
        else:
            print(list1)
            print(list2)


# Boiler plate code to run the test suite
if __name__ == "__main__":
    # First runner will enable html logs on your current directory, second runner will keep local console logs
    unittest.main(warnings='ignore', testRunner=HtmlTestRunner.HTMLTestRunner(output='html_report_dir'))
    # unittest.main(warnings='ignore')